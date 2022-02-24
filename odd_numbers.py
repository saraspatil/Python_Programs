# odd numbers :-  a number which is not divisible by 2 is called odd number.

# Given a list of numbers, write a Python program to print all odd numbers in given list.
list1 = [2, 7, 5, 64, 14]

#usign list comprehension
print([i for i in list1 if i % 2 != 0])

# using for loop
print('list of odd numbers:')
for i in list1:
    if i % 2 != 0:
        print(i, end=' ')

# using while loop
print('list of odd numbers:')
i = 0
while i < len(list1):
    if list1[i] % 2 != 0:
        print(list1[i], end=' ')
    i += 1

# using lambda function
odd_numbers = list(filter(lambda x: x % 2 != 0, list1))
print(odd_numbers)

# output
list of odd numbers: [7, 5]

***********************************************************************
# Python program to print all odd numbers in a range(4,15)

# using for loop
print('odd numbers:', end=' ')
for i in range(4, 15):
    if i % 2 != 0:
        print(i, end=' ')

# using lambda function
print(list(filter(lambda x: x % 2 != 0, range(4, 15))))

# using list comprehension
print([i for i in range(4,15) if i % 2 != 0])

# output
[5, 7, 9, 11, 13]
