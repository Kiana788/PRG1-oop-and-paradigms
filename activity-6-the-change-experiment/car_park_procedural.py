
"""
Car Park (procedural version)

The same program as car_park_oop.py, written without classes. Bays
are dictionaries, the car park is a list of them, and the functions
are passed the list they work on.

Both versions produce exactly the same output. Read them side by
side.
"""


def make_bay(number, size):
    return {
        "number": number,
        "size": size,
        "registration": None,
        "history": []
    }


def is_free(bay):
    return bay["registration"] is None


def describe_bay(bay):
    if bay["registration"] is None:
        return f"Bay {bay['number']} ({bay['size']}): free"
    return f"Bay {bay['number']} ({bay['size']}): {bay['registration']}"


def free_bays(bays, size):
    free = []
    for bay in bays:
        if bay["size"] == size and is_free(bay):
            free.append(bay["number"])
    return free


def park(bays, registration, size):
    for bay in bays:
        if bay["size"] == size and is_free(bay):
            bay["registration"] = registration
            bay["history"].append(registration)
            return bay["number"]
    return None


def bay_history(bay):
    return bay["history"]


def find(bays, registration):
    for bay in bays:
        if bay["registration"] == registration:
            return bay["number"]
    return None


def report(name, bays):
    lines = [name]
    for bay in bays:
        lines.append("  " + describe_bay(bay))
    return "\n".join(lines)


def export_bays(bays, filename="bays.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for bay in bays:
            registration = bay["registration"] or "free"
            file.write(
                f"{bay['number']},{bay['size']},{registration}\n"
            )


bays = [
    make_bay(1, "standard"),
    make_bay(2, "standard"),
    make_bay(3, "accessible"),
    make_bay(4, "standard"),
]

print(f"Bays: {len(bays)}")
print(f"Free standard bays: {free_bays(bays, 'standard')}")

print(f"AB12 CDE parked in bay {park(bays, 'AB12 CDE', 'standard')}")
print(f"XY99 ZZZ parked in bay {park(bays, 'XY99 ZZZ', 'standard')}")
print(f"LM34 NOP parked in bay {park(bays, 'LM34 NOP', 'accessible')}")

print(f"Free standard bays: {free_bays(bays, 'standard')}")
print(f"XY99 ZZZ is in bay {find(bays, 'XY99 ZZZ')}")
print(f"QQ11 QQQ is in bay {find(bays, 'QQ11 QQQ')}")
print("---")
print(report("Ada Street", bays))

export_bays(bays)
print("Bay data exported to bays.txt")
