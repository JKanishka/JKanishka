#!/usr/bin/env python
# coding: utf-8

# # Special Class Python Basics

# Title can be typed in notebook by using "#" and a space
# 
# To decrease a title needs to increase the Hashes //// It will also bold the statement

# # Title1
# ## Title2
# ### Title3
# #### Title4
# ##### Title5

# Print statement is used to print something on the screen
# 
# 
# To delete a cell : "Do D+D to delete a cell", however the cell should be selected

# ### To Activate a cell, we need to do ESC.
# ### Cell will work like markdown by pressing "M"
# ### Or Else it will work like a Coding Cell by pressing "Y"

# In[1]:


print('Kanishka')


# PWD to check what is platform directory

# In[2]:


pwd


# To write something in point we need to write "NUMBER DOT SPACE"
# 1. point 1
# 
# Or else if you required to add in bullet points, would need to "STAR SPACE"
# * point 1

# In[ ]:


#extension

image file - jpg, png, jpeg
video - mkv, mp4
audio - mp3
pdf - pdf
python - .py
jupyter notebook - .ipynb (Interactive Python Notebook)


# In[ ]:


#OS - Operating System

System software that manages computer h/w, software resources and provides common services for computer programs


# In[ ]:


#What is programming language

Is a formal language comprising of set of instructions that produces various kind of outputs


# In[ ]:


# Types of programming language

HLL: High Level Language (Programmer Friendly)
                        Python/
                        Java/
                        C++
                
                
LLL: Low Level Language (Computer/ Machine Friendly)
                        Bianory (0 & 1)


# Why we prefer HLL over LLL
#     
# Because our computer doesnt understand our language, so what we write it converts it to binary
# Need To Read ASCII Value
# 

# In[ ]:


#Convert HLL to LLL
a=10
# a is 97 for computer
# we will devide everything by 2 and remainder will be the Bianry

97/2
48/2 =1
24/2 =0
12/2 =0
6/2  =0
3/2  =0
1    =1


A is in binary 1100001 (Because it goes from down to up)


# In[ ]:


# b=20
98/2=0
49/2=1
24/2=0
12/2=0
6/2=0
3/2=0
1  =1

B is in binary 1100010


# In[ ]:


C = 1100011


# In[ ]:


# HLL  to LLL
- Compiler (C is compiler and a faster lang # because in compiler gives answer entirely)
- Interpreter (Python is interpreter and a bit slow but point out the exact error by pointing out the line of mistake)


# In[ ]:


# Why Python
1. Simple syntax (#we do not have to elaborat/easy to understand and write for python)
2. Libraries
3. Frameworks (create a WEB PAGE/ go to NETWORKING SITE/ build a BECKEND/ give a DESKTOP APPLICATION)
            famous app build on python (Google/ Netflix/ InstaGram (Django) / Quroa/ Youtube/ PUBG 
                                        (desktop built on Python)/ Battle field)
4. Large Community
5. It can work on all the platforms
6. Open Source (anybody can accessable for anyone on free)
7. Dynamic Typed Language  (#We do not have to type variable names/ python will automatically understand if it is int or float)


# # CLASS 2 (SPECIAL CLASS)

# In[5]:


#Basic Code
x = 2
y = 3
c = x+y
print(c)
print(x)
print(y)


# In[ ]:


# X is variable = is an operator & 2 is a Value/ Operand


# In[ ]:


#Identifiers

- rules given for a variable name/ function name/ class name, called as identifiers

1. Variable can contain : A-Z, a-z, 0-9, _
2. Cannot start with a number/ could contain number
3. Case Sensitive
4. No Limit (U can write infinity/ any length will work)
5. Unable to use reserved words


# # Variable can contain : A-Z, a-z, 0-9, _ (INVALID/ VALID)
# 
# ka_12                 | V    
# ka-khan               | I
# ka@123                | I
# jaiswal_kanishka      | V
# 12_34kanishka         | I
# k_123_123             | V

# # Case Sensitive
# 
# a = 10
# A = 20
# print(a)      >>>>> 10
# 
# a = 10
# a = 20
# print(a)      >>>>> 20

# # Unable to use reserved words
# 
# for
# if
# else
# break
# and
# or
# (It will show invalid syntax)

# In[7]:


import keyword


# In[10]:


print(keyword.kwlist) #WE CANNOT USE THESE KEYWORDS


# In[13]:


#print set range are FUNCTIONS


# #### IF we assigning variable to function// it will change the property of function/// The function will act like variable// and func will never work for us

# In[14]:


#solution for it is restart the Kernal


# # Valid (V)/(I) Invalid
# 
# kanis_123        | V
# 123_abc          | I
# _abc123          | V
# if               | I
# if_123           | V
# Else             | V
# true             | V
# False            | I
# print_123        | V
# Break            | V
# clasS            | V

# In[ ]:


# Data Types in python

#fundamental - It is basic Data Type
int (any value that is written/ without any decimatl point: 1,99999,100)
float (any value that is written with a decimal point eg 100.00, -999.0001, -100.01)
None (variable do not have a value)
str (anything that can be written a single/ double/ tripple quotes)
Bool (True or False)
Complex (any number that can be written in the form of a+bj), where a is the real and b is an imaginary

# Derived - which are derived from the fundamental data types
list ( Anything that can be written inside the [square bracket] and elements are seperated by commas a = [1,2,a,k])
tuple ( Anything that can be written inside a ()round bracket and elements are seperated by commas a = (1,2,a,k))
dic ( Anything that can be written inside a curly bracket and element are a pair of value = {"name":'kanishka'})
set ( Anything that can be written inside a {}curly braces and element are sep by commas a = {a,1,2,k})
range ( )


# type() - It will tell the data type of the variable


# # Stack Memory stores the *** Variable ***
# 
# # Heap Memory stores the *** Value ***

# In[15]:


#So when we assigned
a=2
# a created in stack memory
# 2 created in heap memory


# ### Every object (Variable) always has some address

# # id() tells the address of the variable

# In[17]:


a = 10
print(id(a))
b = 20
print(id(b))


# In[18]:


del b


# In[22]:


print(a)
print(b)


# In[ ]:


# type casting - change one datatype to another

int()
float()
str()
complex()
bool()


# In[29]:


a = 100.56
print(a)
print(type(a))
# 1st way
a = int(100.56)
print(type(a))
print(a)
# 2nd way
a = 100.56
print(int(a))
print(type(a))
print(type(int(a)))


# In[4]:


a = input('Please enter First number or name:')
b = input('Please enter Last number or name:')
print(type(a))
print(type(b))
print(a + b)


# In[2]:


x = input('Please enter First number or name:')
y = input('Please enter Last number or name:')
print(type(x))
print(type(y))
print(x+y)


# In[3]:


A = int(input('Please enter First number or name:'))
K = int(input('Please enter Last number or name:'))
print(type(A))
print(type(K))
print(A+K)


# In[13]:


list(range(1,23,1))


# # COMMENTS IN PYTHON
# 1. To make code understandable
# 2. To explaint the code
# 3. To prevent the execution

# In[15]:


pi = 3.14   #Value of a pie
r = 5   # Side of square
a = r*r # Area of square
print(a)
# Area of Square


# In[16]:


a = 10
b = 20
c = 30
print(a) # CTRL + ? to apply comment entirely
# print(b)
# print(c)


# # Operations
# ## 1. Arthmatic operation
# ###  % Modulas
# ###  // floor devision
# ###  / float devision
# ###  ** power symbol
# ###  plus +
# ###  minus -
# ###  multiplication *

# In[17]:


print(10+20)
print(10-30)
print(10/2)
print(10*2)
print(20%6)
print(30//4)


# In[18]:


# Floar valued/ Value / Ceiling Value
# 102/          102.30/ 103


# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[19]:


a = 20
b = 30
if a<10 and b>20:
    print('executed')
else:
    print('OOPs')


# In[ ]:


# AND
True and False ----> false
True and True -------> true
False and False ------> false
False and True ----------->false


# OR
True and False ----> True
True and True -------> true
False and False ------> false
False and True ----------->true

# NOT
not True---> False
not False----> True


# In[21]:


#ASCII VALUE
ord('k')


# In[22]:


chr(97)


# In[31]:


# Shift + Tab by clicking inside the print command


# In[34]:


a = 10
b = 'Kanishka'
c = 30

print(a, end = '\n') #next line\n
print(b, end = '\t') # tab space of 4 spaces
print(c, end = '**')


# In[35]:


# Condition statements
#if statement 1 is correct then print(statement 1)
#else print('whatever')


# In[ ]:


"""
If condition will be executed if condition is true OTHERWISE else will be executed
"""
stat1
stat2
if cond1:
    stat3
    stat4
stat5
stat6
"""
If cond1 is True ---> 1,2,3,4,5,6
If cond1 is False ----> 1,2,4,6
"""


# In[ ]:


"""
If conditions with 2nd If condition
"""
stat1
stat2
if cond1:
    stat3
    stat4
if cond2:
    stat7
    stat8
stat5
stat6
"""
If cond1 is True BUT cond2 is False ---->1,2,3,4,5,6
If cond1 is False BUT cond2 is True ---->1,2,7,8,5,6

If both are false ----> 1,2,5,6
"""


# In[ ]:


stat1
stat2
if cond1:
    stat3
    stat4
else:
    stat7
stat5
stat6
"""
If cond1 is True ---->1,2,3,4,5,6
If cond1 is False---->1,2,7,5,6
"""


# In[ ]:


"""
Else always works on the previous if condition only// if previous if is true then else will not apply/ otherwise else will be
applied
"""
stat1
stat2
if cond1:
    stat3
    stat4
if cond2:
    stat7
    stat8
else:
    stat9
stat5
stat6
"""
If cond1 is True BUT cond2 is False ---->1,2,3,4,9,5,6
If cond1 is False BUT cond2 is True ---->1,2,7,8,5,6

If both are false ----> 1,2,9,5,6
"""


# #### INPUT function  always return a string  data type

# In[38]:


# F string
a = input('Please FN')
b = input('Please LN')

print(a,b)
print('My name is '+a+' and last name is '+b+'')
print(f'My name is {a} and last name is {b}') # F strings
print('My name is {} and last name is {}'.format(a,b)) # format strings


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




