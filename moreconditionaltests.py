monsters = ['Vampire', 'Wolfman', 'Frankenstein', 'Halftoad']
monster = 'Godzilla'
monster_age = 1000
rodan_age = 10

print("\nWait, is the monster you're talking about, Rodan?")
print(monster == 'Rodan')

print("\nSo we're talking about a different monster than Rodan?")
print(monster != 'Rodan')

print("\nIs this monster Godzilla?")
print(monster.lower() == 'Godzilla')

print("\nIs this the correct way to spell Godzilla?")
print(monster.title() == 'Godzilla')

print("\nIs this monster less than a thousand years old?")
print(monster_age != 1000)

print("\nIs this monster a thousand years old, exactly?")
print(monster_age == 1000)

print("\nAre you sure the monster isn't less than a thousand years old?")
print(monster_age < 1000)

print("\nWhat about more than a thousand years old?")
print(monster_age > 1000)

print("\nIt could be a thousand years old or younger, correct?")
print(monster_age <= 1000)

print("\nWhat about a thousand years old or older?")
print(monster_age >= 1000)

print("\nIs Rodan less than 1000 and Godzilla more than 10 years old?")
print(rodan_age >= 10 and monster_age <= 1000)

print("\nIs Rodan less than 10 or Godzilla more than 1000 years old?")
print(rodan_age < 10 or monster_age > 1000)

print("\nAre there vampires in the monster list?")
print('Vampire' in monsters)

if monster not in monsters:
	print(f"\n{monster.title()}, you are not in our list of monsters!")


