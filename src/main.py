import os

from src.employee import Employee
from src.payment import Payment, Rule


def print_payment_for_employees():
    conf_path = os.getcwd()
    with open(conf_path + "/src/input.txt", "r") as file:
        payment = Payment(payment_rules=create_payment_rules())
        for line in file:
            employee = Employee.create_from_string(line.strip())
            payment.employee = employee
            employee_payment = payment.get_total_payment()
            print(f'The amount to pay {employee.name} is: {employee_payment} USD')


def create_payment_rules():
    weekdays = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
    rules = []

    for day in weekdays[:5]:
        rules.append(Rule(day, 0, 9, 25))
        rules.append(Rule(day, 9, 18, 15))
        rules.append(Rule(day, 18, 24, 20))

    for day in weekdays[5:]:
        rules.append(Rule(day, 0, 9, 30))
        rules.append(Rule(day, 9, 18, 20))
        rules.append(Rule(day, 18, 24, 25))

    return rules
