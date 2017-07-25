import movie
import fresh_tomatoes


# This "console file" will create movie instances from the
# movie class to then insert it into the fresh_tomatoes
# code to view on the website.
toy_story = movie.Movie("Toy Story",
                        "A story about toys coming to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/" +
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio"
                        )

mean_girls = movie.Movie("Mean Girls",
                         "A sheltered girl moves into public school only to " +
                         "mix up with the wrong crowd",
                         "https://upload.wikimedia.org/wikipedia/en/8/87/" +
                         "MeanGirlsSoundtrack.jpg",
                         "https://www.youtube.com/watch?v=KAOmTMCtGkI"
                         )

rushmore = movie.Movie("Rushmore",
                       "Private school kid falls in love with teacher but" +
                       " ends up with student",
                       "https://images-na.ssl-images-amazon.com/images/I/" +
                       "51uIGT-c8JL.jpg",
                       "https://www.youtube.com/watch?v=GxCNDpvGyss"
                       )

# Following URL may not meet PEP8 standards, but I kept it on the same line
# because it is a url.
mysterious_skin = movie.Movie("Mysterious Skin",
                              "A boy from the country struggles with past" +
                              " and becomes gay prostitute in NY",
                              "https://images-na.ssl-images-amazon.com/" +
                              "images/M/MV5BMTgxMjQ4NzE5OF5BMl5BanBnXkF" +
                              "tZTcwNzkwOTkyMQ@@._V1_UX182_CR0,0,182,268" +
                              "_AL_.jpg",
                              "https://www.youtube.com/watch?v=5Lp5v4oQZRw"
                              )

forks_over_knives = movie.Movie("Forks Over Knives",
                                "Documentary that advocates a whole" +
                                " plant-food based diet as basis of medicine.",
                                "https://s.movie.as/images/p/150/" +
                                "37173_m1294539380.jpg",
                                "https://www.youtube.com/watch?v=DZb-35oV_7E"
                                )

the_shining = movie.Movie("The Shining",
                          "Based on Stephen King's novel about a family" +
                          " on vacation that turns awry",
                          "http://static.rogerebert.com/uploads/movie/" +
                          "movie_poster/the-shining-1980/large_" +
                          "zc5y5OwKSV9MDXpfWxwrOjyRHsq.jpg",
                          "https://www.youtube.com/watch?v=5Cb3ik6zP2I"
                          )

# I have to create a list because the open_movies_page method only
# takes in a list
movie_list = [toy_story, mean_girls, rushmore, mysterious_skin,
              forks_over_knives, the_shining]
fresh_tomatoes.open_movies_page(movie_list)
