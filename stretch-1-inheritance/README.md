# Stretch 1: One class built on another

File: `inheritance.py`

Optional. Not needed for any assignment task, and worth reaching only once the
core activities are done.

An `ElectricBay` is a `Bay` that also knows about a charger.

## Predict

Six lines of output. The last two are the ones to think about.
Bay 1 (standard): free
Bay 2 (standard): free  [22 kW charger, idle]
Bay 1 (standard): AB12 CDE
Bay 2 (standard): XY99 ZZZ  [charging at 22 kW]
False
True

## Run

Execute and compare.

## Investigate

- `ElectricBay` never defines `is_free`, and yet `electric.is_free()` works.
  Where did that method come from?
- `super().park(registration)` calls the `Bay` version, then `ElectricBay` does
  something extra. Why call the original at all rather than writing it out
  again?
- `isinstance(electric, Bay)` is `True`. An electric bay is a bay. Is a bay an
  electric bay? Check.
- `describe` exists on both classes. Which one runs, and how does Python decide?
1. `ElectricBay` inherits `is_free()` from `Bay`, so it can use that method without defining it again.
2. `super().park(registration)` reuses the parent's parking logic. This avoids duplicating code and allows the child class to add charging behaviour.
3. `isinstance(electric, Bay)` returns `True` because `ElectricBay` inherits from `Bay`. However, an ordinary `Bay` is not automatically an `ElectricBay`.
4. Python uses the method defined on the object's class first. Therefore, `ElectricBay.describe()` runs for electric bays, and `Bay.describe()` runs for ordinary bays.

## Modify

- Add a `DisabledBay` that requires a permit number before parking.
- Make `ElectricBay` refuse to park a car if the charger is broken.

> Inheritance is powerful and frequently misused. The usual test is whether the
> new thing genuinely *is a* kind of the old thing in every situation the
> program cares about. If you find yourself overriding most of the parent, it
> probably is not.
