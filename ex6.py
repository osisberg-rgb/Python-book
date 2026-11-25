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


# #6.7

# people = {
#     "roommate1": {
#         "first": "Oscar",
#         "last": "Isberg",
#         "age": "22"
#     },
#     "roomate2": {
#         "first": "Rian",
#         "last": "Graham",
#         "age": "20"
#     },
#     "roommate3": {
#         "first": "max",
#         "last": "hacther",
#         "age": "20"
#     }
# }

# for roommate, info in people.items():
#     fullName = f"{info['first']} {info['last']}"
#     age = f"{info['age']}"

#     print(f"{roommate}: {fullName} and he is {age} years old")


#6.8 

# pet = {
#     "Dog1": {
#         "name": "sox",
#         "age": "3",
#         "race": "greyhound",
#         "owner": {
#             "name": "max",
#             "street": "728 parkway drive"
#         }
#     },
#     "Dog2": {
#         "name": "bantus",
#         "age": "3",
#         "race": "whippet",
#         "owner": {
#             "name": "oscar",
#             "street": "Greve bygade 9"
#         }
#     },
#     "Dog3": {
#         "name": "cato",
#         "age": "10",
#         "race": "great dane",
#         "owner": {
#             "name": "lotte",
#             "street": "rosenvejen 67"
#         }
#     }
# }

# for key, value in pet.items():
#     doginfo = f"{value['name']}, {value['age'], {value['race']}}"
#     owner = value['owner']
#     ownerInfo = f"{owner['name']}, {owner['street']}"
#     print(f"This is {key}, {value}, he is owned by {owner}")

#6.11
# Cities = {
#     "New_York": {
#         "Country": "USA",
#         "Population": "5m",
#         "fact": "they have good bagels"
#     },
#     "Greve": {
#         "Country": "Denmark",
#         "Population": "50.000",
#         "fact": "That is where i am from"
#     },
#     "Dallas": {
#         "Country": "USA",
#         "Population": "10m",
#         "fact": "They turned blue"
#     }
# }

# for key, value in Cities.items():
#     cityName = key
#     cityInfo = f"{cityName} is located in {value['Country']} it has a population of {value['Population']} and here is a fun fact: {value['fact']}"
#     print(f"{cityInfo}")