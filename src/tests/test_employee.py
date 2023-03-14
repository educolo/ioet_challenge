import unittest

from src.employee import DayWorkedTime, Employee


class TestEmployee(unittest.TestCase):
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
