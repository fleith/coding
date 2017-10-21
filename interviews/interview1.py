'''
Validate the string, checking all open and close brackets
'''

OPEN_BRACKETS = {'{', '(', '['}
CLOSE_BRACKETS = {'}', ')', ']'}
BRACKETS_MAP = {'{':'}', '(':')', '[':']'}


def check_string(s):
    stack = []
    for c in s:
        if c in CLOSE_BRACKETS:
            bracket = stack.pop()
            if c != BRACKETS_MAP[bracket]:
                return False
        if c in OPEN_BRACKETS:
            stack.append(c)
    return len(stack) == 0


assert check_string('{{}} + 3 + ((0 hs )) + {[]}') == True
assert check_string('{]}') == False
assert check_string('{{}[]()}') == True
assert check_string('{{()()([][{}])}[][]{{}{{{}}}}()}') == True
assert check_string('{{()()([][{}])}[][]{{1234*303044}{{{}}}}()}') == True
assert check_string('{{()()([][{}])}[][]{{1234*303044}{{{[}}}}()}') == False


'''
Given a flat file of book metadata, write a Library class that parses the book data and provides an API that lets you search for all books containing a word.

API:

Library
- <constructor>(input) -> returns a Library object
- search(word) -> returns all books that contain the word anywhere in the
                  title, author, or description fields. Only matches *whole* words.
E.g. Searching for "My" or "book" would match a book containing "My book", but searching for "My b" or "boo" would *not* match.
'''

LIBRARY_DATA = """
TITLE: Hitchhiker's Guide to the Galaxy
AUTHOR: Douglas Adams
DESCRIPTION: Seconds before the Earth is demolished to make way for a galactic freeway, Arthur Dent is plucked off the planet by his friend Ford Prefect, a researcher for the revised edition of The Hitchhiker's Guide to the Galaxy who, for the last fifteen years, has been posing as an out-of-work actor.

TITLE: Dune
AUTHOR: Frank Herbert
DESCRIPTION: The troubles begin when stewardship of Arrakis is transferred by the Emperor from the Harkonnen Noble House to House Atreides. The Harkonnens don't want to give up their privilege, though, and through sabotage and treachery they cast young Duke Paul Atreides out into the planet's harsh environment to die. There he falls in with the Fremen, a tribe of desert dwellers who become the basis of the army with which he will reclaim what's rightfully his. Paul Atreides, though, is far more than just a usurped duke. He might be the end product of a very long-term genetic experiment designed to breed a super human; he might be a messiah. His struggle is at the center of a nexus of powerful people and events, and the repercussions will be felt throughout the Imperium.

TITLE: A Song Of Ice And Fire Series
AUTHOR: George R.R. Martin
DESCRIPTION: As the Seven Kingdoms face a generation-long winter, the noble Stark family confronts the poisonous plots of the rival Lannisters, the emergence of the White Walkers, the arrival of barbarian hordes, and other threats.
"""

class Book():
    def __init__(self, title, author, description):
        self._title = title
        self._author = author
        self._description = description

    @property
    def title(self):
        return self._title

    def author(self):
        return self._author

    def description(self):
        return self._description

    def has_word(self, word):
        if word in self._title:
            return True
        if word in self._author:
            return True
        if word in self._description:
            return True
        return False

    def __repr__(self):
        return str(self._title) + str(self._author) + str(self._description)


class Library:
    def __init__(self, data):
        title = ''
        author = ''
        self._books = []
        for item in data.split('\n'):
            if 'TITLE' in item:
                title = item[len('TITLE: '):]
            elif 'AUTHOR' in item:
                author = item[len('AUTHOR: '):]
            elif 'DESCRIPTION' in item:
                self._books.append(Book(title, author, item[len('DESCRIPTION: '):]))
                title = ''
                author = ''

    def search(self, word):
        items = [ book for book in self._books if book.has_word(word) ]
        return items


library = Library(LIBRARY_DATA)
first_results = library.search("Arrakis")
assert first_results[0].title == "Dune"
second_results = library.search("winter")
assert second_results[0].title == "A Song Of Ice And Fire Series"
third_results = library.search("demolished")
assert third_results[0].title == "Hitchhiker's Guide to the Galaxy"
fourth_results = library.search("the")
assert len(fourth_results) == 3
assert fourth_results[0].title == "Hitchhiker's Guide to the Galaxy"
assert fourth_results[1].title == "Dune"
assert fourth_results[2].title == "A Song Of Ice And Fire Series"

