# For example, to count the number of items in a list, we would write the following for loop:

numbers = [3, 41, 12, 9, 74, 15, -1]


def compute_number_count(number_list):
    count = 0
    for interval in number_list:
        count += 1
    return count

# compute_number_count(numbers)


# computes the total of a set of numbers is as follows:

def compute_number_set(number_list):
    total = 0
    for interval in number_list:
        total = total + interval
    return total

# compute_number_set(numbers)

# loop that computes the total of a set of numbers is as follows


def compute_number(number_list):

    total = compute_number_set(number_list)
    count = compute_number_count(number_list)
    avg = total / count
    print('Total: ', total)
    print('Count: ', count)
    print('Average: ', avg)

# compute_number(numbers)

# To find the largest and smallest value in a list or sequence:


def largest_value(number_list):
    largest = None
    # print('Before: ', largest)
    for iterVal in number_list:
        if largest is None or iterVal > largest:
            largest = iterVal
    return largest

print('Largest: ', largest_value(numbers))


def smallest_value(number_list):
    smallest = None
    # print('Before: ', smallest)
    for iterVal in number_list:
        if smallest is None or iterVal < smallest:
            smallest = iterVal
    return smallest


print('Smallest: ', smallest_value(numbers))


# Exercise 1: Write a program which repeatedly reads numbers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

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


read_numbers_from_user()


