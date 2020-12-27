myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'} #key:value pairs seperated by commas, the order does not matter unlike a list/array, and are immutable
print(myCat['size']) #here we're using the key 'size' to output the value 'fat'

print(list(myCat.keys())) #this will print a list of the keys in myCat
print(list(myCat.values())) #this will print a list of the values in myCat
print(list(myCat.items())) #this will print a list of two-item tuples in myCat


#we also put the dictionary through a for loop:
for k in myCat.keys():
    print(k)

for v in myCat.values():
    print(v)

for k, v in myCat.items():
    print(k, v)


print(myCat.get('size', 0)) #this is to check to see if there's a key in the dictionary, in case there isn't anything python will return 0 as a default value; use setdefault(key, value) to ensure a key exists, see chracterCount.py for example

