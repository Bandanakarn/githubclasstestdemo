print ("hello world")
if 5 > 2:
    print("Five is greater than two!")

new_tre='hello\n'
#write a python program to print hello world 1000 times in new line
new_tre = new_tre * 1000
print(new_tre)

## what sir asked for                 print("hello"*1000)
 
#write a program to find the datatypes
#can you perform the addition of string and integer
#write a program to find the ascii value of characters priyanka
#write a program to perform the addition of 1st 20 numbers 
#write a program to show use case of boolean data type
#write a program to take input from the user and render hello <Name>
# write a program to conver string datatype to intger, int to str, float to int, int to float
#1
a="abc"
b=99
print("The datatype for a", type(a))
print("The data type for b", type(b))

#2  No, only possible after conversion

#3 
ab=['P','r','i','y','a','n','k','a']
for c in ab:
    print("The ASCII value of '"+c+"' is ",ord(c))

#4
sum=0
for d in range(1, 20):
    sum= sum+d
print(sum)

#5

#6
f=input('What is your name?')
print("hello "+f)

#7

