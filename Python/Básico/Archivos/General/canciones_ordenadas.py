def sort_songs_alphabetically(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    cleaned_songs = []

    for line in lines:
        cleaned_songs.append(line.strip())

    sorted_songs = sorted(cleaned_songs)

    return sorted_songs


def write_new_file(path, songs_list):
    with open(path, "w") as file:
        for song in songs_list:
            file.write(song + "\n")


def main():
    sorted_songs = sort_songs_alphabetically("lista_canciones.txt")

    write_new_file("lista_canciones_ordenada.txt", sorted_songs)


main()
