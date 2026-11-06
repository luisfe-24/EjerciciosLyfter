def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        for index in range(len(list_to_sort) - 1, 0, -1):
            current_number = list_to_sort[index]
            prev_number = list_to_sort[index - 1]

            if current_number < prev_number:
                list_to_sort[index] = prev_number
                list_to_sort[index - 1] = current_number


list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(list)

bubble_sort(list)

print(list)
