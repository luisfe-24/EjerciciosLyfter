def upper_lower(my_string):
    upper_cases = 0
    lower_cases = 0

    for char in my_string:
        if char.isupper():
            upper_cases += 1
        elif char.islower():
            lower_cases += 1

    print(f"There's {upper_cases} upper cases and {lower_cases} lower cases")


upper_lower("I love Nación Sushi")
