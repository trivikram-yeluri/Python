#simple function programs

def even_number():
    print("Even Number, It will print Even Number")
    print("This is second line.")

even_number()

def even_number():
    return "Hello World"
result = even_number()
print(result)
print(result)


def even_number(a,b):
    print(a+b)
    print(a*b)
    print(a%b)
even_number(10,20)

def even_number(a,b):
    return a + b
even = even_number(10,20)
print(even)  

def even_number(a=10,b=20):
    return a + b

even = even_number(100,3423)
print(even)

def even_numbers(num_list):

    even_result = []
    for number in num_list:
        if number % 2 == 0:
            even_result.append(number)
        else:
            pass
    return even_result
result = even_numbers([1,3,5,3,5,8,4,8,0,1])
print(result)



#sum of all step 2 value in the list

def sum_step2(list):
    return sum(list[::2])
numbers = [1,2,3,4,5,6,7,8,9,10]
result = sum_step2(numbers)
print(result)

#Tuples unpacking using functions

work_hours = [("Ben",100),("Sam",150),("Tom",300),("Pam", 450),("Doy",240)]

def employee_award(work_hours):
    current_hours = 0
    emp_name = ''

    for name,hours in work_hours:
        if hours > current_hours:
            current_hours = hours
            emp_name = name
        else:
            pass
    return emp_name,current_hours

result = employee_award(work_hours)
print(result)


# args and kwargs

def number(*args):
    return sum(args) * 0.05
result = number(10,20)
print(result)

def keywords(**kwargs):
    return kwargs
result = keywords(food='eggs', fruit='apple', animal='cat')
print(result)

def numbers(*args):
    print(args)
    print("My nubmer is : {}".format(args[0]))
numbers(10,20,32,49,45,90)

def sample_kwds(**kwargs):
    print(kwargs)
    print("My fruit is {}".format(kwargs['fruit']))
sample_kwds(food='Eggs', fruit='Orange', animal='cat')


def both_args_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I have {} {}".format(args[0],kwargs['fruit']))
both_args_kwargs(10,23,54,13,fruit='Oranges',food='eggs')
