class Media:
    def __init__(self, media_id, title, avg_rating):
        # Initialize the private member variables
        self._id = media_id
        self._title = title
        self._avg_rating = avg_rating

    # Accessor (getter) for the ID
    def get_id(self):
        return self._id

    # Mutator (setter) for the ID
    def set_id(self, media_id):
        self._id = media_id

    # Accessor (getter) for the title
    def get_title(self):
        return self._title

    # Mutator (setter) for the title
    def set_title(self, title):
        self._title = title

    # Accessor (getter) for the average rating
    def get_avg_rating(self):
        return self._avg_rating

    # Mutator (setter) for the average rating
    def set_avg_rating(self, avg_rating):
        self._avg_rating = avg_rating

# Example usage
if __name__ == "__main__":
    # Creating an instance of Media
    media_example = Media(101, "Example Title", 4.5)
    
    # Accessing and printing details
    print(f"Media ID: {media_example.get_id()}")
    print(f"Title: {media_example.get_title()}")
    print(f"Average Rating: {media_example.get_avg_rating()}")

    # Updating and printing the title
    media_example.set_title("New Example Title")
    print(f"Updated Title: {media_example.get_title()}")
