def spam():
    #global eggs
    print(eggs) #eggs is local
eggs = 42 #eggs is global but python checks to see if you have one in a local variable, which it does, you have to tell python "global eggs" on line 2 to force it ignore the local variable
spam()