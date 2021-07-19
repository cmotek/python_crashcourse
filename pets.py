pets = {

	'Felix': {
		'kind': 'cat',
		'owner': 'Milton',
	},

	'Nelly': {
		'kind': 'dog',
		'owner': 'Stilton',
	},

	'Maurice': {
		'kind': 'parrot',
		'owner': 'Tyra',
	},
}

for pet, pet_details in pets.items():
	print(f"\n {pet_details['owner']}'s {pet_details['kind']}'s name is {pet}!")