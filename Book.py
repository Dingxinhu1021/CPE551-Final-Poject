# Author: Dingxin Hu /Ruiyang Hu
# Date: 2024-05-04
# Description:
# The Book class is a subclass of Media, specifically designed to represent books.
# It extends the basic attributes to include authors, two types of ISBN numbers,
# language code, page count, number of ratings, publication date, and publisher.
# This class takes these details through a constructor and provides corresponding accessor
# and mutator methods to ensure data integrity and secure access.


from Media import Media  # Import the Media base class

class Book(Media):  # Subclass of Media
    def __init__(self, media_id, title, avg_rating, authors, isbn, isbn13, language_code, num_pages, ratings_count, publication_date, publisher):
        # Initialize Media's attributes
        super().__init__(media_id, title, avg_rating)

        # Initialize Book's specific attributes
        self._authors = authors
        self._isbn = isbn
        self._isbn13 = isbn13
        self._language_code = language_code
        self._num_pages = num_pages
        self._ratings_count = ratings_count
        self._publication_date = publication_date
        self._publisher = publisher

    # Accessors (getters) and Mutators (setters) for each attribute
    def get_authors(self):
        return self._authors

    def set_authors(self, authors):
        self._authors = authors

    def get_avg_rating(self):
        return self._avg_rating

    def set_avg_rating(self, avg_rating):
        self._avg_rating = avg_rating

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn

    def get_isbn13(self):
        return self._isbn13

    def set_isbn13(self, isbn13):
        self._isbn13 = isbn13

    def get_language_code(self):
        return self._language_code

    def set_language_code(self, language_code):
        self._language_code = language_code

    def get_num_pages(self):
        return self._num_pages

    def set_num_pages(self, num_pages):
        self._num_pages = num_pages

    def get_ratings_count(self):
        return self._ratings_count

    def set_ratings_count(self, ratings_count):
        self._ratings_count = ratings_count

    def get_publication_date(self):
        return self._publication_date

    def set_publication_date(self, publication_date):
        self._publication_date = publication_date

    def get_publisher(self):
        return self._publisher

    def set_publisher(self, publisher):
        self._publisher = publisher
