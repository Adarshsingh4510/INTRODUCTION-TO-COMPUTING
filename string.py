Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 greeting='hello world'
 
SyntaxError: unexpected indent
greeting = 'Hello world'
greeting[0] ='J'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    greeting[0] ='J'
TypeError: 'str' object does not support item assignment
new_greeting ='J'+greeting[1:]
new_greeting
'Jello world'
new_greet=greeting.upeer()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    new_greet=greeting.upeer()
AttributeError: 'str' object has no attribute 'upeer'. Did you mean: 'upper'?
new_greet=greeting.upper()
new_greet
'HELLO WORLD'
index=greeting.find('o')
index
4
greeting.find('lo')
3
greeting.find('lo',4)
-1
name='bob'
name.find('b',1,2)
-1
'a'in 'banana'
True
'ba'in 'banana'
True
int(3.9999)
3
int(-2.333)
-2
float(32)
32.0
float('23.456')
23.456
str(32)
'32'
print("practice 24 min part")
practice 24 min part
