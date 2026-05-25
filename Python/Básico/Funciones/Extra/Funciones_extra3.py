def how_many_vocals(my_string):
    total_vocals = 0

    for letter in my_string:
        if letter.lower() in "aeiou":
            total_vocals += 1

    return total_vocals


my_string = "Hola mundo"

print(how_many_vocals(my_string))
