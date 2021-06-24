current_users = ['FrodoBaggins', 'Skeebo', 'Notenoughicecream77', 'Vegeta', 'SizzleJones']
lowercase_users = ['frodoBaggins', 'skeebo', 'notenoughicecream77', 'vegeta', 'sizzleJones']
new_users = ['Tesla', 'FrazzleJones', 'BilboBaggins', 'SizzleJones', 'skeebo']

for user in new_users:
	if user in lowercase_users:
		print(f"{user}, there is a case sensitive issue with this one, bro!")
	elif user in current_users:
		print(f"{user}, you're going to need a new username! This one is taken!")
	else:
		print(f"{user}, this username is available!")