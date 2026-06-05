my_list = [9, 4, 7, 1, 5]

min_number = my_list[0]

for record in my_list:
    if record < min_number:
        min_number = record

print(f"El menor valor es {min_number}")
