user_data = {}

user_list = ["first_name", "last_name", "age", "role"]
data_list = ["Luis", "Brenes", 19, "Software Engineer"]

for index in range(len(user_list)):
    user_data[user_list[index]] = data_list[index]

print(user_data)
