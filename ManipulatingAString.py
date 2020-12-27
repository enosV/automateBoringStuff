name = 'Chorro'

print(name[0]) #prints the letter on index 0, C

print(name[1:3]) #prints the letters between index 1 and 3 but not including 3, ho

print(name[-2]) #prints the second letter starting from right to left, r

print('Ch' in name) #checks to see if ch is in name, which is TRUE

print('xxx' in name) #checks to see if xxx is in name, which is FALSE

for letter in name: #this prints a vertical representation of the string
    print(letter)

#the take away is that its not mutating the string like we can in an array/list. But we can create a new string to mutate it.

spam = [0, 1, 2, 3, 4, 5] #here we have a list set to spam
cheese = spam #we set cheese to spam, what python does is it just gives it the same reference id as spam's array
cheese[1] = 'hello' #we modify cheese at index 1
print(cheese) #cheese is updated
print(spam) #but so is spam -- this would not happen if spam was a string 


#if you need to change a list i.e. have seperate reference IDs then you should use import the copy module:

import copy
spam = ['A', 'B', 'C', 'D', 'E']
cheese = copy.deepcopy(spam) #here deepcopy will create a new ref. ID which allows us to change cheese without changing spam
cheese[2] = 45
print(cheese)
print(spam)