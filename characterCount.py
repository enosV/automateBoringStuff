import pprint #without this the output is withour order and ugly

message = 'it was a bright cold day in April, and the clocks were strinking thirteen.'
count = {}

for character in message.upper(): #here we added .upper to get a proper count of the letters, as by default, python counts lower/upper differently
    count.setdefault(character, 0) #without setdefault we'll get an error because we're not telling the loop where to start
    count[character] = count[character] + 1

pprint.pprint(count) #here we're calling pprint module to make the output look pretty