def hello(name): #name is a parameter
    print('Hello ' + name)
hello ('Alice') #alice is an argument
hello ('Bob') #bob is an argument

def plusOne(number):
    return number + 1
newNumber = plusOne(5) #here we're putting plusOne with its parameter into a box called newNumber, then on the following line we print it
print(newNumber)