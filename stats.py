# Functions for analyzing text

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())

#count number of each character into the dictionary
def get_all_characters(text):
    text = text.lower()
    characters = {}
    for char in text:
        characters[str(char)] = characters.get(char, 0) + 1

    return characters


def sort_dictionary(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))