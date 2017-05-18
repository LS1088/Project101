dicta = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

print (dicta)

valuesToDelete = ['a', 'c', 'f']

for i in valuesToDelete:
    if i in dicta:
        del dicta[i]

print (dicta)
