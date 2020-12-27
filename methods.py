spam = ['hello', 'hi', 'howdy', 'heyyyy']
print(spam.index('heyyyy')) # this is how we print the index value in an array, if there's a duplicate, it will only print the first one on the list by default

spam = ['hello', 'hi', 'howdy', 'heyyyy']
spam.append('ahoi')
print(spam) #this will add ahoi to the end of the list (if we tried doing this in 1 line, it will None)

spam = ['hello', 'hi', 'howdy', 'heyyyy', 'ahoi']
spam.insert(2, 'hola') #this is going to insert hola into index 2 and push the rest the list to the right
print(spam)

spam = ['hello', 'hi', 'howdy', 'heyyyy', 'ahoi']
spam.remove('howdy') #this is going to remove howdy, for duplicates it will only remove the first one by default
print(spam)

spam = [2, 5, 3.14, 1, -7]
spam.sort() #sort will sort the numbers; to reverse use spam.sort(reverse=True); alphabet sorting has ascii-betical for normal, use key=str.lower.
print(spam)