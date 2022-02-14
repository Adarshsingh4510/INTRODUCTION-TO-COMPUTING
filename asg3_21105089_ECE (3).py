 #####Question no 1
############################################################################################################################################################################################
print('Solution 1')
inp_string=input('Enter the string: ') ## taking input string from user
upper_string=inp_string.upper()        ## converting in one case either upper or lower so that 'PYTHON',python and Python and all such cases can be treated as a single word
list_conversion=upper_string.split()   ## making a list from string using split function

if len(list_conversion)==1:      ## Using the length function to differentiate the code of both multi length string and single word
    list_new=[]
    for i in upper_string:       
        list_new.append(i) 
    dict1={}                     ## Creating the dictionary to print no of occurences 
    for count in list_new:
        if count in dict1:
            dict1[count]=dict1[count]+1
        else:
            dict1[count]=1 
    print(dict1)                ##printing the dictionary with key as letter and value as no. of occurences
else:
    dict2={}
    for word in list_conversion:
        if word in dict2:
            dict2[word]=dict2[word]+1
        else:
            dict2[word]=1
    print(dict2)                ##printing the dictionary with key as letter/word and value as no. of occurences

#############QUESTION 2
#############################################################################################################################################################################################
print('Solution 2')

#Taking inputs from user
day=int(input('Enter a valid date between 1 to 31- ')) 
month= int(input('Enter a valid month between 1 to 12- '))
year=int(input('Enter a valid year between 1800-2025- '))
###Removing all invalid cases
if day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025 or (month in [4,6,9,11] and day>30) or (month==2 and year%4!=0 and day>28) or (month==2 and year%4==0 and day>29):
         print('Enter a valid inputs')
###Dealing with valid cases
else:
    if month==2:  ## Dealing with leap and non-leap year in month==2
        if year%4==0:
            if day <29:
                day=day+1
                print('Next Date is',day,'/',month,'/',year)
            else:
                print('Next date is 01/03/',year)
        else:
            if day<28:
                day=day+1
                print('Next Date is',day,'/',month,'/',year)
            else:
                print('Next date is 01/03/',year)
    elif month in [4,6,9,11]:  ##dealing with month  having 30 days
        if day<30:
           day=day+1
           print('Next Date is',day,'/',month,'/',year) 
        else:
            print('Next date is 01/',month+1,year)
    else:
        if day<31:             ## dealing with month having 31 day and month of december
            day=day+1
            print('Next Date is',day,'/',month,'/',year)
        else:
            if month==12:
                print('Next date is 01/01/',year+1)
            else:
                print('Next date is 01/',month+1,year)


##########################################################################################################################################################################################
#####   QUESTION 3
#########################################################################################################################################################################################
print('Solution 3')
list=[3,9,10]
list2=[]      ## create the empty list
for i in list:
    tup=(i,i*i)
    list2.append(tup) ### using append function to add tuples to list
print(list2)
#######################################################################################################################################################################################
#### QUESTION 4
#######################################################################################################################################################################################
print('Solution 4')
grade_point=int(input('Enter the grade point between 4 to 10: '))
if grade_point>3 or grade_point<11:   ### using the two dictionary to print grade and performance
    grades={4:'D',5:'C',6:'C+',7:'B',8:'B+',9:'A',10:'A+'}
    performance={4:'Poor',5:'Below Average',6:'Average',7:'Good',8:'Very Good',9:'Excellent',10:'Outstanding'}

    print('Your grade is',grades[grade_point],'and',performance[grade_point],'performance')
else:
    print('Enter a valid grade_point')
######################################################################################################################################################################################
#### QUESTION 5
#######################################################################################################################################################################################
print('Solution 5')
string='ABCDEFGHIGKJ'
j=0
for row in range(1,7):   ### using 'for' loop with row and column 
    for column in range(0,row-1):
        print(' ',end='') ### adding required spaces needed depending upon rows and colomn
    
    s=string[0:11-j] ## adding required alphabets depending upon rows and column 
    print(s)
    j=j+2
########################################################################################################################################################################################
#### QUESTION 6
##########################################################################################################################################################################################

print('Solution 6')
info=dict()
permission='Y'
while permission=='Y':   ### using 'while' loop to ask for details of student 
    SID=int(input('Enter SID: '))
    student_name=input('Enter student name: ')
    info[SID]=student_name
    permission=input('Did you like to enter other student entry say Y for yes and N for no : ')
##Part a
print('Part a')
for i in info:
    print((i,info[i]))  ## printing student details stored  in  the dictionary 
## Part b
print('Part b')
## sort dictionary using student name
list1=[]
for value in info.values():
          list1.append(value)
list1.sort()
sorted_info={}
for i in list1:
         for key in info:
          if i==info[key]:
            sorted_info[key]=i 
print(sorted_info)   ## printing the dictionary by sorting with student name
##Part c
print('Part c')    
for i in sorted(info.keys()):    ## printing the dictionary by sorting using SID
    print((i,info[i]))
##Part d
print('Part d')  ## searching the student name with the help of SID
search=int(input('type the  student SID to get name of that student: '))
print(info[search])
##########################################################################################################################################################################################         
 ##### QUESTION 7
##########################################################################################################################################################################################
print('Solution 7')

### Taking input From the user

n=int(input('Enter the number till you want to See fibonacci series: '))
def fib(n):          ### Using function to print fibonacci series 
    if n==1:         ### giving the required intial two values to form a fibonacci series
        return 0
    if n==2:
        return 1
    
    return   fib(n-2)+fib(n-1)
for i in range(1,n+1):
    print(fib(i),' ',end='')
##########################################################################################################################################################################################
#####   QUESTION 8
#########################################################################################################################################################################################
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
##Part a
print(' ')
print('Part a')
##a new set of all elements that are in Set1 and Set2 but not both.
set_new=Set1^Set2
print(set_new)
## Part b
print('Part b')
### a new set of all elements that are in only one of the three sets Set1, Set2 and Set3.

Set4=Set1^Set2^Set3
print(Set4)
##Part c
print('Part c')
### a new set of elements that are exactly two of the sets Set1, Set2 and Set3.

set5=Set1 & Set2
set6=Set2 & Set3
set7=Set1 & Set3
set8=set5^set6^set7
print(set8)
##Part d
print('Part d')
##a new set of all integers in the range 1 to 10 that are not in Set1.
list1=[]    # creating an empty list
for i in range(1,11) :
    if i not in Set1:
        list1.append(i)
set9=set(list1)     # converting list into set 
print(set9)

# Part e
print('Part e')

list2=[]          # creating an empty list 
for i in range(1,11) :
    if (i not in Set1) and (i not in Set2) and (i not in Set3):
        list2.append(i)
set10=set(list2)         # converting list into set 
print(set10)
                
                
                
                
            
        
