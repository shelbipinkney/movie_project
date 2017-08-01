import fresh_tomatoes
import media
#stores details of movies and displays them on a website




the_dark_night = media.Movie("The Dark Night","A classic Batman movie where the Joker takes control of Gotham City and challenges Batman.",
                             "https://fanart.tv/fanart/movies/155/movieposter/the-dark-knight-5225e1dfa5059.jpg",
                             "https://www.youtube.com/watch?v=EXeTwQWrcwY")


#Incorporating relational database connection -- using CRUD to manipulate tables, records, attributes, and fields in the database
# INSERT value of "Viewed" Atrribute in Movie Name table.
#Default value is "No" but changes to "Yes" after trailer is watched through the end.
#UPDATE database at the end of the script

pulp_fiction = media.Movie("Pulp Fiction","The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")


training_day = media.Movie("Training Day","A crooked cop gets exploited when he tries to take advantage of a rookie cop.",
                           "https://www.cinematerial.com/media/posters/md/ue/uezszcui.jpg?v=1456623237", 
                           "https://www.youtube.com/watch?v=DXPJqRtkDP0")

step_brothers = media.Movie("Step Brothers","A hilarious rendition of when two guys move in together when their parent remarry.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d9/StepbrothersMP08.jpg",
                            "https://www.youtube.com/watch?v=8QKE96wZTkw")


wedding_crashers = media.Movie("Wedding Crashers","Two close friends continue their hobby of crashing weddings and run into an unexpected plot twist that makes them question their morality.",
                               "https://fontmeme.com/images/wedding_crashers_POSTER.jpg",
                               "https://www.youtube.com/watch?v=KX1C5OUT6VQ")


remember_the_titans = media.Movie("Remember the Titans","The true story of a newly appointed African-American coach and his high school team on their first season as a racially integrated unit",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BYThkMzgxNjEtMzFiOC00MTI0LWI5MDItNDVmYjA4NzY5MDQ2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR0,0,182,268_AL_.jpg",
                                 "https://www.youtube.com/watch?v=nPhu9XsRl4M")



movies = [the_dark_night, pulp_fiction, training_day,step_brothers, wedding_crashers,remember_the_titans]
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__module__)
