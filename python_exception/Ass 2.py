subjects = ['Americans', 'Indians']
verbs = ['play', 'watch']
objects = ['Baseball', 'Cricket']

Am = [list(zip(subjects, [i], [j])) for i in verbs for j in objects ]


In = [list(zip([subjects[1]], [i], [j])) for i in verbs for j in objects]


[print(i, j, k) for f in range(4) for i, j, k in Am[f]]

[print(i, j, k) for f in range(4) for i, j, k in In[f] ]
