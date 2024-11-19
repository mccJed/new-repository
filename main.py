from employee import ProductionWorker  # Import classes from employee.py

def main():
    print("\n--- Create a Production Worker ---")
    # Prompt user for details
    name = input("Enter employee name: ")
    number = input("Enter employee number: ")
    shift_number = int(input("Enter shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))

    # Create a ProductionWorker object
    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)

    # Display the data using the object's methods
    print("\n--- Production Worker Details ---")
    print(worker)

if __name__ == "__main__":
    main()
