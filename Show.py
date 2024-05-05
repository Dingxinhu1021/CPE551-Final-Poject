# Author: Dingxin Hu /Ruiyang Hu
# Date: 2024-05-04
# Description: The Show class, a subclass of Media,
# manages details for TV shows or series.
# It stores information like show type, directors, actors, country code, addition and release dates,
# rating, duration, genres, and a description.

from Media import Media  # Import the Media base class

class Show(Media):  # Subclass of Media
    def __init__(self, show_id, type, title, director, cast, avg_rating, country, date_added, release_year, rating, duration, listed_in, description):
        # Initialize Media's attributes
        super().__init__(show_id, title, avg_rating)

        # Initialize Show's specific attributes
        self._show_type = type
        self._directors = director
        self._actors = cast
        self._country_code = country
        self._date_added = date_added
        self._release_year = release_year
        self._rating = rating
        self._duration = duration
        self._genres = listed_in
        self._description = description

    # Accessor (getter) methods for each attribute
    def get_show_type(self):
        return self._show_type

    def get_directors(self):
        return self._directors

    def get_avg_rating(self):
        return self._avg_rating

    def get_actors(self):
        return self._actors

    def get_country_code(self):
        return self._country_code

    def get_date_added(self):
        return self._date_added

    def get_release_year(self):
        return self._release_year

    def get_rating(self):
        return self._rating

    def get_duration(self):
        return self._duration

    def get_genres(self):
        return self._genres

    def get_description(self):
        return self._description
