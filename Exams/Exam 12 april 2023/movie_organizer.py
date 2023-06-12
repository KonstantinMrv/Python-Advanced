def movie_organizer(*args):
    genres = {}

    for movie, genre in args:
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(movie)

    sorted_genres = sorted(genres.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for genre, movies in sorted_genres:
        sorted_movies = sorted(movies)
        result.append(f"{genre} - {len(sorted_movies)}")
        for name in sorted_movies:
            result.append(f"* {name}")
    return "\n".join(result)


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

