eggs = range(4)
print(eggs) #this is just to see it more explicitly 

for i in range(4):
    print (i) #here we're doing taking that same range in passing it through a loop where it goes through the list 0 - 4 but no including 4


ham = list(range(4))
print(ham) #this time we're passing it through list to create a list from that range's parameter

supplies = ['hammer', 'drill', 'wrench', 'screwdriver']
for i in range(len(supplies)): #in order to loop through the supplies we have to turn it into a list using len
    print('Index ' + str(i) + ' in supplies: ' + supplies[i]) #because we turned supplies into an list, i.e. integers, we have to turn it back to a string to concat 


#cat = ['fat', 'orange', 'loud']
#size = cat[0]
#color = cat[1]
#disposition = cat[2]
#size, color, dispotion = cat # this one line does the same as the 4 lines above, it's called multiple assignment as a trick

#spam = 42
#spam += 1 == spam + 1
#print(spam)

