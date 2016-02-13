import media
import fresh_tomatoes

ex_machina = media.Movie("Ex Machina",
                         "A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I.",
                         "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
                         "https://www.youtube.com/watch?v=EoQuVnKhxaM")

#print(toy_story.storyline)
star_wars_vii = media.Movie("The Force Awakens",
                           ("Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a ragtag group of heroes can stop them, along " 
                            "with the help of the Resistance."),
                            "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                            "https://www.youtube.com/watch?v=sGbxmsDFVnE")
#print(avatar.storyline)
#avatar.show_trailer()

mad_max = media.Movie("Mad Max: Fury Road",
                     ("A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, "
                      "and a drifter named Max."),
                      "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                      "https://www.youtube.com/watch?v=cdLl1GVjOrc")

southpaw = media.Movie("Southpaw",
                       "Boxer Billy Hope turns to trainer Tick Wills to help him get his life back on track after losing his wife in a tragic accident and his daughter to child protection services.",
                       "https://upload.wikimedia.org/wikipedia/en/8/89/Southpaw_poster.jpg",
                       "https://www.youtube.com/watch?v=Mh2ebPxhoLs")

the_revenant = media.Movie("The Revenant",
                           "A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team.",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")

steve_jobs = media.Movie("Steve Jobs",
                        ("Steve Jobs takes us behind the scenes of the digital revolution, to paint a portrait of the man at its epicenter. The story unfolds backstage at three iconic product "
                         "launches, ending in 1998 with the unveiling of the iMac."),
                         "https://upload.wikimedia.org/wikipedia/en/a/aa/SteveJobsposter.jpg",
                         "https://www.youtube.com/watch?v=ufMgQNCXy_M")

movies = [ex_machina, star_wars_vii, mad_max, southpaw, the_revenant, steve_jobs]

# Uses list of movie instances as input to generate an HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
