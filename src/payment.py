from .exceptions import NoEmployeeForPaymentError, NoPaymentRuleError, NoRulesForPaymentError


class Payment:
    def __init__(self, employee=None, payment_rules=None):
        self.employee = employee
        self.payment_rules = payment_rules

    def get_total_payment(self):
        """ Calculate the employee total payment.

        Returns
        -------
        int

        Raises
        ------
        NoEmployeeForPaymentError
            If self.employee is None
        NoRulesForPaymentError
            If payment_rules is empty or None
        """

        if self.employee is None:
            raise NoEmployeeForPaymentError()

        if self.payment_rules is None or len(self.payment_rules) == 0:
            raise NoRulesForPaymentError()

        payment = 0
        for worked_day in self.employee.worked_time:
            rules = self._get_rules_for_weekday(worked_day.weekday)
            payment += self._get_day_payment(worked_day.start, worked_day.end, rules)

        return payment

    def _get_day_payment(self, start, end, rules):
        """Calculate the payment for a time range with certain rules.

        Parameters
        ----------
        start : int
        end : int
        rules : list of Rule

        Returns
        -------
        int
        """
        payment = 0
        for rule in rules:
            start_rule = max(rule.start_time, start)
            end_rule = min(rule.end_time, end)
            hours = end_rule - start_rule
            if hours > 0:
                payment += hours * rule.hour_price

        return payment

    def _get_rules_for_weekday(self, weekday):
        rules = []
        for rule in self.payment_rules:
            if weekday in rule.weekdays:
                rules.append(rule)

        if len(rules) == 0:
            raise NoPaymentRuleError()
        return rules


class Rule:
    weekdays = None
    start_time = None
    end_time = None
    hour_price = 0

    def __init__(self, weekdays, start_time, end_time, hour_price):
        """
        :param weekdays: list of weekdays to apply rule
        :type weekdays: list
        :param start_time:
        :type start_time: int
        :param end_time:
        :type end_time: int
        :param hour_price:
        :type hour_price: int
        """
        self.weekdays = weekdays
        self.start_time = start_time
        self.end_time = end_time
        self.hour_price = hour_price
