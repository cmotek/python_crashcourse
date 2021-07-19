people = {
	'fredfred': {
		'first_name': 'Fred',
		'last_name': 'Fred',
		'age': 54,
		'city': 'St. Louis',
	},

	'bill': {
		'first_name': 'Bill',
		'last_name': 'Bill',
		'age': 67,
		'city': 'Los Angeles', 
	},

	'doublematt': {
		'first_name': 'Matt',
		'last_name': 'Matt',
		'age': 98,
		'city': 'Milwaukee',
	},

}

for username, details in people.items():
	print(f"\nUsername: {username}")
	fullname = f"{details['first_name']} {details['last_name']}"
	print(f"\nFull name: {fullname}")
	print(f"Age: {details['age']} ")
	print(f"City of Residence: {details['city']}")