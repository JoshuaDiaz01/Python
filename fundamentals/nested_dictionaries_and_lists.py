#1
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# #1a
# x[1][0] = 15
# print (x)
#1b
# sports_directory['basketball'][1]= 'Bryant'
# print (sports_directory)
#1c
# sports_directory['soccer'][0]= 'Andres'
# print (sports_directory)
# 1d calling a key
# z[0]['y']= 30
# print(z)

# #2
# datalist = [
#         {'first_name' :  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# for index in range (len(datalist)):
#     for key in datalist[index]:
#         print(f"{datalist [index]}")

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3
# from array import array


# iteratedictionary2 = [
#         {'first_name' :  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iteratedictionary2(array):
#     for i in range (len(array)):
#         print(array[i].pop(key))
# iteratedictionary2

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printLocations(dictionary):
    print(f"{len(dojo['locations'])} {'locations'.upper()}")
    for i in range(len(dojo['locations'])):
        print(dojo['locations'][i])
printLocations('locations')

def printInstructors(dictionary):
    for i in range(len(dojo['instructors'])):
        print(dojo['instructors'][i])
printInstructors('dojo')



# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon



