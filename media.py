__author__ = 'Praveen'

import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """ Method to open a popup window and play the youtube video """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def __repr__(self):
        return ("Title = %s, poster image URL is : %s") %(self.title, self.poster_image_url)

    def __str__(self):
        return ("Title = %s, poster image URL is : %s") %(self.title, self.poster_image_url)