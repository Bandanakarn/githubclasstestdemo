
# #write a function to show use case of combination of return value and argument type
# def adding(a,b,c,d=1):
#     print("hi this is inside fucntion with arguement")
#     print(a,b,c,d)
#     return "sum is", a+b+c+d

# val=5 
# def adding():
#     sum=5+9
#     print(sum)
#     multiply=5*9
#     # test=val
#     # test=test+4
#     print("sum is from function",val)
#     print(sum,a+b)
#     print(multiply,a*b)
#     return(sum, multiply)
# #ctrl kc or\ /
# a=5
# b=6
# c,d=adding()
# print(c,d)
# val=val+4
# print("val is",val)
# print("val is",val+1)
# adding()
# # local variable and global variable
# #write a function to print even numbers between 2 and 50 also perform addition of those even numbers
# for even_number in range(2,50,2):
#     print(even_number, end=' ')
#     total=0
#     for number in range(2,51):
#         if(number % 2 == 0):
            
#             total = total + number

# print("The Sum of Even Numbers from 2 to 50",total)

# # Write a function to perform addition between 2 to 50 odd numbers
# sum=0

# for odd_number in range(2,51):
#     if(odd_number % 2 !=0):
#         sum=sum+odd_number
# print("The sum of odd numbers between 2 and 50",sum)

# def find_even(a,b):
#     sum=0
#     for i in range(a,b):
#         if i%2==0:
#             sum+=i
#     print("sum is",sum)
# find_even(2,51)

# #write a program to check if given number is prime or not
# def prim(a):
#     f=False
#     if a==1: 
#         print("not prime")
#     elif a>1:
#         for i in range(2,a):
#             if (a%i)==0:
#                 f=True
#                 break
#         if a==f:
#             print("no")
#         else:
#             print("prime")
# prim(5)



# def is_prime_trial_division(n):

#     if n <= 1:
#         return False
    
#     for i in range(2, int(n**0.5)+1):
       
#         if n % i == 0:
#             return False
    
#     return True
# if is_prime_trial_division(10):
#     print("prime")
# else:
#     print("not prime")


# print(is_prime_trial_division(11))


# #write a program to give the multiplication table of 5, 10, 17
# def multiplication(a):
#     for i in range(1,11):
#         b=i*a
#         print(i,"*",a,"=",b)
#         print(f"{a}*{i}={a*i}")
# multiplication(5)
# multiplication(10)
# multiplication(17)

# my_str="abc this is my abc string"
# print(my_str)
# print(my_str[5])
# #slicing
# print(my_str[4:19])
# #reversing
# print(my_str[::-1])
# # string-collection of character
# user_inputs=input("Enter your name:")
# print(f"Hi {user_inputs} Nice to meet you")
# print(type(user_inputs))
# #type casting

# #here we are using upper case 
# print("Hi {} Nice to meet you".format(user_inputs))
# print(f"hi {user_inputs.upper()} your name has {len(user_inputs)}")

# message="Hi Piaiaq"
# message_replace=message.replace("Hi","Hello")
# print(message)
# print(message_replace)

# #write a program that prompts the user to enter their name and their favorite color. Then create a 
# #message that combines their ame and favouirte color to form a cpersonalized message
# user_nm=input("Enter your name")
# user_color=input("Enter your favourite color")
# print("Hi {}! Your favorite color is {}.".format(user_nm,user_color))

# #ask user to enter sentence and give in length
# user_sentence=input("Enter sentence")
# splitted=user_sentence.split()
# print(len(splitted))

# #enter full name and last name, convert to uppercase and in reverse with comman between first and last name but actually do tuladhar priyanka
# meow=input("What is your first name and last name ?")
# fname,lname = meow.split(" ")
# print("{} {}".format(lname.upper(),fname.upper()))
# # uppy=meow.upper()
# # name_halfing=uppy.split()
# # print(name_halfing[::-1])

# #take sneetnce as input and transforms all the specific word into another specific word

# abc=input("enter sentence please")
# abcabc=input("enter word to be replaced")
# abcabcabc=input("enter replacement word")

# op=abc.replace(abcabc,abcabcabc)
# print(op)


# #list
# my_list=["mango","lichi","tomato","medicine"]
#           #0         1        2       3
# print(my_list[1])
# print(my_list[:1]) #slicing
# print(my_list[-4])

# my_list.append("potato")
# my_list.insert(0,"potato")
# my_list.remove("lichi")
# forgot=my_list.pop(3)
# print(f"I forgot:{forgot}")
# print(my_list)

# my_list.sort(reverse=True)
# print(my_list)
# my_list1=[1,2,3,4,0,4]
# print(my_list+my_list1)



# numbers=[1,3,5,7,9]
# print(numbers[1])
# numbers.insert(2,10)
# numbers.append(12)
# numbers.remove(5)
# print(numbers)

# sliced_list=numbers[1:4]
# print(sliced_list)

# combined_list=numbers+sliced_list
# #check if the number 8 is present in the combined_list and print

# #sort ascednging list

# print(combined_list)











# #Creating a function 
# def my_function():
#      print("Hello from a function")
# # #calling a function
# my_function()
# #Arguments-args information can be passed into functions as arguments

# #are specified under the function name inside() can add as many with separation from comma
# #here the function with one argument (fname)
# def my_function(fname):
#     print(fname + "Refsnes")

# my_function("Email")
# my_function("Tobias")
# my_function("linus")

# def my_function(fname, lname):
#      print(fname + " " +lname)

# my_function("Emil","Refsnes")

# def my_function(*kids):
#      print("The youngest child is " + kids[2])

# my_function("Emil","Tobias","Linus")

# def my_function(kid1,kid2,kid3):
#      print("The youngest child is "+kid3)

# my_function(kid1="Emil", kid2="Tobias", kid3="Linus")

# def my_function(**kid):
#      print("His last name is")






# #day 3 week 5

# my_tuple=(1,2,3,4,5,6)
# my_tuple2=(5,6,7,8,9,9)
# print(my_tuple+my_tuple2)
# print(my_tuple[0])

# print(len(my_tuple2))
# count_1=my_tuple.count(1)
# print(count_1)

# s_tuple=sorted(my_tuple,reverse=True)
# print(s_tuple)
# a_tuple=tuple(sorted(my_tuple2,reverse=False))
# print(type(s_tuple))
# print(type(a_tuple))

# print(2 in my_tuple2)  # check for 2

# print(max(my_tuple))
# print(min(my_tuple))

# # Answer the following questions based on your understanding of tuples and their operations.
# #1. Define a tuple named my_tuple with the following elements: 10,20, 'a', 'b', True.
# my_tuple=[10,20,'a','b',True]

# # 2. Write the code to access and print the third element of the tuple my_tuple.
# print(my_tuple[2])
# # 3. Concatenate two tuples: tuple1 with elements (1, 2, 3) and tuple2 with elements ('x', 'y', 'z'). Store the result in a new tuple called concatenated_tuple.
# tuple1=[1,2,3]
# tuple2=['x','y','z']
# concatenated_tuple=tuple1+tuple2
# # 4. Write a Python code snippet to repeat the tuple my_tuple three times and store the result in a new tuple named repeated_tuple.
# repeated_tuple=my_tuple*3
# print(repeated_tuple)
# # 5. Determine the length of the tuple concatenated_tuple using a built-in function and print the result.
# print(len(concatenated_tuple))
# # 6. Perform slicing on the tuple my_tuple to extract a new tuple with elements 'a', 'b', and True. Store the result in a variable called sliced_tuple.
# slicedtuple=my_tuple[2:]
# print(concatenated_tuple)
# print(slicedtuple)
# print(my_tuple)

# # dictonary
# # it has key value
# my_i={
#      "name":"pi",
#      "age":"88",
#      "address":"NP",
#      "avacado":{
#           "nagarikta":8204920340,
#           "abc":567890
#      }
# }
# print(my_i)
# my_i["age"]=21#to modify the elements in the dict
# #buffer remove delete will delete nai, accessing a term inside avacado-abc, enter a new term in the dict and try pop



# # write a program to show multiplication table of first 20 prime numbers using nested for loop.
# # is wrong def prime(no):
   
# #     for i in range(2,no+1):
# #         k=0
# #         for j in range(int(k**0.5)+1):
# #             if (no % i) ==0:
# #                 k=k+1
# #                 return False
               
#         return True
# prime_list=[]   
# count=0
# no=1
# while count<20:
#     if prime(no):
#          prime_list.append(no)
#          count=count+1
#          for i in range(1,11):
#               b=i*no
#               print(i,"*",no,"=",b)      
#     no=no+1
#     print(":::::::::::::::::::::::::::::::::")

# prime=0
# number=10
# for i in range (2,number):
#      if number%-i==0:
#           print("Not prime")
#           break
#      else:
#           print("prime")
# for j in range(20,30):
#     for i in range(2,j):
#         if j%i==0:
#             print(j,"Not prime")
#             break
#     else:
#         print(j,"prime")
#         break


# #write a program to find the simple interest
# #write a prgram to find perimeter of rectangular grounf
# # How to find volume of iregular body
# #WAP to calculate the volume of a cube
# #WAP to find square root of a number
# #WAP to find error percentage


# # y=input("enter the square root number to be done")
# # print(y**1/5)
# #take a str as an input and check whether the string is rishab or not\
# u=input("Enter a string")
# if(u=="rishabb"):
#      print("ya sure")
# else:
#      print("no")

#WAP to find area of a circle with radius 7.5, 8.97, 20.39,100,129,139,600,1000,5.6,8.9,12.7,11.12,12.13

def radius_find(radius):
     pie=3.14
     for i in range(len(radius)):
          area=pie*radius[i]*radius[i]
          print(area)

radius=[7.5, 8.97, 20.39,100,129,139,600,1000,5.6,8.9,12.7,11.12,12.13]
radius_find(radius)

for pi in range(19):
     print(pi)

for i in(0,3,4,5):
     print(1)

for i in range(2,20,6): #here 6 is incremental, and 2 is for starting from
     print(i)

list_a=[1,2,2,3,3,3]
list_b=list_a
list_b[0]="ram"
print ("list a",list_a)
print("list_b",list_b)
#notice the difference between the without and with the deepcopy
import copy
list_a=[1,2,2,3,3,3]
list_b=copy.deepcopy(list_a)
list_b[0]="ram"
print ("list a",list_a)
print("list_b",list_b)

import copy
a=[5,6,7]
b=copy.deepcopy(a)
b[0]=8
print(a)
print(b)

#Dictonary

#
fruits=["Banana","abc"]
for index,value in enumerate(fruits):
     print(index+1,value)

#to access each char of a string
text="hello ram"
for abc in text:
     print(abc)

se={1,2,3,4}
print(type(se))

print(se)

li=[3,4,4,5,5,5,5]
print(set(li))#removes reduncay

#nested for loop
a=[3,3,4,5,6,6]
b=[8,8,8,8,8,8]
c=[5,6,7,4,3,5]
for i in range(0,6):
     for j in range(0,6):
          for k in range(0,6):
               print(i,j,k)
a=[9,9,9],[0,0,0],[1,1,1]
print(a)
for i in range(0,3):
     for j in range(0,3):
          a[i][j]=1+a[i][j]
print(a)
for i in range(0,3):
     for j in range(0,3):
          a[i][j]=i+a[i][j]
print(a)


a=[[1+a[i][j]for j in range(3)] for i in range(3)]
print(a)

lst=[2,3,4,5]
a=[x**2 for x in lst]#list comprehension
print(a)
a=[]
for x in lst:
     a.append(x**2)
print(a)

number=9
if number<0:
     print("no")
elif number==0:
     print("Zero")
elif number % 2 ==0:
     print("even")
else:
     print("odd")

               



