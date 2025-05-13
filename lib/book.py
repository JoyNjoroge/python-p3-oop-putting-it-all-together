#!/usr/bin/env python3

class Book:
    # first test
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    # testing it
# book = Book("And Then There Were None", 272)
# print(book.title)
# print(book.page_count)

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance (value, int):
            print("page_count must be an integer")
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        