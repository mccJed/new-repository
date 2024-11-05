def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

  # print artists
    print("Current list of top artists:")
    for i, artist in enumerate(top_artists, start=1):
        print(f"{i}: {artist}")

    replace_artist(top_artists)
    
    print("\nUpdated list of top artists:")
    for i, artist in enumerate(top_artists, start=1):
        print(f"{i}: {artist}")

def replace_artist(artists_list):
    try:
        # user input for new artist
        index = int(input("\nEnter the number of the artist you want to replace (1-10): ")) - 1  
        new_artist = input("Enter the name of the new artist: ")

        # Replace the artist
        artists_list[index] = new_artist
        print(f"\nArtist at position {index + 1} has been replaced with '{new_artist}'.")

    except (ValueError, IndexError):
        print("An input error occurred. Please enter a valid number for the index (1-10)")

# Run
if __name__ == "__main__":
    main()
