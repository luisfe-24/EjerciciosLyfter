total_grades = int(input("Ingrese la cantidad de notas: "))

counter = 1

current_grade = 0

passed_count = 0
failed_count = 0

passed_avg = 0
failed_avg = 0
total_avg = 0

while counter <= total_grades:
    current_grade = int(input(f"Ingrese la nota numero {counter}: "))
    if current_grade < 70:
        failed_count = failed_count + 1
        failed_avg = failed_avg + current_grade

    else:
        passed_count = passed_count + 1
        passed_avg = passed_avg + current_grade
    total_avg = total_avg + (current_grade / total_grades)
    counter = counter + 1

if failed_count > 0:
    failed_avg = failed_avg / failed_count

if passed_count > 0:
    passed_avg = passed_avg / passed_count

print(f"Notas aprobadas: {passed_count}")
print(f"Promedio de notas aprobadas: {passed_avg}")

print(f"Notas desaprobadas: {failed_count}")
print(f"Promedio de notas desaprobadas: {failed_avg}")

print(f"Promedio total de notas: {total_avg}")
