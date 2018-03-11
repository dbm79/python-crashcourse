favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel']
    }

#print("Sarah's favorite language is: " + favorite_languages['sarah'].title() + ".")

#This will sort the keys then print
#for name in sorted(favorite_languages.keys()):
#    print(name.title())

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())
