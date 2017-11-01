import media
import fresh_tomatoes

planet_earth = media.Movie("Planet Earth", "A visual journey covering the wonders of planet Earth",
        "https://i.pinimg.com/736x/98/2f/cc/982fcc3212d1dab93f99bee02725c9cc--planet-earth-documentary-bbc-planet-earth.jpg",
        "https://www.youtube.com/watch?v=tiVNk6_0GdY")

prince_of_egypt = media.Movie("Prince of Egypt",
        "An Egyptian prince learns of his identity as a Hebrew and his destiny to become the chosen deliverer of his people.",
        "https://www.google.co.jp/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj_56vl4ZrXAhUEe7wKHdhxA4sQjRwIBw&url=http%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0120794%2F&psig=AOvVaw2ed_BR4H7FTp1ZEF85b1g8&ust=1509533146821359",
        "https://www.youtube.com/watch?v=zmBDY-fSlIs")



movies_list = [planet_earth, avatar, toy_story]

fresh_tomatoes.open_movies_page(movies_list)
