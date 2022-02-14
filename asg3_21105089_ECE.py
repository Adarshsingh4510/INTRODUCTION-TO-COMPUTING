#Taking input string from the user
string=input('Enter the string: ')
#Converting in upper case so that 'python' , 'Phyton' and all related cases are same
upper_case=string.upper()
#Converting the string in list
new_list=upper_case.split()
#using length of string
if len(new_list)==1:
    letters_list=[]
    for letter in string:
        letters_list.append(letter)
    print(letters_list)
    counts={}
    if letter in letters_list:
        counts[letter]=counts[letter]+1
    else:
        counts[letter]=1
    print(counts)
else:
    count={}
    if word in new_list:
        count[word]=count[word]+1
    else:
        count[word]=1
    print(count)
    
    
    

      
            



