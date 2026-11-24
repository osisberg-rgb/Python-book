#6.3-4 make a dictionary

# programming_words = {'encaptiolation': 'isolation code', 'design-pattern': 'diffent design', 'builder': 'making something'}

# for key, value in programming_words.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")



#6.5
# rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china', 'mississippi': 'united states', 'ganges': 'india'}
# for river in rivers:
#     print(f"\nThe {river.title()} runs through {rivers[river].title()}."),

# for river in rivers.keys():
#     print(f"\nThe {river.title()}")

# for country in rivers.values():
#     print(f"\nThe {country.title()}")


#6.6

# favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
# for name, language in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite language is {language.title()}.")


#6.7

people = {
    "roommate1": {
        "first": "Oscar",
        "last": "Isberg",
        "age": "22"
    },
    "roomate2": {
        "first": "Rian",
        "last": "Graham",
        "age": "20"
    },
    "roommate3": {
        "first": "max",
        "last": "hacther",
        "age": "20"
    }
}

for roommate, info in people.items():
    fullName = f"{info['first']} {info['last']}"
    age = f"{info['age']}"

    print(f"{roommate}: {fullName} and he is {age} years old")
    