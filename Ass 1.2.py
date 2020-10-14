

# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))


def my_filter(elem):
    val = True if elem % 2 == 0 else False
    return val


for i in [1, 2, 3, 54, 88]:
    a = my_filter(i)
    print(i) if a == 1 else 0

