import csv
from tkinter import filedialog, messagebox, Tk
from Book import Book
from Show import Show

class Recommender:
    def __init__(self):
        self.books = {}
        self.shows = {}
        self.associations = {}

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
        movie_list = "Title\t\tRuntime\n"
        for show in self.shows.values():
            if isinstance(show, Show) and show.get_show_type() == 'Movie':
                movie_list += f"{show.get_title()}\t\t{show.get_duration()}\n"
        return movie_list

    def get_tv_list(self):
        tv_list = "Title\t\tSeasons\n"
        for show in self.shows.values():
            if isinstance(show, Show) and show.get_show_type() == 'TV Show':
                tv_list += f"{show.get_title()}\t\t{show.get_duration()}\n"
        return tv_list

    def get_book_list(self):
        book_list = "Title\t\tAuthors\n"
        for book in self.books.values():
            if isinstance(book, Book):
                book_list += f"{book.get_title()}\t\t{book.get_authors()}\n"
        return book_list

    def get_movie_stats(self):
        ratings = {}
        total_duration = 0
        count = 0
        for show in self.shows.values():
            if isinstance(show, Show) and show.get_show_type() == 'Movie':
                rating = show.get_rating()
                duration = int(show.get_duration().replace(' min', ''))
                ratings[rating] = ratings.get(rating, 0) + 1
                total_duration += duration
                count += 1

        average_duration = total_duration / count if count else 0
        ratings_percentages = {k: (v / count) * 100 for k, v in ratings.items()}
        
        return {
            'Average Duration': f"{average_duration:.2f} minutes",
            'Ratings Distribution': ratings_percentages
        }
        def get_tv_stats(self):
        ratings = {}
        total_seasons = 0
        count = 0
        for show in self.shows.values():
            if isinstance(show, Show) and show.get_show_type() == 'TV Show':
                rating = show.get_rating()
                seasons = int(show.get_duration().replace(' Seasons', '').replace(' Season', ''))
                ratings[rating] = ratings.get(rating, 0) + 1
                total_seasons += seasons
                count += 1

        average_seasons = total_seasons / count if count else 0
        ratings_percentages = {k: (v / count) * 100 for k, v in ratings.items()}
        
        return {
            'Average Seasons': f"{average_seasons:.2f}",
            'Ratings Distribution': ratings_percentages
        }

    def get_book_stats(self):
        total_pages = 0
        count = 0
        for book in self.books.values():
            if isinstance(book, Book):
                pages = int(book.get_num_pages())
                total_pages += pages
                count += 1

        average_pages = total_pages / count if count else 0
        
        return {'Average Page Count': f"{average_pages:.2f}"}
    

    def search_tv_movies(self, show_type, title, director, actor, genre):
        if show_type not in ['Movie', 'TV Show']:
            return None, "Please select 'Movie' or 'TV Show' from Type first."

        if not any([title, director, actor, genre]):
            return None, "Please enter information for Title, Director, Actor, and/or Genre."

        results = []
        for show_id, show in self.shows.items():
            if show['type'] == show_type and \
               (not title or title.lower() in show['title'].lower()) and \
               (not director or director.lower() in show.get('director', '').lower()) and \
               (not actor or any(actor.lower() in x.lower() for x in show.get('cast', '').split(', '))) and \
               (not genre or genre.lower() in show.get('listed_in', '').lower()):
                results.append(f"{show['title']} - {show['director']} - {', '.join(show['cast'])} - {show['listed_in']}")

        return '\n'.join(results), ""
    

    def search_books(self, title, author, publisher):
        if not any([title, author, publisher]):
            return None, "Please enter information for Title, Author, and/or Publisher."

        results = []
        max_title_len = max_author_len = max_publisher_len = 0
        for book_id, book in self.books.items():
            if (not title or title.lower() in book['title'].lower()) and \
               (not author or author.lower() in book['authors'].lower()) and \
               (not publisher or publisher.lower() in book['publisher'].lower()):
                results.append(book)
                max_title_len = max(max_title_len, len(book['title']))
                max_author_len = max(max_author_len, len(book['authors']))
                max_publisher_len = max(max_publisher_len, len(book['publisher']))

        if not results:
            return None, "No Results"

        header = f"{'Title'.ljust(max_title_len)}  {'Author'.ljust(max_author_len)}  {'Publisher'.ljust(max_publisher_len)}\n"
        formatted_results = [header]
        formatted_results.extend([f"{book['title'].ljust(max_title_len)}  {book['authors'].ljust(max_author_len)}  {book['publisher'].ljust(max_publisher_len)}" for book in results])
        
        return '\n'.join(formatted_results), ""

# Example instantiation and use of the Recommender class
if __name__ == "__main__":
    recommender = Recommender()
    # These methods would be triggered by GUI actions or other parts of the program

