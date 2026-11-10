'''
Library management system models: LibraryItem (abstract), Book, Magazine, DVD, Member
'''
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    '''
    Abstract base class for all library items.
    Keeps track of availability and total items created.
    '''
    total_items = 0  # class attribute, shared by every item
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__available = True  # private
        LibraryItem.total_items += 1  # update the class attribute via the class name

    def is_available(self):
        '''Check if the item is available for borrowing.'''
        return self.__available

    def mark_borrowed(self):
        '''Mark the item as borrowed (not available).'''
        self.__available = False

    def mark_returned(self):
        '''Mark the item as returned (available).'''
        self.__available = True

    @abstractmethod
    def late_fee(self, days_late):
        '''Calculate the late fee for the item based on days late.'''
        pass  # every child class must implement this


class Book(LibraryItem):
    '''Book item in the library.'''
    DAILY_RATE = 2
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        '''Return a string description of the book.'''
        return f"Book: {self.title} by {self.author} (ID {self.item_id})"


class Magazine(LibraryItem):
    '''Magazine item in the library.'''
    DAILY_RATE = 1
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        '''Return a string description of the magazine.'''
        return f"Magazine: {self.title} (Issue {self.issue_number}) (ID {self.item_id})"


class DVD(LibraryItem):
    '''DVD item in the library.'''
    DAILY_RATE = 5
    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        '''Return a string description of the DVD.'''
        return f"DVD: {self.title} ({self.duration_minutes} mins) (ID {self.item_id})"


class Member:
    '''Library member who can borrow items.'''
    def __init__(self, name, member_id, max_items=3):
        self.name = name
        self.member_id = member_id
        self.max_items = max_items
        self.__borrowed = []  # private list of items

    def borrow(self, item):
        '''Borrow an item if available and within the borrowing limit.'''
        if not item.is_available():
            raise ValueError(f"Item '{item.title}' is not available.")
        if len(self.__borrowed) >= self.max_items:
            raise ValueError(f"Member '{self.name}' has reached the borrowing limit.")
        item.mark_borrowed()
        self.__borrowed.append(item)

    def return_item(self, item, days_late=0):
        '''Return a borrowed item and calculate any late fee.'''
        if item not in self.__borrowed:
            raise ValueError(f"Item '{item.title}' is not borrowed by member '{self.name}'.")
        item.mark_returned()
        self.__borrowed.remove(item)
        return item.late_fee(days_late)

    def borrowed_titles(self):
        '''Return a list of titles currently borrowed by the member.'''
        return [item.title for item in self.__borrowed]
