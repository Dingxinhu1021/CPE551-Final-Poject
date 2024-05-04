from Media import Media  # Import the Media base class

class Show(Media):  # Subclass of Media
    def __init__(self, media_id, title, avg_rating, show_type, directors, actors, country_code, date_added, release_year, rating, duration, genres, description):
        # Initialize Media's attributes
        super().__init__(media_id, title, avg_rating)
        
        # Initialize Show's specific attributes
        self._show_type = show_type
        self._directors = directors
        self._actors = actors
        self._country_code = country_code
        self._date_added = date_added
        self._release_year = release_year
        self._rating = rating
        self._duration = duration
        self._genres = genres
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

# Example usage
if __name__ == "__main__":
    show = Show(1, "Breaking Bad", 9.5, "TV Show", "Vince Gilligan", "Bryan Cranston, Aaron Paul", "US", "01/20/2008", 2008, "TV-MA", "5 Seasons", "Drama, Crime", "A high school chemistry teacher turned methamphetamine manufacturing drug dealer teams with a former student.")
    print(f"Show Title: {show.get_title()}, Type: {show.get_show_type()}, Directors: {show.get_directors()}")
