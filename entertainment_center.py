import media
import fresh_tomatoes

# Creating movie instances
big_lebowski = media.Movie("The Big Lebowski",
                           "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y")

shawshank = media.Movie("The Shawshank Redemption",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

godfather = media.Movie("The Godfather",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/The_Funny_Face_of_the_Godfather.jpg/220px-The_Funny_Face_of_the_Godfather.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

good_will_hunting = media.Movie("Good Will Hunting",
                                "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=QSMvyuEeIyw")

get_out = media.Movie("Get Out",
                      "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

old_school = media.Movie("Old School",
                         "https://upload.wikimedia.org/wikipedia/en/2/21/Old_s_poster.jpg",
                         "https://www.youtube.com/watch?v=ybNn__9pnms")

# List of movie instances
movies = [
    godfather, get_out, old_school, big_lebowski, shawshank,
    good_will_hunting
    ]

# Launching page with movies
fresh_tomatoes.open_movies_page(movies)
