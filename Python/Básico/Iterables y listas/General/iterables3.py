my_list = [4, 3, 6, 1, 7]

temp_value = my_list[0]

my_list[0] = my_list[-1]

my_list[-1] = temp_value

print(my_list)
