import webbrowser as w

class Movie():
    """Provides a way to store movie information"""
    #constructor for the movie class
    def __init__(self, movie_title, movie_storyline, movie_image, movie_trailer):
        #These are initial variables created once information is passed
        #into the Movie() class.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer
    #This will show the movie trailer on the web browser.
    def show_trailer(self):
        w.open(self.trailer_url)
