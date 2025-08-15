#Write a program to take ten numbers as input from the user
#and add it to a list. Calculate and print the sum of all the numbers in the list.
# count=0
# list=[]
# while count<10:
#     numbers=int(input("Enter a number: "))
#     list.append(numbers)
#     count=count+1
# num1=0
# for i in range(10):
#     num1= num1+list[i]
# print(num1)
# sum=0
# for num in list:
#     sum+=num
# print(sum)


#Write a Python program to check if a list is empty or not.
# list=[1,2]
# v=len(list)
# if v>0:
#     print("The list is not empty")
# else:
#     print("The list is empty")


#Write a Python program to print the odd numbers from a list of numbers.
list=[1,3,2,4,4,5]
v=len(list)
for i in list:
    if i%2!=0:
        print(i)
    else:
        continue