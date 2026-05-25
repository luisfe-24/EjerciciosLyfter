name = "Luis"
lastname = "Brenes"
age = 19
hobbies = ["programar", "jugar videojuegos", "fotogafia"]
favorite_games = ["The Legend of Zelda: Breath of the Wild",
                  "Super Mario Odyssey", "Minecraft"]
weight = 75.5
student = True
worker = False


print(name + lastname)
# LuisBrenes

# print(name + age) no se puede sumar un string con entero, solo entero con entero.

# print(age + name) no se puede sumar un entero con un string, solo entero con entero.

print(hobbies + favorite_games)
# ['programar', 'jugar videojuegos', 'fotogafia', 'The Legend of Zelda: Breath of the Wild', 'Super Mario Odyssey', 'Minecraft']

# print(name + hobbies) no se puede sumar un string con una lista, solo string con string.

print(weight + age)
# 94.5

print(student + worker)
# True se considera como 1 y False se considera como 0, por lo tanto el resultado es 1.
