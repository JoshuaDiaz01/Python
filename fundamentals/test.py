# 4 + 5
# 31/2
# x = 9
# y = "hello"
# x * y 

# print(x)

# x = "Hello Python"
# print(x)
# y = 42
# print(y)

# x = 10
# if x > 50:
# 	print("bigger than 50")
# else:
# 	print("smaller than 50")

#--------------- Tuple
# # dog = ('Bruce', 'cocker spaniel', 19, False)
# # print(dog[0])		# output: Bruce
# # dog[1] = 'dachshund' will leed to error as you cannot modify tuple

# ---------------list
# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# ---------------Dictionary
# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

# ---------------types
# print(type(24))
# print(type(3.9))
# print(type(3j))
# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

#---------------- random # generator
# import random
# print(random.randint(2,5)) # provides a random number between 2 and 5

#----------------typecasting
# print("Hello" + 42)			# output: TypeError
# print("Hello" + str(42))		# output: Hello 42

# total = 35
# user_val = "26"
# total = total + user_val		# output: TypeError
# total = total + int(user_val)		# total will be 61

#-----------------string interpolation
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# format method:
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.

# --------------list
# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)
# # you can also have mutable lists
# ninjas = ['Rozen', 'KB', 'Oliver']
# my_list = ['4', ['list', 'in', 'a', 'list'], 987]
# empty_list = []

# # list manipulation:
# drawers = ["documents", "envelopes", "pens"]
    
# # access the drawer with index of 0 and print value
# print(drawers[0])  #prints documents
# # access the drawer with index of 1 and print value
# print(drawers[1]) #prints envelopes
# # access the drawer with index of 2 and print value
# print(drawers[2]) #prints pens
    
# # replace "documents" with "tchotchkes"
# drawers[0] = "tchotchkes"
# print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# # stores the value "tchotchkes" in a temporary variable.
# top_contents = drawers[0]

# # Replaces the value at index 1
# # with whatever value is stored at index 0
# drawers[1] = drawers[0]
# print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]


#-------------------- built ins
# my_list = [1, 'Zen', 'hi']
# print(len(my_list))
# # output
# 3


# -------------------for loops
# start at 2, end at 16, increment by 3
# for i in range(2, 16, 3):
#     print(i)

# loop through list
# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# # output: 0 abc, 1 123, 2 xyz
    
# # OR 
    
# for v in my_list:
#     print(v)
# # output: abc, 123, xyz

# count = 0
# while count <= 5:
#     print("looping - ", count)
#     count += 1

# for count in range(0,5):
#     print("looping =", count)

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")

# for val in "string":
#     if val == "i":
#         break
#     print(val)
# # output: s, t, r


# for val in "string":
#     if val == "i":
#         continue
#     print(val)
# # output: s, t, r, n, g
# # notice, no i in the output, but the loop continued after the i

#-----------------dictionaries
# defined with {}
# key:value pair, access the values with the key

#add key value pair to dictionary
# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # Adds a new key value pair for email to person
# person["email"] = "alovelace@codingdojo.com"
        
# # Changes person's "last" value to "Bobada"
# person["last"] = "Bobada"
# print(person)

# replacing key: value pair
# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # Adds a new key value pair for email to person
# person["email"] = "alovelace@codingdojo.com"
        
# person["email"] = "changedemail@gmail.com"
# print(person)

#checking for existing key in dictionary
# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# if "email" not in person:
#     person['email'] = 'wrongemail@gmail.com'
# print(person['email'])

#accessing values
# person = {"first_name": "Ada", "last_name": "Lovelace", "age": 42, "is_organ_donor": True}
# print(person["first_name"])
# full_name = person["first_name"] + " " + person["last_name"]
# print(full_name)

#deleting values
# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# capitals = {} #create an empty dictionary then add values
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"

# value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
# del capitals['dnk'] # will delete the key, and not return anything
# print(capitals)

#accessing keys with for
# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(each_key)
# output: name, language

#accessing value pairs with for
# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(my_dict[each_key])
# output: Noelle, Python

#accessing both key and value
# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#      print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#      print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#      print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# List of dictionaries
# users = [
#     {"first": "Ada", "last": "Lovelace"}, # index 0
#     {"first": "Alan", "last": "Turing"}, # index 1
#     {"first": "Eric", "last": "Idle"} # index 2
# ]
# print(users[0]['last'])
# first_user = {"first": "Ada", "last": "Lovelace"}
# print(first_user['last'])

# # Dictionary of lists
# resume_data = {
#     #        	     0           1           2
#     "skills": ["front-end", "back-end", "database"],
#     #                0           1
#     "languages": ["Python", "JavaScript"],
#     #                0              1
#     "hobbies":["rock climbing", "knitting"]
# }
# print(resume_data["skills"][1])
# print(users[2]["first"])

#print the first listed language of the second resume
resumes = [
    #        	     0           1           2
    {"skills": ["front-end", "back-end", "database"]},
    #                0           1
    {"languages": ["Python", "JavaScript"]},
    #                0              1
    {"hobbies":["rock climbing", "knitting"]},


        #        	     0           1           2
    {"skills": ["front-end", "back-end", "database"]},
    #                0           1
    {"languages": ["Python", "JavaScript"]},
    #                0              1
    {"hobbies":["rock climbing", "knitting"]},


        #        	     0           1           2
    {"skills": ["front-end", "back-end", "database"]},
    #                0           1
    {"languages": ["Python", "JavaScript"]},
    #                0              1
    {"hobbies":["rock climbing", "knitting"]}
]
print(resumes[1]['languages'][0])
#DICTIONARIES ARE ['STRING'],
#LISTS ARE JUST [NUMBER]






















