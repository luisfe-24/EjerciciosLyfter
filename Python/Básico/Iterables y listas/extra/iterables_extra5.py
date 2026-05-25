user_list = []

new_list = []

total_words = 5

for index in range(0, total_words):
    current_word = str(input(f"Ingresa la palabra {index + 1}: "))
    user_list.append(current_word)
    if (len(current_word)) > 4:
        new_list.append(current_word)

print(f"Lista completa: {user_list}")
print(f"Lista de palabras con más de 4 letras: {new_list}")
