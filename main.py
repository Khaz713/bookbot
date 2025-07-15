from stats import get_num_words, get_book_text, get_all_characters, sort_dictionary
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    print(f'============ BOOKBOT ============\n'
          f'Analyzing book found at {path}...')
    words_count = get_num_words(book_text)
    print(f'----------- Word Count ----------\n'
          f'Found {words_count} total words.')
    characters_count =sort_dictionary(get_all_characters(book_text))
    print(f'--------- Character Count -------')
    for key in characters_count:
        if key[0].isalpha():
            print(f'{key[0]}: {characters_count[key]}')
    print('============= END ===============')


if __name__ == '__main__':
    main()
