number_list = []

for index in range(10):
    user_number = int(input(f"Ingrese el numero {index+1}: "))
    number_list.append(user_number)

max_number = number_list[0]

for current_number in number_list:
    if current_number > max_number:
        max_number = current_number

print(f"{number_list}. El más alto fue {max_number}")
