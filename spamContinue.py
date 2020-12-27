spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue #this will reset back to the start
    print('spam is ' + str(spam))