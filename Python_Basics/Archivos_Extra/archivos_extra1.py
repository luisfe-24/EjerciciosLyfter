def transform_complete_file(path):
    # Usamos 'with' para un manejo seguro del archivo
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        cleaned_lines = []

        for line in lines:
            cleaned_lines.append(line.strip())

        single_line_text = " ".join(cleaned_lines)
        return single_line_text


def write_new_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    content = transform_complete_file("extra1.txt")
    write_new_file('extra1_1.txt', content)


main()
