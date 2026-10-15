"""
Optional stretch. Controlling what can be changed from outside.

A plain attribute can be set to anything by anyone. A property lets
the class decide what is allowed.
"""

class Permit:
    def __init__(self, registration, days_valid, zone):
        if not isinstance(days_valid, int) or days_valid < 1:
            raise ValueError("Days valid must be a positive integer")

        self._registration = registration
        self._days_valid = days_valid
        self._zone = zone

    @property
    def registration(self):
        return self._registration

    @property
    def days_valid(self):
        return self._days_valid

    @days_valid.setter
    def days_valid(self, value):
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError("Days valid must be a positive integer")
        self._days_valid = value

    @property
    def zone(self):
        return self._zone


permit = Permit("AB12 CDE", 30, "A")

print(permit.registration)
print(permit.days_valid)

permit.days_valid = 60
print(permit.days_valid)

try:
    permit.days_valid = -5
except ValueError as error:
    print("Rejected:", error)

try:
    permit.days_valid = "a fortnight"
except ValueError as error:
    print("Rejected:", error)

print("Days still valid:", permit.days_valid)

# This would raise AttributeError:
# permit.registration = "XY99 ZZZ"

# This would also raise AttributeError:
# permit.zone = "B"

