import unittest
from src.trip import Trip

class TestTripInitialization(unittest.TestCase):
    def test_trip_creation(self):
        trip = Trip("Paris", 7)
        self.assertEqual(trip.destination, "Paris")
        self.assertEqual(trip.duration, 7)

    def test_invalid_destination(self):
        with self.assertRaises(TypeError):
            Trip(123, 7)
        with self.assertRaises(ValueError):
            Trip(" ", 7)

    def test_invalid_duration(self):
        with self.assertRaises(TypeError):
            Trip("Paris", "seven")
        with self.assertRaises(ValueError):
            Trip("Paris", 0)
        with self.assertRaises(ValueError):
            Trip("Paris", -5)

class TestTripMethods(unittest.TestCase):
    def test_calculate_cost(self):
        trip1 = Trip("Paris", 7)
        self.assertEqual(trip1.calculate_cost(), 700)

        trip2 = Trip("Rome", 5)
        self.assertEqual(trip2.calculate_cost(), 500)

    def test_participants_initially_empty(self):
        trip = Trip("Paris", 7)
        self.assertEqual(trip.participants, [])

    def test_add_participant(self):
        trip = Trip("Paris", 7)
        trip.add_participant("John")
        self.assertIn("John", trip.participants)

        trip.add_participant("Alice")
        trip.add_participant("Bob")
        self.assertListEqual(trip.participants, ["John", "Alice", "Bob"])

    def test_add_invalid_participant(self):
        trip = Trip("Paris", 7)
        with self.assertRaises(ValueError):
            trip.add_participant(" ")
        with self.assertRaises(TypeError):
            trip.add_participant(123)

    def test_participants_immutable(self):
        trip = Trip("Paris", 7)
        trip.add_participant("John")
        participants_copy = trip.participants
        participants_copy.append("Alice")
        self.assertNotIn("Alice", trip.participants)

    def test_setting_price_per_day(self):
        trip = Trip("Paris", 7)
        self.assertEqual(trip.price_per_day, 100)

        trip.price_per_day = 150
        self.assertEqual(trip.price_per_day, 150)

        with self.assertRaises(ValueError):
            trip.price_per_day = 0
        with self.assertRaises(ValueError):
            trip.price_per_day = -50
        with self.assertRaises(TypeError):
            trip.price_per_day = "expensive"

    def test_cost_with_price_per_day_change(self):
        trip = Trip("Paris", 7)
        trip.price_per_day = 150
        self.assertEqual(trip.calculate_cost(), 1050)

    def test_adding_duplicate_participant(self):
        trip = Trip("Paris", 7)
        trip.add_participant("John")
        trip.add_participant("John")
        self.assertEqual(trip.participants.count("John"), 2)

if __name__ == "__main__":
    unittest.main()
