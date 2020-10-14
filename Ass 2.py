# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']


alphabets = ['x', 'y', 'z']

a = [(i*j) for i in alphabets for j in range(1, 5)]

print(a)

# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz']

a1 = [i*alphabets[j] for i in range(1, 4) for j in range(len(alphabets))]

print(a1)


# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]


a2 = [[j] for i in range(3) for j in range(i+2, i+5)]


l1 = []


def pattern(elem):
    global l1
    l1.append(elem)


a3 = [j for i in range(4) for j in range(i+2, i+6)]
f, k = 0, 4
for i in range(4):
    pattern(a3[f:k])
    k += 4
    f += 4
print(a2, l1)


# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


LC = [(j, i) for i in range(1,4) for j in range(1, 4)]
print(LC)
