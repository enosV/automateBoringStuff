spam = [10, 20, 40] #from a given array
spam[1:3] = ['CAT', 'DOG', 'BURGER'] #this is saying take index 1 through 3 but not including the 3rd index and replace it with this new list even if its longer
print(spam)

eggs = ['CAT', 'DOG', 'BURGER', 'SALAD'] #from a given array
print(eggs[:2]) # the :2 will print all things up to the 2nd index
print(eggs[1:]) # the 1: will print any after it

ham = ['CAT', 'DOG', 'BURGER'] #from a given array
del ham[1] # this will delete index 1
print(ham)

bacon = list('hello') #here list will turn the string hello into a list
print(bacon)