# Stretch 2: Deciding what can be changed

File: `getters_and_setters.py`

Optional. Not needed for any assignment task.

A plain attribute can be set to anything by anyone. A property lets the class
decide what is allowed.

## Predict

Work out every line of output. The last line of the program does not print
anything, and that is deliberate.
AB12 CDE
30
60
Rejected: -5 is not a sensible number of days
60
Rejected: a fortnight is not a sensible number of days
60

## Run

Execute and compare. The program ends with an error on purpose.

## Investigate

- `_registration` has a leading underscore. Python does not stop you reading it.
  So what is the underscore actually for?
- `days_valid` can be read and written. `registration` can only be read. Which
  decorator makes the difference?
- Two of the three assignments to `days_valid` are rejected. What happens to the
  value in each case, and would you rather it printed, returned something, or
  raised?
- The final line raises an `AttributeError`. Is that better or worse than
  silently ignoring the assignment? Argue it.
1. A leading underscore in `_registration` signals that the attribute is intended for internal use. It is a convention, not a strict access restriction.
2. `@property` allows `registration` and `days_valid` to be read as attributes. `@days_valid.setter` defines how `days_valid` can be changed. No registration setter is provided, so assigning to `registration` raises an `AttributeError`.
3. Invalid values leave `days_valid` unchanged because the setter prints a message and returns without updating the attribute. Raising `ValueError` would make invalid assignments easier for calling code to detect and handle.
4. Raising `AttributeError` for an unsupported registration assignment is useful because it makes the mistake visible rather than silently ignoring it.

## Modify

- Make the rejected assignments raise a `ValueError` rather than printing.
- Add a `zone` attribute that can only be set once.
