# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

# To find the largest and smallest value in a list or sequence:

def largest_value(number_list):
    largest = None
    # print('Before: ', largest)
    for iterVal in number_list:
        if largest is None or iterVal > largest:
            largest = iterVal
    return largest


def smallest_value(number_list):
    smallest = None
    # print('Before: ', smallest)
    for iterVal in number_list:
        if smallest is None or iterVal < smallest:
            smallest = iterVal
    return smallest


def compute_number(number_list):
    largest = largest_value(number_list)
    smallest = smallest_value(number_list)
    print('Largest: ', largest)
    print('Smallest: ', smallest)


def read_numbers_from_user():
    num_list = []
    i = 0
    while True:
        inp_var = input('Enter a number:')
        try:
            if inp_var == 'done':
                break
                # False
            else:
                num_list.append(int(inp_var))
                i = i + 1
        except:
            print('Invalid input')

    if not num_list:
        print('Numbers List is empty')
    else:
        compute_number(num_list)

# numbers = [3, 41, 12, 9, 74, 15, -1]
# compute_number(numbers)

read_numbers_from_user()

