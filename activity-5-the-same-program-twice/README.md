# Activity 5: The same program, twice

Files: `car_park_procedural.py`, `car_park_oop.py`

Two versions of the same car park. One uses dictionaries and functions, the
other uses classes. They produce character-for-character identical output.

No predicting this time. Read them side by side, in pairs, out loud.

## Read

Open both files next to each other. Work through them together and fill this in:

| Procedural | Object oriented |
|---|---|
| `make_bay(1, "standard")` | |
| `is_free(bay)` | |
| `free_bays(bays, size)` | |
| `park(bays, reg, size)` | |
| the `bays` list | |
Procedural                            Object-oriented

make_bay(1, "standard")	              Bay(1, "standard")
is_free(bay)	                        bay.is_free()
free_bays(bays, size)	                park.free_bays(size)
park(bays, reg, size)	                park.park(reg, size)
The bays list contains dictionaries.	The bays list contains Bay objects.

## Run

Run both. Check for yourself that the output is identical.

## Investigate

- In the procedural version, where is a bay's registration stored, and what else
  in the program is allowed to change it?
- In the object oriented version, same two questions.
- The procedural functions all take the thing they work on as their first
  argument. The methods do not appear to. Where did that argument go?
- `describe_bay(bay)` and `bay.describe()` do the same job. Say each one out
  loud in English. Which sentence sounds more like what is actually happening?
- Neither version is better as it stands. They are the same length and they do
  the same thing. So what would have to change about the requirements before one
  of them became clearly better? Write down a guess. Activity 6 tests it.
  1. In the procedural version, a bay's registration is stored in the dictionary under `"registration"`. Any code with access to that dictionary can change it.

2. In the object-oriented version, the registration is stored in `bay.registration`. Any code with access to the object can also change it directly, although the intended approach is to use methods such as `bay.park()` and `bay.leave()`.

3. The first argument has not disappeared in the object-oriented version. Python passes the object as `self` when an instance method is called.

4. `describe_bay(bay)` means "describe this bay", while `bay.describe()` means "ask this bay to describe itself". Both can do the same job.

5. The best approach depends on future requirements. Object-oriented programming may be easier to extend when different types of bays have different behaviours. Procedural programming may be simpler for a small, straightforward program. Testing changes provides evidence for the decision.

> Do not finish this activity with a view about which paradigm is better. Finish
> it able to describe accurately what each one does. The opinion comes next, and
> it needs evidence.
