import csv
from tkinter import filedialog, messagebox, Tk
from Book import Book
from Show import Show
from collections import Counter

class Recommender:
    def __init__(self):
        self.books = {}
        self.shows = {}
        self.associations = {}
        self.movies = {}  # Initialize as an empty dictionary or appropriate data structure
        self.shows = {}   # Initialize as an empty dictionary or appropriate data structure


    def load_books(self):
        root = Tk()
        root.withdraw()  # Hides the main window
        file_path = filedialog.askopenfilename(title="Select a book file")
        while not file_path:
            messagebox.showerror("Error", "Please select a book file.")
            file_path = filedialog.askopenfilename(title="Select a book file")

        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                book = Book(row['bookID'], row['title'], row['average_rating'], row['authors'],
                            row['isbn'], row['isbn13'], row['language_code'], row['num_pages'],
                            row['ratings_count'], row['publication_date'], row['publisher'])
                self.books[book.get_id()] = book
        root.destroy()

    def load_shows(self):
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Select a show file")
        while not file_path:
            messagebox.showerror("Error", "Please select a show file.")
            file_path = filedialog.askopenfilename(title="Select a show file")

        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                show = Show(row['show_id'], row['title'], row['average_rating'], row['type'],
                            row['director'], row['cast'], row['country'], row['date_added'],
                            row['release_year'], row['rating'], row['duration'],
                            row['listed_in'], row['description'])
                self.shows[show.get_id()] = show
        root.destroy()

    def load_associations(self):
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Select an association file")
        while not file_path:
            messagebox.showerror("Error", "Please select an association file.")
            file_path = filedialog.askopenfilename(title="Select an association file")

        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                id1, id2 = row
                if id1 not in self.associations:
                    self.associations[id1] = {}
                if id2 not in self.associations[id1]:
                    self.associations[id1][id2] = 0
                self.associations[id1][id2] += 1

                # Repeat for reverse association
                if id2 not in self.associations:
                    self.associations[id2] = {}
                if id1 not in self.associations[id2]:
                    self.associations[id2][id1] = 0
                self.associations[id2][id1] += 1
        root.destroy()

    def get_movie_list(self):
        movie_list = "Title\t\t\t\t\t\t\t\t\t\t\t\tRuntime\n"
        for show in self.shows.values():
            if isinstance(show, Show) and show.get_show_type() == 'Movie':
                movie_list += f"{show.get_title()}\t\t\t\t\t\t\t\t\t\t\t\t{show.get_duration()}\n"
        return movie_list

    def get_tv_list(self):
        tv_list = "Title\t\t\t\t\t\t\t\t\t\t\t\tSeasons\n"
        for show in self.shows.values():
            if isinstance(show, Show) and show.get_show_type() == 'TV Show':
                tv_list += f"{show.get_title()}\t\t\t\t\t\t\t\t\t\t\t\t{show.get_duration()}\n"
        return tv_list

    def get_book_list(self):
        book_list = "Title\t\t\t\t\t\t\t\t\t\t\t\tAuthors\n"
        for book in self.books.values():
            if isinstance(book, Book):
                book_list += f"{book.get_title()}\t\t\t\t\t\t\t\t\t\t\t\t{book.get_authors()}\n"
        return book_list

    def get_movie_stats(self):
        ratings = {}
        total_duration = 0
        directors = Counter()
        actors = Counter()
        genres = Counter()

        for show in self.shows.values():
            if isinstance(show, Show) and show.get_show_type() == 'Movie':
                duration = int(show.get_duration().replace(' min', ''))
                ratings[show.get_rating()] = ratings.get(show.get_rating(), 0) + 1
                total_duration += duration
                # Corrected method names:
                directors.update(show.get_directors().split(', '))
                actors.update(show.get_actors().split(', '))
                genres.update(show.get_genres().split(', '))

        count = len([show for show in self.shows.values() if isinstance(show, Show) and show.get_show_type() == 'Movie'])
        average_duration = total_duration / count if count else 0
        ratings_percentages = {k: f"{(v / count * 100):.2f}%" for k, v in ratings.items()}

        most_common_director = directors.most_common(1)[0] if directors else ("None", 0)
        most_common_actor = actors.most_common(1)[0] if actors else ("None", 0)
        most_common_genre = genres.most_common(1)[0] if genres else ("None", 0)

        return {
            'Average Duration': f"{average_duration:.2f} minutes",
            'Ratings Distribution': ratings_percentages,
            'Most Common Director': most_common_director,
            'Most Common Actor': most_common_actor,
            'Most Common Genre': most_common_genre
        }

    def get_tv_stats(self):
        ratings = {}
        total_seasons = 0
        actors = Counter()
        genres = Counter()

        for show in self.shows.values():
            if isinstance(show, Show) and show.get_show_type() == 'TV Show':
                seasons = int(show.get_duration().replace(' Seasons', '').replace(' Season', ''))
                ratings[show.get_rating()] = ratings.get(show.get_rating(), 0) + 1
                total_seasons += seasons
                actors.update(show.get_actors().split(', '))
                genres.update(show.get_genres().split(', '))

        count = len([show for show in self.shows.values() if isinstance(show, Show) and show.get_show_type() == 'TV Show'])
        average_seasons = total_seasons / count if count else 0
        ratings_percentages = {k: f"{(v / count * 100):.2f}%" for k, v in ratings.items()}

        most_common_actor = actors.most_common(1)[0] if actors else ("None", 0)
        most_common_genre = genres.most_common(1)[0] if genres else ("None", 0)

        return {
            'Average Seasons': f"{average_seasons:.2f}",
            'Ratings Distribution': ratings_percentages,
            'Most Common Actor': most_common_actor,
            'Most Common Genre': most_common_genre
        }

    def get_book_stats(self):
        total_pages = 0
        authors = Counter()
        publishers = Counter()

        for book in self.books.values():
            pages = int(book.get_num_pages())
            total_pages += pages
            authors[book.get_authors()] += 1
            publishers[book.get_publisher()] += 1

        count = len(self.books)
        average_pages = total_pages / count if count else 0
        most_common_author = authors.most_common(1)[0] if authors else ("None", 0)
        most_common_publisher = publishers.most_common(1)[0] if publishers else ("None", 0)

        return {
            'Average Page Count': f"{average_pages:.2f} pages",
            'Most Common Author': most_common_author,
            'Most Common Publisher': most_common_publisher
        }
    

    def search_tv_movies(self, show_type, title, director, actor, genre):
        if show_type not in ['Movie', 'TV Show']:
            return None, "Please select 'Movie' or 'TV Show' from Type first."

        if not any([title, director, actor, genre]):
            return None, "Please enter information for Title, Director, Actor, and/or Genre."

        results = []
        max_title_len = max_director_len = max_actor_len = max_genre_len = 0
        for show in self.shows.values():
            if show.get_show_type() == show_type and \
               (not title or title.lower() in show.get_title().lower()) and \
               (not director or director.lower() in show.get_directors().lower()) and \
               (not actor or any(actor.lower() in actor_name.lower() for actor_name in show.get_actors().split(', '))) and \
               (not genre or genre.lower() in show.get_genres().lower()):
                results.append(show)
                max_title_len = max(max_title_len, len(show.get_title()))
                max_director_len = max(max_director_len, len(show.get_directors()))
                max_actor_len = max(max_actor_len, max(len(actor_name) for actor_name in show.get_actors().split(', ')))
                max_genre_len = max(max_genre_len, len(show.get_genres()))

        if not results:
            return "No Results", None

        # Create a formatted header
        format_str = f"{{:<{max_title_len}}}  {{:<{max_director_len}}}  {{:<{max_actor_len}}}  {{:<{max_genre_len}}}\n"
        header = format_str.format("Title", "Director", "Actors", "Genres")
        formatted_results = [header] + [
            format_str.format(show.get_title(), show.get_directors(), ', '.join(show.get_actors().split(', ')), show.get_genres())
            for show in results
        ]

        return '\n'.join(formatted_results), None
    

    def search_books(self, title, author, publisher):
        if not any([title, author, publisher]):
            return None, "Please enter information for Title, Author, and/or Publisher."

        results = []
        max_title_len = max_author_len = max_publisher_len = 0
        for book_id, book in self.books.items():
            # Assuming you have methods like get_title(), get_authors(), get_publisher() in your Book class
            if (not title or title.lower() in book.get_title().lower()) and \
               (not author or author.lower() in book.get_authors().lower()) and \
               (not publisher or publisher.lower() in book.get_publisher().lower()):
                results.append(book)
                max_title_len = max(max_title_len, len(book.get_title()))
                max_author_len = max(max_author_len, len(book.get_authors()))
                max_publisher_len = max(max_publisher_len, len(book.get_publisher()))

        if not results:
            return "No Results", None

        header = f"{'Title'.ljust(max_title_len)}  {'Author'.ljust(max_author_len)}  {'Publisher'.ljust(max_publisher_len)}\n"
        formatted_results = [header]
        formatted_results.extend([f"{book.get_title().ljust(max_title_len)}  {book.get_authors().ljust(max_author_len)}  {book.get_publisher().ljust(max_publisher_len)}" for book in results])
    
        return '\n'.join(formatted_results), None
        
    def get_recommendations(self, media_type, title):
        recommendations = []
        if media_type in ['Movie', 'TV Show']:
            found = False
            for show in self.shows.values():
                if show.get_show_type() == media_type and title.lower() in show.get_title().lower():
                    found = True
                    associated_books = self.associations.get(show.get_id(), [])
                    if not associated_books:
                        recommendations.append("No associated books found for this title.")
                    else:
                        for book_id in associated_books:
                            if book_id in self.books:
                                book = self.books[book_id]
                                book_details = (f"Title: {book.get_title()}\nAuthor: {book.get_authors()}\n"
                                                f"Avg Rating: {book.get_avg_rating()}\nIsbn: {book.get_isbn()}\n"
                                                f"Isbn13: {book.get_isbn13()}\nLanguage Coder: {book.get_language_code()}\n"
                                                f"Num Pages: {book.get_num_pages()}\nAtings Count: {book.get_ratings_count()}\n"
                                                f"Publication Date: {book.get_publication_date()}\nPublisher: {book.get_publisher()}\n\n")
                                
                                recommendations.append(book_details)
            if not found:
                messagebox.showwarning("Warning", "No recommendations for that title")
                return "No results"

        elif media_type == 'Book':
            found = False
            for book in self.books.values():
                if title.lower() in book.get_title().lower():
                    found = True
                    associated_media = self.associations.get(book.get_id(), [])
                    if not associated_media:
                        recommendations.append("No associated movies or TV shows found for this book.")
                    else:
                        for media_id in associated_media:
                            if media_id in self.shows:
                                show = self.shows[media_id]
                                media_details = (f"Title: {show.get_title()}\nShow Type: {show.get_show_type()}\n"
                                                f"Avg Rating: {show.get_avg_rating()}\nDirectors: {show.get_directors()}\n"
                                                f"Actors: {show.get_actors()}\nCountry: {show.get_country_code()}\n"
                                                f"Date Added: {show.get_date_added()}\nRelease Year: {show.get_release_year()}\n"
                                                f"Rating: {show.get_rating()}\nDuration: {show.get_duration()}\n"
                                                f"Genres: {show.get_genres()}\nDescription: {show.get_description()}\n\n")
                                recommendations.append(media_details)
            if not found:
                messagebox.showwarning("Warning", "No recommendations for that title")
                return "No results"

        if not recommendations:
            return "No results found."
        else:
            return "\n".join(recommendations)
        


if __name__ == "__main__":
    recommender = Recommender()
    # These methods would be triggered by GUI actions or other parts of the program
