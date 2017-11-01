import media
import fresh_tomatoes

planet_earth = media.Movie("Planet Earth", "A visual journey covering the wonders of planet Earth",
        "https://i.pinimg.com/736x/98/2f/cc/982fcc3212d1dab93f99bee02725c9cc--planet-earth-documentary-bbc-planet-earth.jpg",
        "https://www.youtube.com/watch?v=tiVNk6_0GdY")

prince_of_egypt = media.Movie("Prince of Egypt",
        "An Egyptian prince learns of his identity as a Hebrew and his destiny to become the chosen deliverer of his people.",
        "https://www.google.co.jp/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj_56vl4ZrXAhUEe7wKHdhxA4sQjRwIBw&url=http%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0120794%2F&psig=AOvVaw2ed_BR4H7FTp1ZEF85b1g8&ust=1509533146821359",
        "https://www.youtube.com/watch?v=zmBDY-fSlIs")

natural_curiosities = media.Movie("Natural Curiosities",
        "David Attenborough presents a collection of his favourite natural curiosities found throughout the animal kingdom from armoured giants to crafty insects.",
        "https://www.google.co.jp/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj0v5Sg5JrXAhWIS7wKHXNsAKEQjRwIBw&url=https%3A%2F%2Fwww.themoviedb.org%2Ftv%2F58703-david-attenborough-s-natural-curiosities%2Fimages%2Fposters&psig=AOvVaw1QF8qvQMVBqheUSTy5w19m&ust=1509536615644068",
        "https://www.youtube.com/watch?v=gNpJGAIo-YU")

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




movies_list = [planet_earth, avatar, toy_story]

fresh_tomatoes.open_movies_page(movies_list)
