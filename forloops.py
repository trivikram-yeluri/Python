#for loops

my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num)

#--------> Print Even and Odd Numbers

for num in my_list:
    if num % 2 == 0:
        print(f"Even Number: {num}")
    else:
        print(f"Odd Number: {num}")

#---------> Sum of numbers in the list

list_sum = 0
for num in my_list:
    list_sum = list_sum + num
print(list_sum)

for num in my_list:
    print("Hello")

my_string = "Hello World"
for letter in my_string:
    print(letter)

for letter in "Hello World!":
    print(letter)

for _ in my_list:
    print("Cool!")

#Tuple

my_tuple = [(1,2),(3,4),(5,6),(7,8)]
for num in my_tuple:
    print(num)

for a,b in my_tuple:
    print(a)

for a,b in my_tuple:
    print(b)

for x,y in my_tuple:
    print(a,b)

for x,y in my_tuple:
    print(a+b)

for x,y in my_tuple:
    print(x,y)

#Dictionary

my_dict = {"key1": 1, "key2": 2, "key3": 3}
for key in my_dict:
    print(key)

for item in my_dict.items():
    print(item)

for key,value in my_dict.items():
    print(key, value)

for value in my_dict.values():
    print(value)

