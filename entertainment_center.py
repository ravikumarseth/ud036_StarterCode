import media
import fresh_tomatoes

# Declaring 6 instances of movie class each containing movie title,
# one line movie description, poster image url and movie trailer's youtube url.

toy_story = media.Movies('Toy Story',
                         'A story of a boy and his toys that come to life.',
                         'http://www.impawards.com/1995/posters/toy_'
                         'story_ver1_xlg.jpg',
                         'https://www.youtube.com/watch?v=KYz2wyBy3kc'
                         )

avatar = media.Movies('Avatar',
                      'A marine on an alien planet.',
                      'http://www.impawards.com/2009/posters/avatar_xlg.jpg',
                      'https://www.youtube.com/watch?v=5PSNL1qE6VY')

school_of_rock = media.Movies('School of Rock',
                              'Using rock mucic to learn.',
                              'https://images-na.ssl-images-amazon.com/images'
                              '/M/MV5BMTM0OTgzMjg2MF5BMl5BanBnXkFtZTcwMDg5'
                              'MTUyMQ@@._V1_.jpg',
                              'https://www.youtube.com/watch?v=LqEszt5wG9I'
                              )

ratatouille = media.Movies('Ratatouille', 'A rat is a chef in Paris.',
                           'https://s-media-cache-ak0.pinimg.com/736x/66/f2'
                           '/f4/66f2f48e24762592f4e083c556e913cf.jpg',
                           'https://www.youtube.com/watch?v=ALUmKa_mpik'
                           )

midnight_in_paris = media.Movies('Midnight In Paris',
                                 'Going back in time to meet authors.',
                                 'https://images-na.ssl-images-amazon.com/'
                                 'images/I/61uuYEUFw4L._SY450_.jpg',
                                 'https://www.youtube.com/watch?v=FAfR8omt-CY'
                                 )

hunger_games = media.Movies('Hunger Games',
                            'A really real reality show.',
                            'http://www.impawards.com/2014/posters/hunger_games'
                            '_mockingjay__part_one_ver24_xlg.jpg',
                            'https://www.youtube.com/watch?v=3PkkHsuMrho'
                            )

# Adding all instances of movies class in a List.

movies = [
    toy_story,
    avatar,
    school_of_rock,
    ratatouille,
    midnight_in_paris,
    hunger_games,
    ]

# Passing list of movies to fresh_tomatoes.py and calling its method
# open_movies_page for creating new html file using the data provided in
# movies list and for opening that new html file.

fresh_tomatoes.open_movies_page(movies)
