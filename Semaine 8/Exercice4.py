Movies = []
def add_new_movie():
    number_new_movies = int(input("Enter the number of new movies: "))
    for i in range(number_new_movies):
        movie_name = input("\nEnter the name of the movie: ")
        year = input("Enter the year of the movie: ")
        imdb = input("Enter the IMDB rating of the movie (out of 10): ")
        copies = input("Enter the number of copies of the movie: ")
        price = input("Enter the price of the movie: ")
        duration = input("Enter the duration of the movie in minutes: ")
        new_movie_dict = dict(name=movie_name, year=year, imdb=imdb, copies=copies, price=price, duration=duration)
        Movies.append(new_movie_dict)

add_new_movie()
print("\n")

only_available = True
def display_movies(only_available):
    if only_available:
        for movie in Movies:
            if int(movie["copies"]) > 0:
                print("Name:", movie["name"])
                print("Year:", movie["year"])
                print("IMDB:", movie["imdb"])
                print("Copies:", movie["copies"])
                print("Price:", movie["price"])
                print("Duration:", movie["duration"])
                print("")
    else:
        for movie in Movies:
            print("Name:", movie["name"])
            print("Year:", movie["year"])
            print("IMDB:", movie["imdb"])
            print("Copies:", movie["copies"])
            print("Price:", movie["price"])
            print("Duration:", movie["duration"])
            print("")

display_movies(only_available)

def display_movies_sorted_by_imdb():
    Movies.sort(key=lambda x: x["imdb"], reverse=True)
    display_movies(Movies)

def rent_movie():
    movie_name = input("Enter the name of the movie you want to rent: ")
    for movie in Movies:
        if movie_name == movie["name"]:
            if int(movie["copies"]) > 0:
                movie["copies"] = int(movie["copies"]) - 1
                print("Successfully rented the movie")
            else:
                print("Sorry, there are no copies left")

rent_movie()