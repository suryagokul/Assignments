""" from functools import reduce

last = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x+y, last))    # Using in-built reduce function

O/P  15

"""

# Implementing using own function


def my_reduce(elements):
    Sum = elements[0]
    for i in range(1, len(elements)):
        Sum += elements[i]

    return Sum


Value = my_reduce([1, 2, 3, 4, 5])
print(Value)
