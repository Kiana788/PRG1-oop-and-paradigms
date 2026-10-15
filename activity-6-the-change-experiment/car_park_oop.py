
"""
Car Park (object oriented version)

The same program as car_park_procedural.py, written with classes.
A Bay looks after its own registration; a CarPark holds Bay objects
and asks them things.

Both versions produce exactly the same output. Read them side by
side.
"""


class Bay:
    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.registration = None
        self.history = []

    def is_free(self):
        return self.registration is None

    def park(self, registration):
        if self.registration is None:
            self.registration = registration
            self.history.append(registration)
            return True
        return False

    def get_history(self):
        return self.history.copy()

    def leave(self):
        leaving = self.registration
        self.registration = None
        return leaving

    def describe(self):
        if self.registration is None:
            return f"Bay {self.number} ({self.size}): free"
        return f"Bay {self.number} ({self.size}): {self.registration}"

    def export_line(self):
        registration = self.registration or "free"
        return f"{self.number},{self.size},{registration}"


class CarPark:
    def __init__(self, name):
        self.name = name
        self.bays = []

    def add_bay(self, number, size):
        self.bays.append(Bay(number, size))

    def free_bays(self, size):
        free = []
        for bay in self.bays:
            if bay.size == size and bay.is_free():
                free.append(bay.number)
        return free

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

    def report(self):
        lines = [f"{self.name}"]
        for bay in self.bays:
            lines.append("  " + bay.describe())
        return "\n".join(lines)

    def export_bays(self, filename="bays.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for bay in self.bays:
                file.write(bay.export_line() + "\n")


park = CarPark("Ada Street")
park.add_bay(1, "standard")
park.add_bay(2, "standard")
park.add_bay(3, "accessible")
park.add_bay(4, "standard")

print(f"Bays: {len(park.bays)}")
print(f"Free standard bays: {park.free_bays('standard')}")

print(f"AB12 CDE parked in bay {park.park('AB12 CDE', 'standard')}")
print(f"XY99 ZZZ parked in bay {park.park('XY99 ZZZ', 'standard')}")
print(f"LM34 NOP parked in bay {park.park('LM34 NOP', 'accessible')}")

print(f"Free standard bays: {park.free_bays('standard')}")
print(f"XY99 ZZZ is in bay {park.find('XY99 ZZZ')}")
print(f"QQ11 QQQ is in bay {park.find('QQ11 QQQ')}")
print("---")
print(park.report())

park.export_bays()
print("Bay data exported to bays.txt")
