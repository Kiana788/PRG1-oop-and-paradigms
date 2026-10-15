# Activity 1: Reading a class

File: `bay.py`

One class, describing a single parking bay. Read it before you run it.

## Predict

Nine lines of output. Write them all down. Pay particular attention to the two
`park` calls: one of them does something and one of them does not.
Bay 1 (standard): free
True
True
Bay 1 (standard): AB12 CDE
False
False
Bay 1 (standard): AB12 CDE
AB12 CDE
Bay 1 (standard): free

## Run

Execute and compare.

## Investigate

- `Bay` is the description. `bay = Bay(1, "standard")` makes one actual bay from
  it. Which lines of the class run at the moment that happens?
- `self` appears in every method. Replace `self.registration` with `registration`
  in `is_free` and run it. Read the error. What is `self` actually standing in
  for?
- `park` returns `True` or `False` rather than printing anything. Why is that
  more useful than printing "parked" inside the method?
- `describe` reads `self.registration` but never changes it. `leave` changes it.
  Which methods ask the bay something, and which tell it to do something?
1. When `bay = Bay(1, "standard")` executes, Python calls `__init__()`. It sets the bay's number, size and registration.

2. `self` refers to the particular object the method is working with. Without `self.registration`, Python looks for a local variable called `registration`, which does not exist in `is_free()` and causes a `NameError`.

3. Returning `True` or `False` allows other code to make decisions using the result. Printing inside the method would restrict how the result could be used.

4. `is_free()` asks a question, `describe()` provides information, and `park()` and `leave()` change the bay's state.


## Modify

- Add a `size_matches(wanted)` method that says whether this bay is the right
  size.
- Make `leave` return `None` and print a message if the bay was already empty.
- Add an attribute recording how many cars have used this bay, and update it in
  the right place.

> A class is a description of a kind of thing: what it knows about itself, and
> what it can be asked to do. Everything else today is built on that sentence.
