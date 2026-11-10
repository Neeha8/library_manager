# Campus Library Manager

Requires Python 3.12 or later and no external packages. From this folder, run:

```shell
python main.py
```

On systems that use `python3`, run `python3 main.py`. The final demo's console output is recorded in [output.txt](output.txt).


### Why is LibraryItem abstract, and what happens if DVD forgets late_fee()?

`LibraryItem` shares the common item state and behavior but requires each concrete item type to implement its own late-fee calculation. If `DVD` omits `late_fee()`, it remains abstract, and attempting to create a DVD raises `TypeError`.

### What happens when you read item.__available, and why use is_available()?

Reading `item.__available` outside the class raises `AttributeError` because Python name-mangles the double-underscore attribute. Using `is_available()` provides a public way to read availability while normal changes go through `mark_borrowed()` and `mark_returned()`; name mangling prevents accidental access, not deliberate access.

### How do LibraryItem.total_items and self.title differ?

`LibraryItem.total_items` is a class attribute shared across item types and counts successfully created items. `self.title` is an instance attribute, so each book, magazine, or DVD stores its own title independently.