import requests

def movie_details(movie_name):
    url = "https://www.omdbapi.com/"
    params = {
        "t" : movie_name,
        "apikey" : "1660fab9"
    }
    response = requests.get(url,params=params, timeout=10)
    data = response.json()

    if data["Response"] == "True":
        title = data['Title']
        year = data['Year']
        genre = data['Genre']
        director = data['Director']
        IMDb_rating = data['imdbRating']
        print(title, year, genre, director, IMDb_rating)
    else:
        print("Movie not found")

def main():
    try:
        movie_name = input("Enter a movie name: ")
        movie_details(movie_name)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()