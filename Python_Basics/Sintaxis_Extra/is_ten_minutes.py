missing_time = 0

seconds_time = float(input("Digite un tiempo en segundos: "))

if seconds_time < 600:
    missing_time = 600 - seconds_time
    print(missing_time)

elif seconds_time > 600:
    print("Mayor")
else:
    print("Igual")
