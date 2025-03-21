class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.artists = []

    def calculate_royalty(self):
        return self.duration * 0.1

    def add_artist(self, artist):
        if not artist.strip():
            raise ValueError("Artist nie moze byc pusty")
        self.artists.append(artist)
