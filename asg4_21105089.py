print('Question1')
###########################################################################################################################################################
print('')


print("problem of tower of Hanoi with three disks.")
print("")
print("SOL 1. :- Solution the problem of tower of Hanoi with three disks.")
print("")
no_of_count=0
def hanoi(n, fro, to, aux):
    global no_of_count
    if n == 0:
        return
    no_of_count+=1
    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)

#calling funtion for 3 disks
hanoi(3, 'A', 'C', 'B')
print("Number of counts : %d" % (no_of_count))
print("")
###########################################################################################################################################################
print('Question2')
print('')
n=int(input('Enter the line till which you want to see pascal triangle which must be greater than 0: '))
print('With recursion')
## Defining the recursive function 

def factorial(n):
    if n==0:
        return 1
    
    return n * factorial(n-1)
for i in range(0,n):
    for x in range(0,n+1-i):
        print(" ",end='')
    for w in range(0,i+1):
        f=int(factorial(i) / (factorial(w)*factorial(i-w)))
        print(f,'',end='')
    print('')
print('With iteration')    
for l in range(n) :  
           for e in range(l,n+1):
               print(' ',end='')
           for j in range(l+1):
               a,b,c=1,1,1
               for m in range(l+1):
                   if m>0:
                       a=a*m
                       if m<=j:
                           b=b*m
                       if m<=l-j:
                           c=c*m
               print(int(a/(b*c)),end=' ')
           print()
print('')
###########################################################################################################################################################
print('Question 3')
print('')
a=int(input('enter first no. :'))  ##Getting input from user 
b=int(input('enter secod no. :'))
if b==0 :
    print('Denominator cant be 0 , error')
else :
    result=divmod(a,b)    ## calling divmod function
    print(result)
    print('\nPart a)')
    print(callable(divmod))   ## using callable function to check callability

    print('\nPart b)')
    if result[0] == 0 :   ## checking weather the values are non-zeros 
        if result[1] == 0 :
            print('both values are zero ')
    else :
       if result[1] == 0 :
            print('one value is zero')
       else :
            print('both values are non zero')    
    
    print('\nPart c)')
    lis=[result[0],result[1],4,5,6]   ##adding (4,5,6) to values and finding out values greater than 4 
    print(lis)
    set1=set()
    for i in lis :
        if i > 4 :
            print(i,end=' ')
            set1.add(i)   ## making set of the values
    print()


    print('\nPart d)')
    print(set1)

    print('\nPart e)')
    fr_set=frozenset(set1)  ## making set immutable
    print('the immutable set is :',fr_set)

    print('\nPart f)')
    b=max(set1)
    print('max value :',b)    ### calculating max value and its hash value
    print('Hash value :',hash(b))

print('')


###################################################################################################################################################################
print('Question 4')
print('')
##creating a class
class Student:          ###Creating class with constuctor and destructor
    def __init__(self,name,roll_number):
        self.name=name           
        self.roll_number=roll_number

    def __del__(self) :
        print('Record of ',self.name,' destroyed')


s1=Student('Adarsh Mandloi',21105089) ## creating a class and feeding data into it
print('Name of s1:',s1.name)
print('Roll number of s1:',s1.roll_number)
del s1   ## deleting the object s1
print('Object s1 deleted') 
print('')
##############################################################################################################################################################
print('Question 5')
print('')
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def input_data(self):
        print('%s is an employee having salary %d'%(self.name,self.salary))
e1=Employee('Mehak',40000) 
e2=Employee('Ashok',50000)   
e3=Employee('Viren',60000)
##Printing the data entered for different object
## using for loop
for i in [e1,e2,e3]:
              i.input_data()
              
print('Part a')
e1.salary=70000 ## Updating the salary
print('Updated salary of Mehak is  :',e1.salary)
print('Part b')
print('Deleted the record of %s with salary %d'%(e3.name,e3.salary))
del e3   # deleting the object e3
print('')
##############################################################################################################################################################33
print('Question 6')
print('')
##Using anagram 
def anagram(s):  ## Defining the anagram function 
    if s=='' :
        return [s]
    else :
        word=[]
        for i in anagram(s[1:]) :
            for p in range(len(i)+1) :
                word.append(i[:p]+s[0]+i[p:])
        return word
### Talking input from the users 
word1=input('Give a word to test friendship :')
word_1=word1.lower()
word2=input('Give a meaningful word containing same letter of the word given by your friend :')
word_2=word2.lower()
## checking if the word contains same letter as the first word i.e its in its anagram or not
if word_2 in anagram(word_1) :  
    c=input('does the word entered by 2nd friend seems meaningfull ? (y/n) :')
    if c == 'y' :   ### checking the meaningfulness of word 
        print('Test passed thus  friendship is true')
    else :
        print('Test failed thus friendship is false ')
else :
    print('word does not have the same letter thus  test failed friendship is false ')
################################################################################################################################################################
