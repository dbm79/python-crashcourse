favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

print("Sarah's favorite language is: " + favorite_languages['sarah'].title() + ".")

for name in favorite_languages.keys():
    print(name.title())
