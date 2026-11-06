def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        for index in range(0, len(list_to_sort) - 1):
            current_number = list_to_sort[index]
            next_number = list_to_sort[index + 1]

            if current_number > next_number:
                list_to_sort[index] = next_number
                list_to_sort[index + 1] = current_number


list = [4, 5, 8, 3, 2, 1, 6, 10, 9, 7]

print(list)

bubble_sort(list)

print(list)
