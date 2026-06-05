def is_prime(number):
    if number <= 1:
        return False

    for index in range(2, number):
        if number % index == 0:
            return False
    return True


def filter_primes(my_list):
    prime_list = []

    for number in my_list:
        if is_prime(number):
            prime_list.append(number)
    return prime_list


print(filter_primes([1, 4, 6, 7, 13, 9, 67]))
