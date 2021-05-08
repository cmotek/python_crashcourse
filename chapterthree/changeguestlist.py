guestlist = ['Barack Obama', 'Stanley Kubrick', 'Thomas Pynchon']


message = (f"How does McDonalds sound, {guestlist[0]}?")
print(message)
message = (f"How does McDonalds sound, {guestlist[1]}?")
print(message)
message = (f"How does McDonalds sound, {guestlist[2]}?")
print(message)

print("Barack said he can't make it to McDonalds.")

newguest = "Yadier Molina"
guestlist.pop(0)
guestlist.insert(2, newguest)

message = (f"How does McDonalds sound, {guestlist[0]}?")
print(message)
message = (f"How does McDonalds sound, {guestlist[1]}?")
print(message)
message = (f"How does McDonalds sound, {guestlist[2]}?")
print(message)
