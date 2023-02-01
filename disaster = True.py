# disaster = True
# if disaster:
#     print("Woe!")
# else:
#     print("Whee!")


# furry = True
# small = True
# if furry:
#     if small:
#         print("It's a cat.")
#     else:
#         print("It's a bear!")
# else:
#     if small:
#         print("It's a skink!")
#     else:
#         print("It's a human")

# color = "puce"
# if color == "red":
#     print("It's a tomato")
# elif color == "green":
#     print("It's a green pepper")
# elif color == "bee purple":
#     print("I do not know what it is, but only bees can see it")
# else:
#     print("I have never heard of such color - puce")

# some_list = [1, 2, 3, 4]
# if some_list:
#     print("There is something in the list")
# else:
#     print("Hey. The list is empty!")

#  ITERIROVANIJE:
# rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
# current = 0
# # while current < len(rabbits):
# #     print(rabbits[current])
# #     current += 1
# for rabbit in rabbits:
#     print(rabbit)

# word = 'cat'
# for letter in word:
#     print(letter)

# accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
#               'person': 'Col.Mustard'}
# for card in accusation.keys():
#     print(card)
# for value in accusation.values():
#     print(value)
# for item in accusation.items():
#     print(item)
# for card, contents in accusation.items():
#     print('Card', card, 'has the contents', contents)

############################################################

# funcija ZIP:
# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['coffee', 'tea', 'beer']
# desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#     print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
ef_list = list(zip(english, french))
print(ef_list)
ef_dict = dict(zip(english, french))
print(ef_dict)
# for item in ef_dict.items():
#     print(item)
current = 0
while current < len(ef_list):
    print(ef_list[current])
    current += 1
