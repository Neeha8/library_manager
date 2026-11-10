'''
Main script to demonstrate the library management system.
'''
from models import LibraryItem, Book, Member, Magazine, DVD

print("=== Abstract parent ===")
try:
    LibraryItem("Sample", 0)
except TypeError:
    print("LibraryItem cannot be created directly: late_fee() is abstract.")

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 42)
dvd = DVD("Python Recording", 3, 148)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

print("\n=== Borrowing and invalid actions ===")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.borrow(book)
except ValueError as e:
    print("Could not borrow again:", e)

try:
    bob.borrow(magazine)  # should succeed
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: borrow limit reached
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.return_item(dvd)  # should fail: not borrowed by Alice
except ValueError as e:
    print("Could not return:", e)

print("\n=== Polymorphic late fees ===")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

print("\n=== Returns ===")
try:
    fee = alice.return_item(book, days_late=3)
    print("Alice returned:", book.title, "-> late fee: Rs", fee)
    fee = bob.return_item(magazine)
    print("Bob returned:", magazine.title, "-> late fee: Rs", fee)
    bob.borrow(dvd)
    print("Bob borrowed after returning:", dvd.title)
    fee = bob.return_item(dvd, days_late=3)
    print("Bob returned:", dvd.title, "-> late fee: Rs", fee)
except ValueError as e:
    print("Could not complete transaction:", e)

try:
    alice.return_item(book)
except ValueError as e:
    print("Could not return again:", e)

print("\n=== Encapsulation ===")
try:
    print(book.__available)
except AttributeError:
    print("Direct access to book.__available raises AttributeError.")
print("Book available through is_available():", book.is_available())
print("Alice's borrowed titles:", alice.borrowed_titles())
print("Bob's borrowed titles:", bob.borrowed_titles())
titles = alice.borrowed_titles()
titles.append("Not a real loan")
print("Changing the returned titles list leaves Alice's loans unchanged:",
      alice.borrowed_titles())

print("\n=== Shared class attribute ===")
print("Total items created:", LibraryItem.total_items)
