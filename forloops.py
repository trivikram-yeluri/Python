# #for loops

# my_list = [1,2,3,4,5,6,7,8,9,10]

# for num in my_list:
#     print(num)

# #--------> Print Even and Odd Numbers

# for num in my_list:
#     if num % 2 == 0:
#         print(f"Even Number: {num}")
#     else:
#         print(f"Odd Number: {num}")

# #---------> Sum of numbers in the list

# list_sum = 0
# for num in my_list:
#     list_sum = list_sum + num
# print(list_sum)

# for num in my_list:
#     print("Hello")

# my_string = "Hello World"
# for letter in my_string:
#     print(letter)

# for letter in "Hello World!":
#     print(letter)

# for _ in my_list:
#     print("Cool!")

# #Tuple

# my_tuple = [(1,2),(3,4),(5,6),(7,8)]
# for num in my_tuple:
#     print(num)

# for a,b in my_tuple:
#     print(a)

# for a,b in my_tuple:
#     print(b)

# for x,y in my_tuple:
#     print(a,b)

# for x,y in my_tuple:
#     print(a+b)

# for x,y in my_tuple:
#     print(x,y)

# #Dictionary

# my_dict = {"key1": 1, "key2": 2, "key3": 3}
# for key in my_dict:
#     print(key)

# for item in my_dict.items():
#     print(item)

# for key,value in my_dict.items():
#     print(key, value)

# for value in my_dict.values():
#     print(value)

# example = 'Hello World!'
# for i in example:
#     print(i, end="*")

##For loop in a list

# languages = ["Java", "HTML", "Python", "ruby"]
# for i in languages:
#     print(i, end=",")

##Find the avg of list of numbers
# list_sum = [23,54,13,54,34,75,23,43]
# length = len(list_sum)
# sum = 0
# for i in list_sum:
#     sum+=i
# avg = sum/length
# print(avg)

##find the avg of tuples of numbers
# my_tuple = (211,43,54,2,43,65,245)
# sum = 0
# for i in my_tuple:
#     sum+=i
# print("Average :", sum/len(my_tuple))

# for i in range(1,10):
#     print(i, end=" ")

# for i in range(0,11,2):
#     print(i,end=" ")

##Print a table of a given number

# number = int(input("Please enter a number : "))

# for i in range(1,11):
#     mul = number * i
#     print(number, "*", i, "=", mul)

# company = ["Google","Apple","Microsoft","Netflix","Tesla"]
# for i in company:
#     print("We will print all the letters in ",i)
#     for letter in i:
#         print(letter)

# list = ["Tesla", "SpaceX", "OpenAI", "Neuralink", "The Boring company"]
# for i in range(len(list)):
#     print("Hello ",list[i])

##for loop with else clause

# for i in range(0,11,2):
#     print(i)
# else:
#     print("loop has completed execution")

# for i in range(11):
#     if i == 6:
#         break
#     print(i)

# for i in range(11):
#     if i == 6:
#         continue
#     print(i)

##program to display the total goals a player has scored

player_name = "Ronaldo"
goals = {"Messi" : 8, "Bernat" : 6, "Ronaldo" : 7, "Carmelo" : 4}

for player in goals:
    if player == "Ronaldo":
        print(goals[player])
        break
else:
    print(f"No player found with that name {player_name}")
