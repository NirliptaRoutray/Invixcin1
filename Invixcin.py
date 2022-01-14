#!/usr/bin/env python
# coding: utf-8

# In[14]:


def freq(str):          
    str2 = []
    for i in str:           
        if i not in str2:
            str2.append(i) 
              
    for i in range(0, len(str2)):
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))  
        

    
s1=str(input("enter a string : "))
freq(s1)
s2=str(input("enter a string : "))
freq(s2)

def count(str1, str2): 
    c, j = 0, 0
    for i in str1:
        if str2.find(i)>= 0 and j == str1.find(i): 
            c += 1
        j += 1
    print ('No. of matching characters are : ', c)


# In[21]:


def freq(str):          
    str2 = []
    for i in str:           
        if i not in str2:
            str2.append(i) 
              
    for i in range(0, len(str2)):
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))  
        
s1=str(input("enter a string : "))

s2=str(input("enter a string : "))
if len(s1) != len(s2):
    print('valid')
else:
    def count(str1, str2): 
        c, j = 0, 0
        for i in str1:
            if str2.find(i)>= 0 and j == str1.find(i): 
                c += 1
            j += 1
        print ('No. of matching characters are : ', c)


# In[ ]:




