# Functions for analyzing text

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def get_all_characters(text):
    text = text.lower()
    characters = {}
    for char in text:
        characters[char] = characters.get(char, 0) + 1

    return characters

