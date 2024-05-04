import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from Recommender import Recommender

class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Media Recommender System")
        self.root.geometry("1200x800")

        # Create a Notebook widget
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Tabs for different functionalities
        self.setup_movie_tab()
        self.setup_tv_tab()
        self.setup_book_tab()
        self.setup_movie_tv_search_tab()
        self.setup_book_search_tab()
        self.setup_recommendation_tab()

        # Buttons for loading data and quitting
        self.setup_buttons()

        self.root.mainloop()

    def setup_movie_tab(self):
        self.movie_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.movie_tab, text='Movies')

        # Text widget for displaying movies and statistics
        self.movie_text = tk.Text(self.movie_tab, height=10, width=80)
        self.movie_text.pack(padx=10, pady=10, fill='both', expand=True)
        self.movie_text.insert('1.0', 'No movie data loaded yet.')

        # Scrollbar
        self.movie_scroll = ttk.Scrollbar(self.movie_tab, orient='vertical', command=self.movie_text.yview)
        self.movie_scroll.pack(side='right', fill='y')
        self.movie_text['yscrollcommand'] = self.movie_scroll.set

    def setup_tv_tab(self):
        self.tv_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.tv_tab, text='TV Shows')

        # Text widget for displaying TV shows and statistics
        self.tv_text = tk.Text(self.tv_tab, height=10, width=80)
        self.tv_text.pack(padx=10, pady=10, fill='both', expand=True)
        self.tv_text.insert('1.0', 'No TV show data loaded yet.')

        # Scrollbar
        self.tv_scroll = ttk.Scrollbar(self.tv_tab, orient='vertical', command=self.tv_text.yview)
        self.tv_scroll.pack(side='right', fill='y')
        self.tv_text['yscrollcommand'] = self.tv_scroll.set

    def setup_book_tab(self):
        self.book_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.book_tab, text='Books')

        # Text widget for displaying books and statistics
        self.book_text = tk.Text(self.book_tab, height=10, width=80)
        self.book_text.pack(padx=10, pady=10, fill='both', expand=True)
        self.book_text.insert('1.0', 'No book data loaded yet.')

        # Scrollbar
        self.book_scroll = ttk.Scrollbar(self.book_tab, orient='vertical', command=self.book_text.yview)
        self.book_scroll.pack(side='right', fill='y')
        self.book_text['yscrollcommand'] = self.book_scroll.set

    def setup_movie_tv_search_tab(self):
        self.movie_tv_search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.movie_tv_search_tab, text='Search Movies/TV Shows')

        # Frame for Movie/TV Show search controls
        search_frame = ttk.Frame(self.movie_tv_search_tab)
        search_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Dropdown menu for selecting either a Movie or TV Show
        self.movie_tv_type_var = tk.StringVar()
        self.movie_tv_type_combo = ttk.Combobox(search_frame, textvariable=self.movie_tv_type_var, state='readonly')
        self.movie_tv_type_combo['values'] = ('Movie', 'TV Show')
        self.movie_tv_type_combo.current(0)
        self.movie_tv_type_combo.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        ttk.Label(search_frame, text="Type:").grid(row=0, column=0, sticky='e', padx=5, pady=5)

        # Entry widgets for search criteria (Title, Director, Actor, Genre)
        self.entries = {}
        labels = ['Title', 'Director', 'Actor', 'Genre']
        for i, label in enumerate(labels):
            ttk.Label(search_frame, text=f"{label}:").grid(row=i + 1, column=0, sticky='e', padx=5, pady=5)
            entry = ttk.Entry(search_frame, width=50)
            entry.grid(row=i + 1, column=1, sticky='ew', padx=5, pady=5)
            self.entries[label.lower()] = entry

        # Search button for Movies/TV Shows
        self.movie_tv_search_button = ttk.Button(search_frame, text="Search", command=self.perform_movie_tv_search)
        self.movie_tv_search_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        # Text widget for displaying search results
        self.movie_tv_search_results_text = tk.Text(self.movie_tv_search_tab, height=20, width=80)
        self.movie_tv_search_results_text.pack(padx=10, pady=10, fill='both', expand=True)
        self.movie_tv_search_results_scroll = ttk.Scrollbar(self.movie_tv_search_tab, orient='vertical', command=self.movie_tv_search_results_text.yview)
        self.movie_tv_search_results_scroll.pack(side='right', fill='y')
        self.movie_tv_search_results_text['yscrollcommand'] = self.movie_tv_search_results_scroll.set

    def setup_book_search_tab(self):
        self.book_search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.book_search_tab, text='Search Books')

        # Frame for Book search controls
        search_frame = ttk.Frame(self.book_search_tab)
        search_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Setup for Title, Author, Publisher
        labels = ['Title', 'Author', 'Publisher']
        self.book_entries = {}
        for i, label in enumerate(labels):
            ttk.Label(search_frame, text=f"{label}:").grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(search_frame, width=50)
            entry.grid(row=i, column=1, sticky='ew', padx=5, pady=5)
            self.book_entries[label.lower()] = entry

        # Search button
        search_button = ttk.Button(search_frame, text="Search Books", command=self.perform_book_search)
        search_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Text widget for displaying search results
        self.book_search_results_text = tk.Text(self.book_search_tab, height=20, width=80)
        self.book_search_results_text.pack(padx=10, pady=10, fill='both', expand=True)
        self.book_search_results_scroll = ttk.Scrollbar(self.book_search_tab, orient='vertical', command=self.book_search_results_text.yview)
        self.book_search_results_scroll.pack(side='right', fill='y')
        self.book_search_results_text['yscrollcommand'] = self.book_search_results_scroll.set

    def setup_recommendation_tab(self):
        self.recommendation_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.recommendation_tab, text='Recommendations')

        # Frame for recommendation controls
        self.recommendation_frame = ttk.Frame(self.recommendation_tab)
        self.recommendation_frame.pack(padx=10, pady=10, fill='x', expand=False)

        # Drop-down menu for selecting media type
        self.recommendation_type_var = tk.StringVar()
        self.recommendation_type_combo = ttk.Combobox(self.recommendation_frame, textvariable=self.recommendation_type_var, state='readonly')
        self.recommendation_type_combo['values'] = ('Movie', 'TV Show', 'Book')
        self.recommendation_type_combo.current(0)
        self.recommendation_type_combo.pack(side='left', padx=10, pady=10)

        # Entry widget for Title
        self.recommendation_title_label = ttk.Label(self.recommendation_frame, text="Title:")
        self.recommendation_title_label.pack(side='left', padx=5, pady=10)
        self.recommendation_title_entry = ttk.Entry(self.recommendation_frame)
        self.recommendation_title_entry.pack(side='left', fill='x', expand=True, padx=5, pady=10)

        # Button to trigger recommendations
        self.recommendation_button = ttk.Button(self.recommendation_frame, text="Get Recommendations", command=self.perform_recommendations)
        self.recommendation_button.pack(side='right', padx=10, pady=10)

        # Text widget for displaying recommendation results
        self.recommendation_results_text = tk.Text(self.recommendation_tab, height=20, width=80)
        self.recommendation_results_text.pack(padx=10, pady=10, fill='both', expand=True)
        self.recommendation_results_text.insert('1.0', 'Enter a title and select a media type to get recommendations.')

        # Scrollbar for recommendation results
        self.recommendation_scroll = ttk.Scrollbar(self.recommendation_tab, orient='vertical', command=self.recommendation_results_text.yview)
        self.recommendation_scroll.pack(side='right', fill='y')
        self.recommendation_results_text['yscrollcommand'] = self.recommendation_scroll.set

    def setup_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill='x', expand=False)

        load_shows_button = tk.Button(button_frame, text="Load Shows", command=self.load_shows)
        load_shows_button.pack(side='left', padx=10, pady=10)

        load_books_button = tk.Button(button_frame, text="Load Books", command=self.load_books)
        load_books_button.pack(side='left', padx=10, pady=10)

        load_associations_button = tk.Button(button_frame, text="Load Associations", command=self.load_associations)
        load_associations_button.pack(side='left', padx=10, pady=10)

        # Button to show credits
        credit_button = tk.Button(button_frame, text="Credits", command=self.creditInfoBox)
        credit_button.pack(side='left', padx=10, pady=10)

        quit_button = tk.Button(button_frame, text="Quit", command=self.root.quit)
        quit_button.pack(side='right', padx=10, pady=10)

    def creditInfoBox(self):
        credit_message = "Project completed by:\n- Alice\n- Bob\n- Charlie\n\nCompleted on: April 30, 2024"
        messagebox.showinfo("Project Credits", credit_message)

    def load_shows(self):
        self.recommender.load_shows()
        movies_text = self.recommender.get_movie_list()
        tv_text = self.recommender.get_tv_list()
        self.movie_text.delete('1.0', tk.END)
        self.movie_text.insert('1.0', movies_text)
        self.tv_text.delete('1.0', tk.END)
        self.tv_text.insert('1.0', tv_text)

    def load_books(self):
        self.recommender.load_books()
        books_text = self.recommender.get_book_list()
        self.book_text.delete('1.0', tk.END)
        self.book_text.insert('1.0', books_text)

    def load_associations(self):
        self.recommender.load_associations()

    def perform_movie_tv_search(self):
        show_type = self.movie_tv_type_var.get()  # Assuming you have a ComboBox or similar for this
        title = self.entries['title'].get()
        director = self.entries['director'].get()
        actor = self.entries['actor'].get()
        genre = self.entries['genre'].get()

        results, error = self.recommender.search_tv_movies(show_type, title, director, actor, genre)
        if error:
            messagebox.showerror("Search Error", error)
            self.movie_tv_search_results_text.delete('1.0', tk.END)
            self.movie_tv_search_results_text.insert('1.0', "No Results")
        else:
            self.movie_tv_search_results_text.delete('1.0', tk.END)
            self.movie_tv_search_results_text.insert('1.0', results if results else "No Results")
            
    def perform_book_search(self):
        title = self.book_entries['title'].get()
        author = self.book_entries['author'].get()
        publisher = self.book_entries['publisher'].get()
        results, error = self.recommender.search_books(title, author, publisher)
        if error:
            messagebox.showerror("Search Error", error)
            self.book_search_results_text.delete('1.0', tk.END)
            self.book_search_results_text.insert('1.0', "No Results")
        else:
            self.book_search_results_text.delete('1.0', tk.END)
            self.book_search_results_text.insert('1.0', results if results else "No Results")

    def perform_recommendations(self):
        media_type = self.recommendation_type_var.get()
        title = self.recommendation_title_entry.get()
        results = self.recommender.get_recommendations(media_type, title)
        self.recommendation_results_text.delete('1.0', tk.END)
        self.recommendation_results_text.insert('1.0', results)

if __name__ == "__main__":
    app = RecommenderGUI()
