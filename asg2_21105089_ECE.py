print('Question 1')
### writing given string
given_string='Python is a case sensitive language'
# printing the length of given string 
print('Length of given string = ',len(given_string))
#reversing the string 
print('Reversing the given string = ',given_string[::-1])
#slicing a part from string 
sliced_string=given_string[10:26]
#printing the sliced part
print('Using slice function-',sliced_string)
#replacing and printing new string
new_string= given_string.replace('a case sensitive','object oriented')
print(new_string)
#printing index of "a" from given_string
print(given_string.index('a'))
#Removing the white spaces
print(given_string.replace(' ',''))

print('Question 2')

print('Using string formatting')
name='Adarsh Mandloi'
sid= 21105089
department='ECE'
CGPA=9.9
print('Hey, %s Here!'%name)
print('My SID is %d '%sid)
print('I am from %s department and my CGPA is %f'%(department,CGPA))

print('Question 3')

###Bitwise operators
a=56
b=10
print(' a&b :', a & b)
print(' a|b :', a | b)
print(' a^b :', a ^ b)
###Left shift  both a and b with 2 bits.
print('a<<2 : ', a<<2)
print('b<<2 : ', b<<2)
###Right shift a with 2 bits and b with 4 bits.
print('a>>2 : ', a>>2)
print('b>>2 : ', b>>2)

print('Question 4')

###the greatest of three numbers entered by the user

num1=input('Enter num1: ')
num2=input('Enter num2: ')
num3=input('Enter num3: ')

###Finding the highest number among the 3 number entered by user
if num1>num2 and num1>num3:
    print('Highest number: ',num1)
elif num2>num1 and num2>num3:
    print('Highest number: ',num2)
else:
   print('Highest number: ',num3)

print('Question 5')

###Find the word "name" in the string entered by the user
input_string=input('Enter the string: ')
if 'name' in input_string:
    print('Yes')
else:
    print('No')

print('Question 6')

###Checking condition to form a triangle
a = int(input("Enter  length1 : ")) 
b = int(input("Enter  length2 : "))
c = int(input("Enter  length3 : "))

if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")

    

    
    








