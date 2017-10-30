import media

toy_story = media.Movie("Toy Story",
        "A boy whose toys come to life",
        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
        "A marine on an alien planet",
        "http://www.imdb.com/title/tt0499549/videoplayer/vi531039513?ref_=tt_ov_vi",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg")
print(avatar.poster_image_url)
