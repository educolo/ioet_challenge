import unittest

from src.employee import DayWorkedTime, Employee
from src.exceptions import NoPaymentRuleError, NoRulesForPaymentError, NoEmployeeForPaymentError
from src.payment import Payment, Rule


class TestAddNumbers(unittest.TestCase):

    def test_get_weekday_rules_success(self):
        employee = Employee("RENE", [])
        rules = (
            Rule(['MO'], 0, 9, 25),
            Rule(['SU'], 9, 18, 15),
            Rule(['MO'], 18, 24, 20)
        )
        payment = Payment(employee, rules)

        one_rule = payment._get_rules_for_weekday('SU')
        two_rules = payment._get_rules_for_weekday('MO')
        self.assertEqual(1, len(one_rule))
        self.assertEqual(2, len(two_rules))

    def test_get_weekday_rules_raise_error_on_zero_matching_rules(self):
        employee = Employee("RENE", [])
        rules = (
            Rule(['MO'], 0, 9, 25),
            Rule(['SU'], 9, 18, 15),
            Rule(['MO'], 18, 24, 20)
        )
        payment = Payment(employee, rules)

        with self.assertRaises(NoPaymentRuleError):
            zero_rule = payment._get_rules_for_weekday('XX')

    def test_create_employee_from_string(self):
        employee = Employee.create_from_string(
            "RENE=MO10:00-12:00,TU10:00-12:00"
        )
        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.name, "RENE")
        self.assertEqual(len(employee.worked_time), 2)
        for worked_day in employee.worked_time:
            self.assertIsInstance(worked_day, DayWorkedTime)

    def test_create_day_worked_time_from_string(self):
        day_worked_time = DayWorkedTime.create_from_string(
            "MO10:00-12:00"
        )
        self.assertIsInstance(day_worked_time, DayWorkedTime)
        self.assertEqual("MO", day_worked_time.weekday)
        self.assertEqual(10, day_worked_time.start)
        self.assertEqual(12, day_worked_time.end)

    def test_day_payment_with_one_rule(self):
        employee = Employee.create_from_string(
            "RENE=MO10:00-12:00,TU10:00-12:00"
        )
        rules = (
            Rule(['MO'], 9, 18, 25),
        )
        payment = Payment(employee, rules)

        day_payment = payment._get_day_payment(10, 12, rules)
        self.assertEqual(50, day_payment)

    def test_day_payment_with_three_rules(self):
        employee = Employee.create_from_string(
            "RENE=MO10:00-12:00,TU10:00-12:00"
        )
        rules = (
            Rule(['MO'], 0, 9, 15),
            Rule(['MO'], 9, 18, 25),
            Rule(['MO'], 18, 24, 30)
        )
        payment = Payment(employee, rules)

        day_payment = payment._get_day_payment(10, 12, rules)
        self.assertEqual(50, day_payment)

    def test_day_payment_with_two_rules_apply(self):
        employee = Employee.create_from_string(
            "RENE=MO10:00-12:00,TU10:00-12:00"
        )
        rules = (
            Rule(['MO'], 0, 9, 15),
            Rule(['MO'], 9, 18, 25),
            Rule(['MO'], 18, 24, 30)
        )
        payment = Payment(employee, rules)

        day_payment = payment._get_day_payment(7, 12, rules)
        self.assertEqual(30 + 75, day_payment)

    def test_day_payment_with_three_rules_apply(self):
        employee = Employee.create_from_string(
            "RENE=MO10:00-12:00,TU10:00-12:00"
        )
        rules = (
            Rule(['MO'], 0, 9, 15),
            Rule(['MO'], 9, 18, 25),
            Rule(['MO'], 18, 24, 30)
        )
        payment = Payment(employee, rules)

        day_payment = payment._get_day_payment(7, 22, rules)
        self.assertEqual(30 + 225 + 120, day_payment)

    def test_total_payment(self):
        employee = Employee.create_from_string(
            "RENE=MO10:00-12:00,TU08:00-19:00"
        )
        rules = (
            Rule(['MO'], 0, 9, 15),
            Rule(['MO'], 9, 18, 25),
            Rule(['MO'], 18, 24, 30),
            Rule(['TU'], 0, 9, 17),
            Rule(['TU'], 9, 18, 27),
            Rule(['TU'], 18, 24, 33),
        )
        payment = Payment(employee, rules)
        total_payment = payment.get_total_payment()

        self.assertEqual(50 + 17 + 9*27 + 33, total_payment)

    def test_total_payment_raises_error_without_rules(self):
        employee = Employee.create_from_string(
            "RENE=MO10:00-12:00,TU08:00-19:00"
        )
        payment = Payment(employee)
        with self.assertRaises(NoRulesForPaymentError):
            total_payment = payment.get_total_payment()

    def test_total_payment_raises_error_without_employee(self):
        rules = (
            Rule(['MO'], 0, 9, 15),
        )
        payment = Payment(payment_rules=rules)
        with self.assertRaises(NoEmployeeForPaymentError):
            total_payment = payment.get_total_payment()

    def test_total_payment_with_half_hour(self):
        employee = Employee.create_from_string(
            "RENE=MO10:00-10:30"
        )
        rules = (
            Rule(['MO'], 0, 9, 15),
            Rule(['MO'], 9, 18, 25),
            Rule(['MO'], 18, 24, 30),
        )
        payment = Payment(employee, rules)
        total_payment = payment.get_total_payment()

        self.assertEqual(12.5, total_payment)

    def test_total_payment_with_half_hour_from_different_rules(self):
        employee = Employee.create_from_string(
            "RENE=MO08:30-09:30"
        )
        rules = (
            Rule(['MO'], 0, 9, 15),
            Rule(['MO'], 9, 18, 25),
            Rule(['MO'], 18, 24, 30),
        )
        payment = Payment(employee, rules)
        total_payment = payment.get_total_payment()

        self.assertEqual(12.5 + 7.5, total_payment)