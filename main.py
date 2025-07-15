from stats import get_num_words, get_book_text, get_all_characters


def main():
    print(get_all_characters(get_book_text("books/frankenstein.txt")))


if __name__ == '__main__':
    main()
