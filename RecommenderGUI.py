# Author: Dingxin Hu /Ruiyang HU
# Date: 2024-05-04
# Description: Various parts of the GUI are set up
# First set up the main application window,
# create a widget with multiple tabs for different functions, and set interactive buttons for the user;
# Create the movie TAB, one area for the title and market, one area for the movie details,
# and the TV and book tabs are created according to the same criteria;
# Set Search movies and TV TAB, Search books TAB, Recommend TAB;
# And set the button for each function, load and render each kind of title and statistics.
# Finally, a rating area is set up and two pie charts are presented
# to show the proportion of the number of movies and TV shows of different ratings.


import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from Recommender import Recommender
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RecommenderGUI:
    """
    Initializes the RecommenderGUI class, setting up the main application window,
    creating a notebook widget with multiple tabs for different functionalities,
    and setting up buttons for user interactions.
    """
    def __init__(self):
        self.recommender = Recommender() # Create an instance of the Recommender object to manage recommendation logic

        # Initialize the main window of the application
        self.root = tk.Tk()
        self.root.title("Media Recommender System")
        self.root.geometry("1200x800")

        # Create a Notebook widget that will hold different tabs for functionality
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True) # Make the notebook expandable and fill the space

        # Tabs for different functionalities
        self.setup_movie_tab()
        self.setup_tv_tab()
        self.setup_book_tab()
        self.setup_movie_tv_search_tab()
        self.setup_book_search_tab()
        self.setup_recommendation_tab()
        self.setup_ratings_tab()

        # Setup buttons for loading data and quitting the application
        self.setup_buttons()

        self.root.mainloop()

    def setup_movie_tab(self):
        """
        Sets up the 'Movies' tab in the GUI's notebook. This tab contains two main areas:
        one for displaying movie titles and runtimes, and another for displaying detailed
        statistics about the movies.
        """
        # Add the movie tab to the notebook widget in the main GUI window
        self.movie_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.movie_tab, text='Movies')

        # Create frames for organizing content within the 'Movies' tab
        titles_frame = ttk.Frame(self.movie_tab)
        stats_frame = ttk.Frame(self.movie_tab)
        titles_frame.pack(fill='both', expand=True)
        stats_frame.pack(fill='both', expand=True)

        # Setup the text widget for displaying movie titles and runtimes
        self.movie_titles_text = tk.Text(titles_frame, height=10, width=80)
        self.movie_titles_text.pack(padx=10, pady=5, fill='both', expand=True)
        self.movie_titles_text.insert('1.0', 'No movie data loaded yet.')
        # Add a scrollbar for the movie titles text widget
        movie_titles_scroll = ttk.Scrollbar(titles_frame, orient='vertical', command=self.movie_titles_text.yview)
        movie_titles_scroll.pack(side='right', fill='y')
        self.movie_titles_text['yscrollcommand'] = movie_titles_scroll.set

        # Setup the text widget for displaying detailed movie statistics
        self.movie_stats_text = tk.Text(stats_frame, height=10, width=80)
        self.movie_stats_text.pack(padx=10, pady=5, fill='both', expand=True)
        # Add a scrollbar for the movie statistics text widget
        movie_stats_scroll = ttk.Scrollbar(stats_frame, orient='vertical', command=self.movie_stats_text.yview)
        movie_stats_scroll.pack(side='right', fill='y')
        self.movie_stats_text['yscrollcommand'] = movie_stats_scroll.set

    def setup_tv_tab(self):
        """
        Sets up the 'TV Shows' tab in the GUI's notebook. This tab is divided into two sections:
        one for displaying titles and seasons of TV shows, and another for displaying detailed statistics.
        """
        # Add the TV tab to the notebook widget in the main GUI window
        self.tv_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.tv_tab, text='TV Shows')

        # Create two frames within the TV tab for better organization of content
        titles_frame = ttk.Frame(self.tv_tab) # Frame for TV show titles and seasons
        stats_frame = ttk.Frame(self.tv_tab)  # Frame for TV show statistics
        titles_frame.pack(fill='both', expand=True)
        stats_frame.pack(fill='both', expand=True)

        # Set up a Text widget in the titles frame for displaying TV show titles and seasons
        self.tv_titles_text = tk.Text(titles_frame, height=10, width=80)
        self.tv_titles_text.pack(padx=10, pady=5, fill='both', expand=True)
        self.tv_titles_text.insert('1.0', 'No TV show data loaded yet.') # Default text before data is loaded
        tv_titles_scroll = ttk.Scrollbar(titles_frame, orient='vertical', command=self.tv_titles_text.yview)
        tv_titles_scroll.pack(side='right', fill='y')
        self.tv_titles_text['yscrollcommand'] = tv_titles_scroll.set

        # Set up another Text widget in the stats frame for displaying detailed statistics of TV shows
        self.tv_stats_text = tk.Text(stats_frame, height=10, width=80)
        self.tv_stats_text.pack(padx=10, pady=5, fill='both', expand=True)
        # Add a vertical scrollbar to the stats Text widget
        tv_stats_scroll = ttk.Scrollbar(stats_frame, orient='vertical', command=self.tv_stats_text.yview)
        tv_stats_scroll.pack(side='right', fill='y')
        self.tv_stats_text['yscrollcommand'] = tv_stats_scroll.set

    def setup_book_tab(self):
        """
        Configures the 'Books' tab in the application's notebook. This tab is designed to display
        book titles and authors, as well as various statistics about the books.
        """
        self.book_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.book_tab, text='Books')

        # Create frames for titles and statistics
        titles_frame = ttk.Frame(self.book_tab)
        stats_frame = ttk.Frame(self.book_tab)
        titles_frame.pack(fill='both', expand=True)
        stats_frame.pack(fill='both', expand=True)

        # Text widget for displaying book titles and authors
        self.book_titles_text = tk.Text(titles_frame, height=10, width=80)
        self.book_titles_text.pack(padx=10, pady=5, fill='both', expand=True)
        self.book_titles_text.insert('1.0', 'No book data loaded yet.')
        book_titles_scroll = ttk.Scrollbar(titles_frame, orient='vertical', command=self.book_titles_text.yview)
        book_titles_scroll.pack(side='right', fill='y')
        self.book_titles_text['yscrollcommand'] = book_titles_scroll.set

        # Text widget for displaying book statistics
        self.book_stats_text = tk.Text(stats_frame, height=10, width=80)
        self.book_stats_text.pack(padx=10, pady=5, fill='both', expand=True)
        book_stats_scroll = ttk.Scrollbar(stats_frame, orient='vertical', command=self.book_stats_text.yview)
        book_stats_scroll.pack(side='right', fill='y')
        self.book_stats_text['yscrollcommand'] = book_stats_scroll.set

    def display_movie_stats(self):
        """
        Retrieves and displays statistical data for movies in the movie stats text widget.
        includes ratings distribution, average duration, and other relevant statistics.
        """
        stats = self.recommender.get_movie_stats()
        # Format the statistics into a readable string
        stats_text = (
            "Ratings:\n" + "\n".join(f"{k}: {v}" for k, v in stats['Ratings Distribution'].items()) + "\n"
            f"\nAverage Movie Duration: {stats['Average Duration']}\n"
            f"Most Prolific Director: {stats['Most Common Director'][0]} ({stats['Most Common Director'][1]} times)\n"
            f"Most Prolific Actor: {stats['Most Common Actor'][0]} ({stats['Most Common Actor'][1]} times)\n"
            f"Most Frequent Genre: {stats['Most Common Genre'][0]} ({stats['Most Common Genre'][1]} times)"
        )
        self.movie_stats_text.delete('1.0', tk.END)
        self.movie_stats_text.insert('1.0', stats_text)


    def display_tv_stats(self):
        """
        Retrieves and displays statistical data for TV shows in the TV stats text widget.
        includes ratings distribution, average number of seasons, and other relevant statistics.
        """
        stats = self.recommender.get_tv_stats()
        # Format the statistics into a readable string
        stats_text = (
            "Ratings:\n" + "\n".join(f"{k}: {v}" for k, v in stats['Ratings Distribution'].items()) + "\n"
            f"\nAverage Number of Seasons: {stats['Average Seasons']} seasons\n"
            f"Most Prolific Actor: {stats['Most Common Actor'][0]} ({stats['Most Common Actor'][1]} times)\n"
            f"Most Frequent Genre: {stats['Most Common Genre'][0]} ({stats['Most Common Genre'][1]} times)"
        )
        # Clear the current contents of the TV stats text widget and insert the new stats
        self.tv_stats_text.delete('1.0', tk.END)
        self.tv_stats_text.insert('1.0', stats_text)


    def display_book_stats(self):
        """
        Retrieves and displays statistical data for books in the book stats text widget.
        includes average page count, most common author, and most common publisher.
        """
        stats = self.recommender.get_book_stats()
        stats_text = (
            f"Average Page Count: {stats['Average Page Count']}\n"
            f"Most Common Author: {stats['Most Common Author'][0]} ({stats['Most Common Author'][1]} times)\n"
            f"Most Common Publisher: {stats['Most Common Publisher'][0]} ({stats['Most Common Publisher'][1]} times)"
        )
        self.book_stats_text.delete('1.0', tk.END)
        self.book_stats_text.insert('1.0', stats_text)

    def setup_movie_tv_search_tab(self):
        """
        Sets up the 'Search Movies/TV Shows' tab in the application's notebook. This tab allows
        the user to search for movies or TV shows based on specific criteria such as title,
        director, actor, and genre.
        """
        # Create a new tab in the notebook specifically for movie and TV show search functionalities
        self.movie_tv_search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.movie_tv_search_tab, text='Search Movies/TV Shows')

        # Set up a frame within the tab for housing the search controls
        search_frame = ttk.Frame(self.movie_tv_search_tab)
        search_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Dropdown menu to select either a movie or a TV show for the search
        self.movie_tv_type_var = tk.StringVar()
        self.movie_tv_type_combo = ttk.Combobox(search_frame, textvariable=self.movie_tv_type_var, state='readonly')
        self.movie_tv_type_combo['values'] = ('Movie', 'TV Show')
        self.movie_tv_type_combo.current(0) # Default to 'Movie'
        self.movie_tv_type_combo.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
        # Label for the dropdown menu
        ttk.Label(search_frame, text="Type:").grid(row=0, column=0, sticky='e', padx=5, pady=5)

        # Create entry widgets for search criteria (title, director, actor, genre)
        self.entries = {}
        labels = ['Title', 'Director', 'Actor', 'Genre']
        for i, label in enumerate(labels):
            ttk.Label(search_frame, text=f"{label}:").grid(row=i + 1, column=0, sticky='e', padx=5, pady=5)
            entry = ttk.Entry(search_frame, width=50)
            entry.grid(row=i + 1, column=1, sticky='ew', padx=5, pady=5)
            # Store entries in a dictionary for later access
            self.entries[label.lower()] = entry

        # Search button for Movies/TV Shows
        self.movie_tv_search_button = ttk.Button(search_frame, text="Search", command=self.perform_movie_tv_search)
        self.movie_tv_search_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        # Text widget for displaying search results
        self.movie_tv_search_results_text = tk.Text(self.movie_tv_search_tab, height=20, width=80)
        self.movie_tv_search_results_text.pack(padx=10, pady=10, fill='both', expand=True)
        # Scrollbar for the text widget
        self.movie_tv_search_results_scroll = ttk.Scrollbar(self.movie_tv_search_tab, orient='vertical', command=self.movie_tv_search_results_text.yview)
        self.movie_tv_search_results_scroll.pack(side='right', fill='y')
        self.movie_tv_search_results_text['yscrollcommand'] = self.movie_tv_search_results_scroll.set

    def setup_book_search_tab(self):
        """
        Sets up the 'Search Books' tab in the application's notebook. allows
        the user to search for books based on title, author, or publisher.
        """
        self.book_search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.book_search_tab, text='Search Books')

        # Frame for Book search controls
        search_frame = ttk.Frame(self.book_search_tab)
        search_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Define labels for the entry widgets that will collect search criteria
        labels = ['Title', 'Author', 'Publisher']
        self.book_entries = {}

        # Create and grid labels and entry widgets for each search criterion
        for i, label in enumerate(labels):
            ttk.Label(search_frame, text=f"{label}:").grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(search_frame, width=50)
            entry.grid(row=i, column=1, sticky='ew', padx=5, pady=5)
            # Store entry widgets in a dictionary for easy access
            self.book_entries[label.lower()] = entry

        # Create a search button that will trigger the search operation
        search_button = ttk.Button(search_frame, text="Search Books", command=self.perform_book_search)
        search_button.grid(row=len(labels), column=0, columnspan=2, pady=10) # Span across both columns

        # Text widget for displaying search results
        self.book_search_results_text = tk.Text(self.book_search_tab, height=20, width=80)
        self.book_search_results_text.pack(padx=10, pady=10, fill='both', expand=True)
        self.book_search_results_scroll = ttk.Scrollbar(self.book_search_tab, orient='vertical', command=self.book_search_results_text.yview)
        self.book_search_results_scroll.pack(side='right', fill='y')
        self.book_search_results_text['yscrollcommand'] = self.book_search_results_scroll.set

    def setup_recommendation_tab(self):
        """
        Sets up the 'Recommendations' tab in the application's notebook. allows
        the user to search for media recommendations based on a given title.
        """
        # Create the tab within the notebook for recommendations
        self.recommendation_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.recommendation_tab, text='Recommendations')

        # Frame for holding the controls like dropdowns, entry fields, and buttons
        self.recommendation_frame = ttk.Frame(self.recommendation_tab)
        self.recommendation_frame.pack(padx=10, pady=10, fill='x', expand=False) # Only expand horizontally

        # Dropdown menu for selecting the type of media: Movie, TV Show, or Book
        self.recommendation_type_var = tk.StringVar()
        self.recommendation_type_combo = ttk.Combobox(self.recommendation_frame, textvariable=self.recommendation_type_var, state='readonly')
        self.recommendation_type_combo['values'] = ('Movie', 'TV Show', 'Book')
        # Set default selection to the first entry
        self.recommendation_type_combo.current(0)
        self.recommendation_type_combo.pack(side='left', padx=10, pady=10)

        # Label and entry widget for inputting the title to search
        self.recommendation_title_label = ttk.Label(self.recommendation_frame, text="Title:")
        self.recommendation_title_label.pack(side='left', padx=5, pady=10)
        self.recommendation_title_entry = ttk.Entry(self.recommendation_frame)
        self.recommendation_title_entry.pack(side='left', fill='x', expand=True, padx=5, pady=10)

        # Button to trigger the search for recommendations
        self.recommendation_button = ttk.Button(self.recommendation_frame, text="Get Recommendations", command=self.perform_recommendations)
        self.recommendation_button.pack(side='right', padx=10, pady=10)

        # Text widget for displaying the results of the recommendations
        self.recommendation_results_text = tk.Text(self.recommendation_tab, height=20, width=80)
        self.recommendation_results_text.pack(padx=10, pady=10, fill='both', expand=True)
        self.recommendation_results_text.insert('1.0', 'Enter a title and select a media type to get recommendations.')

        # Scrollbar for recommendation results
        self.recommendation_scroll = ttk.Scrollbar(self.recommendation_tab, orient='vertical', command=self.recommendation_results_text.yview)
        self.recommendation_scroll.pack(side='right', fill='y')
        self.recommendation_results_text['yscrollcommand'] = self.recommendation_scroll.set


    def setup_buttons(self):
        """
        Sets up the buttons for loading data and managing the application in the main GUI frame.
        Initializes and places buttons in a frame toLoad show, book, and association data from respective sources；
        Display credits information；Quit the application.
        """
        # Create a frame to hold all buttons below the main content area
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill='x', expand=False) # Horizontal packing with no vertical expansion

        # Button to load TV show data
        load_shows_button = tk.Button(button_frame, text="Load Shows", command=self.load_shows)
        load_shows_button.pack(side='left', padx=10, pady=10) # Position to the left with padding
        # Button to load book data
        load_books_button = tk.Button(button_frame, text="Load Books", command=self.load_books)
        load_books_button.pack(side='left', padx=10, pady=10) # Adjacent to the show load button
        # Button to load association data
        load_associations_button = tk.Button(button_frame, text="Load Associations", command=self.load_associations)
        load_associations_button.pack(side='left', padx=10, pady=10) # Next to the book load button

        # Button to show credits
        credit_button = tk.Button(button_frame, text="Credits", command=self.creditInfoBox)
        credit_button.pack(side='left', padx=10, pady=10) # Placed next to the association load button
        # Button to quit the application
        quit_button = tk.Button(button_frame, text="Quit", command=self.root.quit)
        quit_button.pack(side='right', padx=10, pady=10) # Positioned to the far right for clarity and accessibility

    def creditInfoBox(self):
        """Displays project credit information in a dialog box."""
        credit_message = "Project completed by:\n- Dingxin Hu\n- Ruiyang Hu\n\nCompleted on: 2024.5.3"
        messagebox.showinfo("Project Credits", credit_message)

    def load_shows(self):
        """Loads and displays show data including movies and TV shows, updating the statistics in the GUI."""
        self.recommender.load_shows()
        movies_text = self.recommender.get_movie_list()
        tv_text = self.recommender.get_tv_list()

        # Clear existing content in text widgets and insert new data
        self.movie_titles_text.delete('1.0', tk.END)
        self.movie_titles_text.insert('1.0', movies_text)
        self.tv_titles_text.delete('1.0', tk.END)
        self.tv_titles_text.insert('1.0', tv_text)
        # Display updated stats for movies and TV shows
        self.display_movie_stats()
        self.display_tv_stats()

    def load_books(self):
        """Loads and displays book data, updating the book titles and statistics in the GUI."""
        self.recommender.load_books()
        books_text = self.recommender.get_book_list()
        # Update text widget with new book titles or default message if none
        self.book_titles_text.delete('1.0', tk.END)
        self.book_titles_text.insert('1.0', books_text)
        self.display_book_stats()  # Update statistics display for books

    def load_associations(self):
        self.recommender.load_associations()

    def perform_movie_tv_search(self):
        """
        Searches for movies or TV shows using input from GUI components and displays the results in the GUI.
        Alerts user if an error occurs or no data matches the search criteria.
        """
        # Retrieve values from the GUI's ComboBox and Entry widgets
        show_type = self.movie_tv_type_var.get()
        title = self.entries['title'].get()
        director = self.entries['director'].get()
        actor = self.entries['actor'].get()
        genre = self.entries['genre'].get()

        # Perform the search operation using the Recommender class
        results, error = self.recommender.search_tv_movies(show_type, title, director, actor, genre)
        # Update the GUI based on search results
        if error:
            messagebox.showerror("Search Error", error) # Display any errors encountered during the search
            self.movie_tv_search_results_text.delete('1.0', tk.END) # Clear existing content in the results display area
            self.movie_tv_search_results_text.insert('1.0', "No Results")
        else:
            self.movie_tv_search_results_text.delete('1.0', tk.END)
            self.movie_tv_search_results_text.insert('1.0', results if results else "No Results")

    def perform_book_search(self):
        """
        Executes a search for books based on the user input from GUI components and displays the results.
        Alerts the user if an error occurs or no data matches the search criteria.
        """
        # Retrieve input values from GUI Entry widgets for book search
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
        """
        Generates media recommendations based on the user-selected media type and title. Displays results in GUI.
        """
        media_type = self.recommendation_type_var.get()
        title = self.recommendation_title_entry.get()
        # Obtain recommendations using the Recommender class
        results = self.recommender.get_recommendations(media_type, title)
        # Clear previous results
        self.recommendation_results_text.delete('1.0', tk.END)
        self.recommendation_results_text.insert('1.0', results)


    def generate_pie_charts(self):
        """
        Generates pie charts for both movie and TV show ratings,
        based on data retrieved from the Recommender object, and
        displays them in the designated frames within the GUI.
            """
        # Retrieve movie and TV show statistics from the Recommender object
        movie_stats = self.recommender.get_movie_stats()
        tv_stats = self.recommender.get_tv_stats()

        # Process ratings data for movies and TV shows for pie chart display
        movie_ratings = {k: float(v.rstrip('%')) for k, v in movie_stats['Ratings Distribution'].items()}
        tv_show_ratings = {k: float(v.rstrip('%')) for k, v in tv_stats['Ratings Distribution'].items()}

        # Create pie charts for movie ratings and TV show ratings
        self.create_pie_chart(movie_ratings, self.frame_movies, "Movie Ratings")
        self.create_pie_chart(tv_show_ratings, self.frame_tv_shows, "TV Show Ratings")


    def setup_ratings_tab(self):
        """
        Sets up the 'Ratings' tab in the GUI with necessary widgets
        including frames for movies and TV shows and a button to generate pie charts.
        """
        # Setup the Ratings tab in the notebook
        ratings_tab = ttk.Frame(self.notebook)
        self.notebook.add(ratings_tab, text='Ratings')

        # Frame for buttons within the Ratings tab
        button_frame = ttk.Frame(ratings_tab)
        button_frame.pack(side='top', fill='x', padx=10, pady=10)

        # Button to trigger the generation of pie charts
        generate_button = ttk.Button(button_frame, text="Generate Charts", command=self.generate_pie_charts)
        generate_button.pack(side='left')

        self.frame_movies = tk.Frame(ratings_tab)
        self.frame_tv_shows = tk.Frame(ratings_tab)
        self.frame_movies.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame_tv_shows.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def create_pie_chart(self, data, frame, title):
        """
        Creates and displays a pie chart within the provided frame using matplotlib,
        based on the data passed which includes the ratings for either movies or TV shows.
        """
        # Create a pie chart using matplotlib and display it in the provided frame
        fig, ax = plt.subplots()
        # Convert percentage data into float and format labels with percentages
        labels = [f"{k} - {v:.2f}%" for k, v in data.items()]

        # Plot the pie chart with autopct to display the percentage value on chart
        ax.pie(data.values(), labels=labels, autopct='%1.2f%%', startangle=90)
        ax.set_title(title)
        ax.axis('equal')  # Ensure that pie is drawn as a circle.
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Main function to run the GUI
if __name__ == "__main__":
    app = RecommenderGUI()
