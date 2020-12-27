print('how many cats do you have') #we are not specifying if the user can an enter an integer or a string; but we can catch the string and except the error
numCats = input()
try:
    if int(numCats) >= 4:
        print ('That is a lot of cats')
    else:
        print('that aint much')
except ValueError:
    print('Must be an integer')