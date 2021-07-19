favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

polling_folks = {
	'bill': 'javascript',
	'jen': 'python',
	'edward': 'ruby',
	'theodore': 'javascript'
}

for name in polling_folks.keys():
	if name in favorite_languages.keys():
		print(f"{name.title()}, you already took our poll! Thank you.")
	else:
		print(f"{name.title()}, you need to take the poll!")
