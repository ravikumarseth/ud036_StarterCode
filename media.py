import webbrowser


# This class is data structure to store movies data.
# It contains movie title, one line movie description, poster image url and
# movie trailer's youtube url.
class Movies:

    """This class stores movie related information."""

    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image_url,
        trailer_youtube_url,
        ):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
