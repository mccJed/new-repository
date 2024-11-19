class NotNumericError(Exception):
    def __init__(self, message="Input is not a numeric value. Please try again."):
        self.message = message
        super().__init__(self.message)

def get_number():
    while True: 
        try:
            user_input = input("Enter a number: ")
       
            if not user_input.isnumeric():
                raise NotNumericError
            else:
                print(f"Valid input received: {user_input}")
                return int(user_input)
        except NotNumericError as e:
            print(f"Error: {e}")
        finally:
            print("Execution of this attempt is complete.")

def main():
    print("Welcome to the Number Validator Program!")
    valid_number = get_number()
    print(f"Success! You entered the number: {valid_number}")
    print("Program has ended.")

if __name__ == "__main__":
    main()
