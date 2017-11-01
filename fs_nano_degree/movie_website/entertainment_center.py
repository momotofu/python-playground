import media
import fresh_tomatoes

planet_earth = media.Movie("Planet Earth", "A visual journey covering the wonders of planet Earth",
        "https://i.pinimg.com/736x/98/2f/cc/982fcc3212d1dab93f99bee02725c9cc--planet-earth-documentary-bbc-planet-earth.jpg",
        "https://www.youtube.com/watch?v=tiVNk6_0GdY")

prince_of_egypt = media.Movie("Prince of Egypt",
        "An Egyptian prince learns of his identity as a Hebrew and his destiny to become the chosen deliverer of his people.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BOWNjMjgyNmMtNWMzZC00YjI4LWI1NmUtMTY0ZTA0ZDQ4Y2EwXkEyXkFqcGdeQXVyNTUyMzE4Mzg@._V1_.jpg",
        "https://www.youtube.com/watch?v=zmBDY-fSlIs")

natural_curiosities = media.Movie("Natural Curiosities",
        "David Attenborough presents a collection of his favourite natural curiosities found throughout the animal kingdom from armoured giants to crafty insects.",
        "https://image.tmdb.org/t/p/original/cd7eNiMyxHCRTdCYBTPAEQF7Ec3.jpg",
        "https://www.youtube.com/watch?v=hsHtu03G0e0")

patterns_of_evidence = media.Movie("Patterns of Evidence",
        "What is the validity of history found in the Bible? Is it fact or fiction? What does the hard evidence really have to say about the foundational story of the Old Testament: the Exodus...",
        "https://s-media-cache-ak0.pinimg.com/originals/8d/14/38/8d14381ea548684ba7fef6c218912afc.jpg",
        "https://www.youtube.com/watch?v=2assFIyLInE")

indie_game = media.Movie("Indie Game",
        "A documentary that follows the journeys of indie game developers as they create games and release those works, and themselves, to the world.",
        "http://www.indiegamethemovie.com/storage/post-images/2011-posts/nov-2011/POSTER_SD_PIXEL.jpg?__SQUARESPACE_CACHEVERSION=1322687529780",
        "https://www.youtube.com/watch?v=GhaT78i1x2M")

batman_begins = media.Movie("Batman Begins",
        "After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from the corruption that Scarecrow and the League of Shadows have cast upon it.",
        "https://s-media-cache-ak0.pinimg.com/originals/21/d6/39/21d6398a3369280670857c4021aef42b.jpg",
        "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

jago = media.Movie("Jago: A Life Underwater",
        "An award-winning documentary about Rohani, an 80-year-old hunter who dives on a single breath descending to great depths for several minutes. Set against the spectacular backdrop of the Togian Islands of Indonesia.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzExOTAxODc4OF5BMl5BanBnXkFtZTgwNTczMjE0NzE@._V1_SY1000_CR0,0,699,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=rVVI3Ta--No")

sound_of_music = media.Movie("Sound of Music",
        "A woman leaves an Austrian convent to become a governess to the children of a Naval officer widower.",
        "http://loyd-theater.com/movie-collect-1/20th/sound-of-music/sound-dvd.jpg",
        "https://www.youtube.com/watch?v=5fH2FOn1V5g")

the_grand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
        "The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka between the first and second World Wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.",
        "https://s-media-cache-ak0.pinimg.com/originals/48/08/cd/4808cde63ff708572be687970f979cfe.jpg",
        "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

the_matrix = media.Movie("The Matrix",
        "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "https://images-na.ssl-images-amazon.com/images/I/51EG732BV3L.jpg",
        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_karate_kid = media.Movie("The Karate Kid",
        "A martial arts master agrees to teach karate to a bullied teenager.",
        "http://thegalileo.co.za/wp-content/uploads/2015/09/a1r6Azn2WfeXAx9p2TKXOpOaGlx.jpg",
        "https://www.youtube.com/watch?v=n7JhKCQnEqQ")

the_last_samurai = media.Movie("The Last Samurai",
        "An American military advisor embraces the Samurai culture he was hired to destroy after he is captured in battle.",
        "https://static.rogerebert.com/uploads/movie/movie_poster/the-last-samurai-2003/large_cRz4FRx731ulws6zHuQVaDXpx73.jpg",
        "https://www.youtube.com/watch?v=T50_qHEOahQ")

samurai_jack = media.Movie("Samurai Jack",
        "A samurai warrior fights against the evil entity that took him away from his home world.",
        "http://www.filmandtvnow.com/wp-content/uploads/2016/07/samurai-jack-returns-2016.jpg",
        "https://www.youtube.com/watch?v=VSrv_n4tw7w")

big_hero_six = media.Movie("Big Hero Six",
        "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
        "https://a.dilcdn.com/bl/wp-content/uploads/sites/25/2014/06/Disney_BigHero6_Poster_Baymax.jpg",
        "https://www.youtube.com/watch?v=rD5OA6sQ97M")

the_great_dictator = media.Movie("The Great Dictator",
        "Dictator Adenoid Hynkel tries to expand his empire while a poor Jewish barber tries to avoid persecution from Hynkel's regime.",
        "https://static.rogerebert.com/uploads/movie/movie_poster/the-great-dictator-1940/large_i9rN9JPbTHplRa9OLEwcymUAKvb.jpg",
        "https://www.youtube.com/watch?v=4sfJxdytYn4")

movies_list = [planet_earth, prince_of_egypt, natural_curiosities, patterns_of_evidence, indie_game,
        batman_begins, jago, sound_of_music, the_grand_budapest_hotel, the_matrix, the_karate_kid,
        the_last_samurai, samurai_jack, big_hero_six, the_great_dictator]

fresh_tomatoes.open_movies_page(movies_list)
