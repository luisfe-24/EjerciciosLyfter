def swipe_word(words):
    reversed_text = ""

    for index in range(len(words) - 1, -1, -1):
        reversed_text += words[index]

    return reversed_text


resultado = swipe_word("Hola Mundo")
print(resultado)
