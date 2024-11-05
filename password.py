def main():
    print("Welcome! Please create a password that meets the following criteria:")
    print("- Between 8 to 20 characters long")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one number")
    print("- At least one special character")
    special_characters = "!@#$%&*"
    
    while True:
        try:
            # user input
            password = input("Enter your password: ")

            # length
            if len(password) < 8 or len(password) > 20:
                raise ValueError("Password must be between 8 and 20 characters long.")

            # Uppercase
            if not any(char.isupper() for char in password):
                raise ValueError("Password must contain at least one uppercase letter.")
            
            # Lowercase
            if not any(char.islower() for char in password):
                raise ValueError("Password must contain at least one lowercase letter.")
            
            # Number
            if not any(char.isdigit() for char in password):
                raise ValueError("Password must contain at least one number.")
            
            # Special Character
            if not any(char in special_characters for char in password):
                raise ValueError("Password must contain at least one special character")
            
            # Confirm
            confirm_password = input("Re-enter your password for confirmation: ")

            # Check if passwords match
            if password != confirm_password:
                print("Passwords do not match. Please try again.")
                continue

            # Success
            print("Password successfully created!")
            break

        except ValueError as e:
            print(f"Error: {e}")

# run
if __name__ == "__main__":
    main()
