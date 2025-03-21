import unittest
from lab4.src.song import Song

class TestSongInitialization(unittest.TestCase):
    def test_song_creation(self):
        song = Song("Bohemian Rhapsody", 355)
        self.assertEqual(song.title, "Bohemian Rhapsody")
        self.assertEqual(song.duration, 355)

    def test_calculate_royalty(self):
        song1 = Song("Bohemian Rhapsody", 355)
        self.assertEqual(song1.calculate_royalty(), 35.5)

        song2 = Song("Yesterday", 125)
        self.assertEqual(song2.calculate_royalty(), 12.5)

    def test_add_artist(self):
        song = Song("Bohemian Rhapsody", 355)
        song.add_artist("Freddie Mercury")
        self.assertIn("Freddie Mercury", song.artists)

        song.add_artist("Brian May")
        song.add_artist("Roger Taylor")
        self.assertListEqual(song.artists, ["Freddie Mercury", "Brian May", "Roger Taylor"])

    def test_add_empty_artist_raises_error(self):
        song = Song("Bohemian Rhapsody", 355)
        with self.assertRaises(ValueError) as context:
            song.add_artist(" ")
        self.assertEqual(str(context.exception), "Artist nie moze byc pusty")

    def test_calculate_royalty_for_zero_seconds(self):
        song = Song("Silence", 0)
        self.assertEqual(song.calculate_royalty(), 0)

    def test_adding_duplicate_artist(self):
        song = Song("Bohemian Rhapsody", 355)
        song.add_artist("Freddie Mercury")
        song.add_artist("Freddie Mercury")
        self.assertEqual(song.artists.count("Freddie Mercury"), 2)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
