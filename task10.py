movie_ratings = {
    "Inception": 8.8,
    "Interstellar": 8.6,
    "Parasite": 8.9,
    "The Dark Knight": 9.0,
    "Avengers: Endgame": 8.4
}

highest_rated_movie = max(movie_ratings.items(), key=lambda x: x[1])

top_3_movies = sorted(movie_ratings.items(), key=lambda x: x[1], reverse=True)[:3]

average_rating = sum(movie_ratings.values()) / len(movie_ratings)

print(f"Highest Rated Movie: {highest_rated_movie[0]} ({highest_rated_movie[1]})")
print(f"Top 3 Movies: {top_3_movies}")
print(f"Average Rating: {average_rating:.2f}")

