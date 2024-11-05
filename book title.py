# Program for collecting and sorting book titles

def main():
    books = []
    
    # user input
    print("Please enter 10 book titles:")
    while len(books) < 10:
        title = input(f"Enter title {len(books) + 1}: ")
        books.append(title.title())

    # Sorted list
    sorted_titles = sorted(books)
    
    print("\nBook Titles in Alphabetical Order:")
    for title in sorted_titles:
        print(title)

if __name__ == "__main__":
    main()
