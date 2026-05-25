def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        cleaned_lines = []

        for line in lines:
            cleaned_lines.append(line.strip().upper())

        return cleaned_lines


def write_new_file(path, lines_list):
    with open(path, 'w', encoding='utf-8') as file:
        for line in lines_list:
            file.write(line + "\n")


def main():
    content = read_file("extra3.txt")
    write_new_file('extra3_1.txt', content)


main()
