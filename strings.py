def main():
    # Example string
    example_string = "Hello, Python programmers!"
    
    # Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char, end=' ')
    
    # Find and print the character with the minimum ASCII value in the string
    min_char = min(example_string)
    print("\n\nCharacter with the minimum ASCII value:", min_char)
    
    # Find and print the character with the maximum ASCII value in the string
    max_char = max(example_string)
    print("Character with the maximum ASCII value:", max_char)
    
    # Find and print the index of the first occurrence of 'o' in the string
    index_o = example_string.find('o')
    print("Index of 'o':", index_o)
    
    # Convert the string into a list of characters and print the list
    char_list = list(example_string)
    print("Converting string to a list of characters:", char_list)
    
    # Count and print the number of occurrences of 'o' in the string
    count_o = example_string.count('o')
    print("Count of 'o' in the string:", count_o)

# Call the main function to run the program
if __name__ == "__main__":
    main()