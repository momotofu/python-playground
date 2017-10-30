import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
        "A boy whose toys come to life",
        "http://i0.kym-cdn.com/photos/images/original/001/045/043/cdc.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
        "A marine on an alien planet",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

planet_earth = media.Movie("Planet Earth", "A visual journey covering the wonders of planet Earth",
        "https://i.pinimg.com/736x/98/2f/cc/982fcc3212d1dab93f99bee02725c9cc--planet-earth-documentary-bbc-planet-earth.jpg",
        "https://www.youtube.com/watch?v=tiVNk6_0GdY")

movies_list = [planet_earth, avatar, toy_story]

fresh_tomatoes.open_movies_page(movies_list)
