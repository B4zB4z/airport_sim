import random

class RandomEvents:
    def random_event(self):
        roll = random.randint(1, 100)
        if roll <= 60:
            return "nothing"
        elif roll <= 90:
            return "emergency"
        else:
            return "severe_emergency"
