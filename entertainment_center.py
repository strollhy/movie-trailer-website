import media
import requests
import fresh_tomatoes

response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=<api_key>&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1")
movies = []

if response.status_code == 200:
    for res in response.json()["results"]:
        movie = media.Movie(res["title"], res["overview"], None, None)
        movie.poster_image_url = "https://image.tmdb.org/t/p/w300/" + res["poster_path"]

        trailer_response = requests.get("https://api.themoviedb.org/3/movie/%s/videos?api_key=<api_key>&language=en-US" % res["id"])
        # add to site only if the trailer is found
        if trailer_response.status_code == 200:
            movie.trailer_youtube_url = "https://www.youtube.com/watch?v=" + trailer_response.json()["results"][0]["key"]
            movies.append(movie)

fresh_tomatoes.open_movies_page(movies)
