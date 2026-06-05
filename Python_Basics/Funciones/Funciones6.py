def sort_string(my_string):
    new_list = my_string.split("-")

    new_list.sort()

    return "-".join(new_list)


print(sort_string("python-variable-funcion-computadora-monitor"))
