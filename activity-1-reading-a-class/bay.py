"""
One parking bay.

A class is a description of a kind of thing. This one describes a
single bay in a car park: what it knows about itself, and what it
can be asked to do.
"""
class Bay:
    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.registration = None
        self.cars_used = 0

    def is_free(self):
        return self.registration is None

    def size_matches(self, wanted):
        return self.size == wanted

    def park(self, registration):
        if self.is_free():
            self.registration = registration
            self.cars_used += 1
            return True
        return False

    def leave(self):
        if self.is_free():
            print("This bay is already empty.")
            return None

        leaving = self.registration
        self.registration = None
        return leaving

    def describe(self):
        if self.is_free():
            return f"Bay {self.number} ({self.size}): free"
        return f"Bay {self.number} ({self.size}): {self.registration}"


bay = Bay(1, "standard")

print(bay.describe())
print(bay.is_free())
print(bay.park("AB12 CDE"))
print(bay.describe())
print(bay.is_free())
print(bay.park("XY99 ZZZ"))
print(bay.describe())
print(bay.leave())
print(bay.describe())
print("Cars used:", bay.cars_used)
