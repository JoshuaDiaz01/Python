# # 1
# def countdown (num):
#     output = []
#     for i in range (num,-1,-1):
#         output.append(i)
#     return output
# print(countdown(5))

# #2
# def print_and_return(list):
#     print(list[0])
#     return list[1]
# print(print_and_return([1,2]))

# #3
# def first_plus_length(list):
#     return list[0] + len(list)
# print (first_plus_length([1,2,3,4,5]))

# #4
# def values_greater_than_second(list):
#     if len(list)<2:
#         return False
#     output=[]
#     for i in range(0,len(list)):
#         if list[i] > list[1]:
#             output.append(list[i])
#     print(len(output))
#     return output

# print(values_greater_than_second[5,2,3,2,1,4])
# print(values_greater_than_second[3])

#5 
# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def size_and_length(size,value):
    output = []
    for i in range(0,size):
        output.append(value)
    return output
print(size_and_length(4,7))
print(size_and_length(2,7))

