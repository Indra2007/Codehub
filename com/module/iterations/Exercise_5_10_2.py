# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

# To find the largest and smallest value in a list or sequence:

numbers = [3, 41, 12, 9, 74, 15, -1]

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

