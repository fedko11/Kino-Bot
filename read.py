import sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# Connect to a database. If the file does not exist, it will be created.

def start_db():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description VARCHAR(50),
        url varchar(20)
    )
    """
    cursor.execute("""DROP TABLE movies""")
    cursor.execute(create_table_query)

def save_movies(name,description,url):
    insert_query = "INSERT INTO movies (name,description,url) VALUES (?, ?, ?)"
    users_data = [
        (name,  description,url),
    ]

    cursor.executemany(insert_query, users_data)
    connection.commit()
    
def fetch_movies(token):
  # Retrieve movie data
    select_query = "SELECT id, name, description,url FROM movies"
    cursor.execute(select_query)

    # Fetch all results
    results = cursor.fetchall()

    # Create a list of dictionaries to store results
    filtered_movies = []

    for row in results:
        # Create a dictionary for each row
        movie = {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "url": row[3]
        }

        # Check if the token is in any of the string fields
        if any(token.casefold() in str(value).casefold() for value in movie.values() if isinstance(value, str)):
            filtered_movies.append(movie)

    # Close the database connection
    connection.close()

    # Return the list of filtered movies
    return filtered_movies


start_db()


# Example usage
token = "HA"
save_movies("Titanik", "Zor kino","html")
save_movies("hamster", "seks porno","sbdcuwciewhciilwec")
save_movies("porno hub", "eva elfi","salom")
save_movies("wwojcojweocw", "Zor kino","html")
save_movies("Titanik", "Zor kino","html")
save_movies("HALICOPTER", "Zor kino","html")
save_movies("Titanik", "Zor kino","html")
save_movies("Titanik", "Zor kino","html")
movies = fetch_movies(token)


# Organize and display the results
# for movie in movies:
#     print(f"ID: {movie['id']}, Name: {movie['name']}, Description: {movie['description']}, URL: {movie['url']}")


