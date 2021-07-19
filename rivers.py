countries_rivers = {
	'nile': 'egypt', 
	'mississippi': 'united states', 
	'amazon': 'brazil'
	}

for key, value in countries_rivers.items():
	print(f"\nThe {key.title()} river is in {value.title()}.")

for rivers in countries_rivers.keys():
	print(rivers.title())

for countries in countries_rivers.values():
	print(countries.title())