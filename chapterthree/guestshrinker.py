guestlist = ['Barack Obama', 'Stanley Kubrick', 'Thomas Pynchon']


print("This new dinner table, I have, however, now seats 120 dinner guests.")

guestlist.insert(0, 'Bill Murray')
guestlist.insert(2, 'Stephen King')
guestlist.append('Kim Kardashian')

message = (f"How does McDonalds sound, {guestlist[0]}?")
print(message)
message = (f"How does McDonalds sound, {guestlist[1]}?")
print(message)
message = (f"How does McDonalds sound, {guestlist[2]}?")
print(message)
message = (f"How does McDonalds sound, {guestlist[3]}?")
print(message)
message = (f"How does McDonalds sound, {guestlist[4]}?")
print(message)
message = (f"How does McDonalds sound, {guestlist[5]}?")
print(message)

print("Unfortunately, I only have enough Chicken McNuggets for two guests.")

print(f"Sorry, {guestlist[0]}, no Chicken McNuggets for you.")
guestlist.pop(0)
print(f"Sorry, {guestlist[0]}, no Chicken McNuggets for you.")
guestlist.pop(0)
print(f"Sorry, {guestlist[1]}, no Chicken McNuggets for you.")
guestlist.pop(1)
print(f"Sorry, {guestlist[1]}, no Chicken McNuggets for you.")
guestlist.pop(1)

print(f"You made the cut {guestlist[0]}, enjoy your McNuggets.")
print(f"You made the cut {guestlist[1]}, enjoy your McNuggets.")

del guestlist[0]
del guestlist[0]

print(guestlist)


