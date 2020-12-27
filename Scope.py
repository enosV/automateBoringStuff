#Global variables can't be used in the global scope
def spam():
    eggs = 99
spam()
print(eggs) #reason why eggs is not defined is because its being called after being destroyed from when the def executes it (run this on pythontutor.com to see it stepbystep)

#######################################################################################
def spam(): #first local scope because that's what we initially called
    eggs = 99
    bacon() #this calls the def bacon() function
    print(eggs) #here it's local and cane be called

def bacon(): #this now creates a 2nd local scope
    ham = 101
    eggs = 0 # these eggs are NOT the same as the eggs under the spam() function

spam()

########################################################################################

