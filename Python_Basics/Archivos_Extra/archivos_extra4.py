def append_to_file(path, extra_text):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(extra_text + "\n")


def main():
    additional_text = input("Ingrese el texto: ")
    append_to_file('extra4.txt', additional_text)


main()
