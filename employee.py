# Employee superclass
class Employee:
    def __init__(self, name, number):
        self._name = name  # Protected attribute
        self._number = number

    # Getter and Setter for Employee name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and Setter for Employee number
    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number

    def __str__(self):
        return f"Employee Name: {self._name}, Employee Number: {self._number}"


# ProductionWorker subclass
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self._shift_number = shift_number
        self._hourly_pay_rate = hourly_pay_rate

    # Getter and Setter for shift number
    def get_shift_number(self):
        return self._shift_number

    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    # Getter and Setter for hourly pay rate
    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self._hourly_pay_rate = hourly_pay_rate

    def __str__(self):
        return (
            super().__str__()
            + f", Shift Number: {self._shift_number}, Hourly Pay Rate: ${self._hourly_pay_rate:.2f}"
        )
