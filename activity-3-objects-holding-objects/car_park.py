"""
A car park, which is a thing made of other things.

A CarPark does not hold registrations. It holds Bay objects, and
each Bay looks after its own registration. That division is the
whole idea of this activity.
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

    def leave(self):
        leaving = self.registration
        self.registration = None
        return leaving

    def describe(self):
        if self.is_free():
            return f"Bay {self.number} ({self.size}): free"
        return f"Bay {self.number} ({self.size}): {self.registration}"


class CarPark:
    def __init__(self, name):
        self.name = name
        self.bays = []

    def add_bay(self, number, size):
        self.bays.append(Bay(number, size))

    def free_bays(self, size):
        return [
            bay.number for bay in self.bays
            if bay.size == size and bay.is_free()
        ]

    def free_counts(self):
        counts = {}
        for bay in self.bays:
            if bay.is_free():
                counts[bay.size] = counts.get(bay.size, 0) + 1
        return counts

    def park(self, registration, size):
        for bay in self.bays:
            if bay.size == size and bay.is_free():
                bay.park(registration)
                return bay.number
        return None

    def find(self, registration):
        for bay in self.bays:
            if bay.registration == registration:
                return bay.number
        return None

    def leave(self, registration):
        for bay in self.bays:
            if bay.registration == registration:
                bay.leave()
                return True
        return False

    def report(self):
        lines = [self.name]
        for bay in self.bays:
            lines.append("  " + bay.describe())
        return "\n".join(lines)


park = CarPark("Ada Street")
park.add_bay(1, "standard")
park.add_bay(2, "standard")
park.add_bay(3, "accessible")
park.add_bay(4, "standard")
park.add_bay(5, "electric")

print("Free bays by size:", park.free_counts())
print("AB12 CDE parked in bay", park.park("AB12 CDE", "standard"))
print("XY99 ZZZ parked in bay", park.park("XY99 ZZZ", "standard"))
print("LM34 NOP parked in bay", park.park("LM34 NOP", "accessible"))
print("Free bays by size:", park.free_counts())
print("XY99 ZZZ is in bay", park.find("XY99 ZZZ"))
print("QQ11 QQQ is in bay", park.find("QQ11 QQQ"))
print("Car left:", park.leave("AB12 CDE"))
print(park.report())
