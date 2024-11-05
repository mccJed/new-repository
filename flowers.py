def main():
    flowers = []

    print("Enter the names of flowers. Type 'done' when you are finished:")
    
    # user input
    while True:
        flower = input("Enter flower name: ").strip()
        if flower.lower() == "done":
            break
        flowers.append(flower.title()) 

    # sort
    flowers.sort()

    # print the sorted flowers
    print("\nSorted list of flowers:")
    for i, flower in enumerate(flowers, start=1):
        print(f"{i}. {flower}")

    # Search by name
    search_flower = input("\nEnter the name of a flower to search for: ").title()
    if search_flower in flowers:
        print(f"'{search_flower}' is in the list!")
    else:
        print(f"'{search_flower}' is not in the list.")

    # search by number
    try:
        choice = int(input("\nEnter the number of the flower you want to access: "))
        selected_flower = flowers[choice - 1]
        print(f"The flower at position {choice} is: {selected_flower}")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("The number you entered is out of range.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run
if __name__ == "__main__":
    main()
