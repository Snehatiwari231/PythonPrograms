'''
name = "sneha tiwari"
print("my name is ", name)
num1 = 25
num2 = 50
addition = num1+num2
sustraction = num1-num2
multiply = num1*num2
division = num1/num2
print("Addition:",addition)
print("Sustraction",sustraction)
print("Multiply",multiply)
print("Division",division)
x=25
print("Data type of x is :", type(x))
name = input("what is your name")
print("hello", name + "!Welcome to Python")
age = input("Enter your Age")
print("your age is" +age+ "years old!")


num = int(input("Enter a Number: "))

if num % 2 == 0:
    print(f"{num} is Even")    
else:
    print(f"{num} is Odd.")   
    
    '''
#for i in range(1, 11):
 #          print(i)

    
count = 5
while count >= 1:
    print(count)
    count -= 1  
#concatenate two strings
str1 = "hello"
str2 = "world"
result = str1+ " "+str2
print(result)

my_list = [1,2,3,4,5]
my_list.append(6)
print(my_list)

my_list= [2,6,8,5]
my_list.sort()
print("Ascending:",my_list)
my_list.sort(reverse=True)
print("Descending:",my_list)

numbers = [4,4,5,6,6,7,12,3,4]
maximum = max(numbers)
minimum = min(numbers)
print("Maximum:",maximum)
print("Minimum:",minimum)



numbers = [4,4,5,6,6,7,12,3,4]
numbers=list(set(numbers))
print("without duplicate:",numbers)

#FUNCTION

def add_numbers(a, b):
    return a + b

result = add_numbers(456, 765)
print("Sum is:", result)


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))  # Output: 120





def greet(name):
    print("Hello, " + name + "!")

greet("Sneha")  # Output: Hello, Sneha!














































things = ["pen","laptop","phone","copy"]
print(things[0])
print(things[2])
num = [1,3,2,4,5,5]
num.append(7)
print(num)
num = [1,2,3,4,5,6,7,8,9]
print(num)


number = [32,43,554,76,8,23]
total = sum(number)
print("sum of elements :", total)




