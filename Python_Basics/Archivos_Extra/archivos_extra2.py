def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content.split()


def count_words(words_list):
    total_words = len(words_list)
    print(f"Este archivo contiene {total_words} palabras")


def main():
    words = read_file("extra2.txt")

    count_words(words)


main()
