my_list = [10, 20, 30, 40, 50]

total_sum = 0
count = 0

new_list = []

for record in my_list:
    total_sum += record
    count += 1

average = total_sum / count

for record in my_list:
    if record > average:
        new_list.append(record)

print(f"Promedio: {average}")
print(f"Nueva lista: {new_list}")
