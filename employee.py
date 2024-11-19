# Employee and ProductionWorker Classes
class Employee:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number

    def __str__(self):
        return f"Employee Name: {self._name}, Employee Number: {self._number}"


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self._shift_number = shift_number
        self._hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self._shift_number

    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self._hourly_pay_rate = hourly_pay_rate

    def __str__(self):
        return (
            super().__str__()
            + f", Shift Number: {self._shift_number}, Hourly Pay Rate: ${self._hourly_pay_rate:.2f}"
        )


def main():
    print("\n--- Create a Production Worker ---")
    name = input("Enter employee name: ")
    number = input("Enter employee number: ")
    shift_number = int(input("Enter shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))

    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)
    print("\n--- Production Worker Details ---")
    print(worker)


if __name__ == "__main__":
    main()
