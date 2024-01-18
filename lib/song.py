# The Song class can produce individual songs. Each song has a name, an artist and a genre. 
class Song:
    # We need our Song class to be able to keep track of the number of songs that it creates. Song.count
    # Create a class attribute, count. We will use this attribute to keep track of the number of new songs that are created from the Song class. Set this attribute equal to 0.
    count = 0

    # We need our Song class to be able to show us all of the artists of existing songs:
    artists = []

    # We need our Song class to be able to show us all of the genres of existing songs:
    genres = []

    # We also need our Song class to be able to keep track of the number of songs of each genre it creates.
    genre_count = {}

    # Lastly, we want our Song class to reveal to us the number of songs each artist is responsible for.
    artist_count = {}

    # Define your Song class such that an individual song is initialized with a name, artist and genre.
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists.append(self.artist)
        Song.genres.append(self.genre)
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

