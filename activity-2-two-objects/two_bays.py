"""
Two bays, one class.

The same class as activity 1, used twice. The interesting part is
what each object knows, and what the word self is actually doing.
"""

class Bay:
    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.registration = None

    def is_free(self):
        return self.registration is None

    def park(self, registration):
        if self.is_free():
            self.registration = registration
            return True
        return False

    def describe(self):
        if self.is_free():
            return f"Bay {self.number} ({self.size}): free"
        return f"Bay {self.number} ({self.size}): {self.registration}"


first = Bay(1, "standard")
second = Bay(2, "accessible")
third = Bay(3, "standard")  # Separate object
fourth = Bay(4, "electric")

first.park("AB12 CDE")
second.park("XY99 ZZZ")
fourth.park("LM34 NOP")

bays = [first, second, third, fourth]

for bay in bays:
    print(bay.describe())
