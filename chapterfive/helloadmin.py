usernames = ['FrodoBaggins', 'admin', 'Notenoughicecream77', 'Vegeta', 'Vegeta28']

if usernames:
	for user in usernames:
		if user == 'admin':
			print(f"Hello {user}, would you like to see a status report?")
		else:
			print(f"Hello {user}, thank you for loggin in again!")
else:
	print("We need to find some users!")

