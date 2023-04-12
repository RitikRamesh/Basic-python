# # two types of loops are there in python : whileloop and forloop
# while loops; where we don't know when the condn will end or return false.
# # usage
# syntax

# while condition:
#     code

# num = eval(input())
# while num < 13:
#     print(num)
#     num += 1

# name = input('Enter a Name : ')
# while name != 'quit':
#     name  = input('Enter Valid Input : ')
# else:
#     print('Thanks')

# # write a while loop that prints out the even numbers from 2 to 20.

# num = 2
# while num <= 20:
#     if num % 2 == 0:
#         print(num, 'even')
#         num += 2

# num = 2
# while num <= 20:
#     print(num, 'even')
#     num += 2

# num = 1 
# while num < 21:
#     if num > 12:
#         break
#     print(num)
#     num += 1
    
# i = 1
# while i < 30:
#     if i > 12:
#         continue              here 13 value is being stuck in loop where it can't reach to print statement
#     print(i)
#     i += 1

# i = 1
# while i < 21:
#     if i == 12:
#         i += 1
#         continue
#     print(i)
#     i += 1
    

# # for loop
# syntax
# for num in range(2,21,2):
#     print(num)

# lst = ['ritik', 'ritik', 'ritik']
# # for x in lst:
# #     print(x)

# # for x in range(0,2):
# #     print(x)
    
# for i in range(len(lst)):
#     print(lst[i])

# while True:
#     i = eval(input('Enter a number : '))
#     if i < 0:
#         break
#     i **= 2
#     print(i)

# i = eval(input('Enter a number : '))    
# while i > 0:
#     i = eval(input('Enter a number : '))    
#     if i < 0:
#         break
#     i **= 2
#     print(i)

# # Q) Write a while loop that prompts the user to enter a password and keeps prompting until the correct password is entered
    
# User_pass = input('Enter a User_pass : ')
# while User_pass != '12345R@':
#     User_pass  = input('Enter Valid Input : ')
# else:
#     print('Thank You')

# Q) Write a while loop that generates a multiplication table for a number entered by the user,
# and stops when the multiplication table reaches 10

# x = eval(input("Enter a Number : "))
# i = 1
# while i > 0:
#     if i == 11:
#         break
#     y = x*i
#     print(f'{x} X {i} = {y}')
#     i += 1
    
# x = eval(input("Enter a Number : "))
# i = 1
# while i <= 10:
#     y = x * i
#     print(f'{x} X {i} = {y}')
#     i += 1

# x = eval(input('Enter a Number : '))
# i = 1
# while i <= 10:
#     print(f'{x} X {i} = {x*i}')
#     i += 1

# x = eval(input("Enter a Number : "))
# for i in range(1,11):
#    print(f'{x} X {i} = {x*i}')
   
# # Q) Write a for loop that iterates through a list of names and prints out each name with counting

# Name = ['Ritik', 'Sukhdeep', 'Paramjeet', 'Simran', 'Rahul', 'Nidhi', "Diksha"]
# for i in range(len(Name)):
#     print(i+1, Name[i])

