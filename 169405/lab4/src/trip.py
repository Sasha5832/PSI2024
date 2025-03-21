class Trip:
    def __init__(self, destination, duration):
        self._destination = None
        self._duration = None
        self._participants = []
        self._price_per_day = 100

        self.destination = destination
        self.duration = duration

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        if not isinstance(value, str):
            raise TypeError("Destination must be a string")
        if not value.strip():
            raise ValueError("Destination cannot be empty")
        self._destination = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, int):
            raise TypeError("Duration must be an integer")
        if value <= 0:
            raise ValueError("Duration must be greater than 0")
        self._duration = value

    @property
    def price_per_day(self):
        return self._price_per_day

    @price_per_day.setter
    def price_per_day(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price per day must be a number")
        if value <= 0:
            raise ValueError("Price per day must be greater than 0")
        self._price_per_day = value

    def calculate_cost(self):
        return self.duration * self.price_per_day

    @property
    def participants(self):
        return self._participants.copy()

    def add_participant(self, participant):
        if not isinstance(participant, str):
            raise TypeError("Participant name must be a string")
        if not participant.strip():
            raise ValueError("Participant name cannot be empty")
        self._participants.append(participant)
