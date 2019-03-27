import webbrowser
'''
__doc__
__name__
__module__
'''
class Movie():  % class
    '''
    This class provides a way to store movie related information
    '''
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']  # class variables
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): # constructor
        self.title = movie_title  # instance variable
        self.storyline = movie_storyline  # instance variable
        self.poster_image_url = poster_image # instance variable
        self.trailer_youtube_url = trailer_youtube # instance variable

    def show_trailer(self):  # instance method
        webbrowser.open(self.trailer_youtube_url)