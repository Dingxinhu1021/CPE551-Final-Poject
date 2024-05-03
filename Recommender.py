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
