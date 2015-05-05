__author__ = 'Praveen'

import media
import fresh_tomatoes

# Create the meta data for the movie toy_story
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)

# Create the meta data for the movie Avatar
avatar = media.Movie("Avatar", "An adventure of a marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# Create the meta data for the movie Ratatouille
ratatouille = media.Movie("Ratatouille", "Story of a Rat who wanted to be a Chef",
                          "http://www.impawards.com/2007/posters/ratatouille.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

movies = [toy_story, avatar, ratatouille]
fresh_tomatoes.open_movies_page(movies)