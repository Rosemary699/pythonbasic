# # 3-4
# guests = ['Weiwei Weng', 'Nini Cao', 'Hally', 'Kevin', 'Chelsy', 'Nikky', 'Cindy']
# for guest in guests:
#     print(f"Dear {guest}! Welcome to our house warming!")
#
# # 3-5
# # (1)
# guests.append('Iris')
# print()
# for guest in guests:
#     print(f"Dear {guest}! Welcome to our house warming!")
#
# # (2)(3)
# guests[2] = 'Vivian'
# print()
# for guest in guests:
#     print(f"Dear {guest}! Welcome to our house warming!")
#
# # 3-6
# # (1)
# guests.append('Mary')
# guests.append('Rose')
# guests.append('Jerry')
# print()
# for guest in guests:
#     print(f"Dear {guest}! Welcome to our house warming!")
#
# # (2)
# guests.insert(0, 'Tom')
# print()
# for guest in guests:
#     print(f"Dear {guest}! Welcome to our house warming!")
#
# # (3)
# guests.insert(5, 'Cherry')
# print()
# for guest in guests:
#     print(f"Dear {guest}! Welcome to our house warming!")
#
# # (4)
# guests.append('Rebecca')
# print()
# for guest in guests:
#     print(f"Dear {guest}! Welcome to our house warming!")
#
# # 3-7
# # (1)
# print()
# for guest in guests:
#     print(
#         f"Dear {guest}! Since my bigger dinner table cannot arrive on time, only 2 guests can be invited to my house warming")
#
# # (2)
# print(guests)
# canceled_guest = []
# # guests_not_invited=['Tom','Vivian', 'Kevin', 'Cherry', 'Chelsy', 'Nikky', 'Cindy', 'Iris', 'Mary', 'Rose', 'Jerry', 'Rebecca']
# cancel = guests.pop()
# canceled_guest.append(cancel)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# print(canceled_guest)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# print(canceled_guest)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# print(canceled_guest)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# print(canceled_guest)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# print(canceled_guest)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# print(canceled_guest)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# print(canceled_guest)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# print(canceled_guest)
# cancel = guests.pop()
# canceled_guest.append(cancel)
# cancel = guests.pop(0)
# canceled_guest.append(cancel)
# print(canceled_guest)
#
# # guests.pop()
# # guests.pop()
# # guests.pop()
# # guests.pop()
# # guests.pop()
# # guests.pop()
# # guests.pop()
# # guests.pop()
# # guests.pop()
# # guests.pop()
# # guests.pop(0)
# # print(guests)
# for not_invited in canceled_guest:
#     print(f"Dear {not_invited}! I'm sorry you are not being invited.")
#
# # (3)
# invited = ['Weiwei Weng', 'Nini Cao']
# print()
# for invited_guest in invited:
#     print(f"Dear {invited_guest}, you are still invited!")
#
# #(4)
# print()
# print(guests)
# del guests[0]
# del guests[0]
# print(guests)

# 3-8
# (1)
# visit = ['Greece', 'New Zealand', 'Japan', 'Peru', 'Swissland']
#
# #(2)
# print("Original Order:")
# print(visit)
#
# #(3)
# print("Alphabetical Order:")
# print(sorted(visit))
#
# #(4)
# print("Still Original Order:")
# print (visit)
#
# #(5)
# print("Reverse Alphabetical Order:")
# print(sorted(visit, reverse=True))
#
# #(6)
# print("Still Orginal Order:")
# print (visit)
# #(7)
# print("Reverse Order:")
# visit.reverse()
# print(visit)
# #(8)
# print("Reverse Order Again:")
# visit.reverse()
# print(visit)
# #(9)
# print("Sorted Again:")
# print(sorted(visit))
# #10
# print("Sorted in Alphabetical Again")
# print(sorted(visit, reverse=True))

# 4-2
# (1)
# animals = ['cat', 'tiger', 'lion']
# print("Statement for Each Animal:")
# for animal in animals:
#     print(f"A {animal} make a great pet!")

# (2)
# print("Add a Lin in Statement for Each Animal:")
# for animal in animals:
#     print(f"A {animal} make a great pet!Any of these animals would make a great pet.")

# 4-10
# Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# animals = ['cat', 'tiger', 'lion', 'dog', 'rabbit', 'fish', 'bird']

# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# print(animals[:3])

# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# print(animals[2:5])

# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.
# print(animals[-3:])

# 4-11.
# My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# pizzas =  ['Greek Pizza', 'Neapolitan Pizza', 'Mexican Pizza', 'Chicago Pizza', 'California Pizza']
# friend_pizzas = ['Greek Pizza', 'Neapolitan Pizza', 'Mexican Pizza', 'Chicago Pizza', 'California Pizza']

# • Add a new pizza to the original list.
# pizzas.append('Detroit Pizza')
# print(pizzas)

# • Add a different pizza to the list friend_pizzas.
# friend_pizzas.append('New York-Style Pizza')
# print (friend_pizzas)

# • Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.
# print('My favorite pizzas are:')
# for x in pizzas:
#     print('\t-'+x)
# print("\n My friend's favorite pizzas are:")
# for y in friend_pizzas:
#     print('\t-'+y)

# 4-12
# More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

# my_favorite_foods = ['hairy crab', 'bamboo soup', 'hotpot', 'cold noodles']
# for food in my_favorite_foods:
#     print(f"my favorite foods is {food}.")

# 6-5
# Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# rivers = {'yellow river': 'China', 'hudson': 'usa', 'volga': 'russia', 'rhine river': 'germany', 'seine': 'france'}

# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# for river, country in rivers.items():
#     if country == 'usa':
#         print(f'The {river.title()} runs through {country.upper()}.')
#     else:
#         print(f'The {river.title()} runs through {country.title()}.')

# • Use a loop to print the name of each river included in the dictionary.
# print('***********************************************************')
# print('The name of each river is:')
# for river in rivers.keys():
#     print ('\t',river.title())

# • Use a loop to print the name of each country included in the dictionary.
# print('***********************************************************')
# print('The name of each country is:')
# for country in rivers.values():
#     if country == 'usa':
#         print(f" {country.upper()}", end = ';')
#     else:
#         print (f" {country.title()}", end = ';')

# 6-11
# Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary.
# Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city.
# print('***********************************************************')
# cities = {'new york': {'country': 'usa', 'population': '19.45', 'fact': 'the big apple'},
#           'shanghai': {'country': 'china', 'population': '24.28', 'fact': 'the magic'},
#           'tokyo': {'country': 'japan', 'population': '9.27', 'fact': 'the fashion'},
#           'amsterdam': {'country': 'holland', 'population': '0.82', 'fact': 'the windmill'}}

# The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.
# CITY is know as FACT city in COUNTRY with the POPULATION.
# for city, info in cities.items():
#     print(info['country'].upper())
#     # print(city)
#     # print(info)
#     if info['country'] == 'usa':
#         print(
#             f"{city.title()} is known as {info['fact'].upper()} city in {info['country'].upper()} with the population of {info['population']} million.")
#     else:
#         print(
#             f"{city.title()} is known as {info['fact'].upper()} city in {info['country'].title()} with the population of {info['population']} million.")

# multiplication table 1-10
# for num1 in range(1, 11):
#     for num2 in range(1, 11):
#         for num3 in range(1,11):
#             print(f"{num1}*{num2}*{num3}={num1 * num2 * num3}")


