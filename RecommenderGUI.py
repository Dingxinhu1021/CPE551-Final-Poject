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

