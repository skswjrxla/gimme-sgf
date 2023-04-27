#!/usr/bin/env python
# coding: utf-8

# In[1]:


# source

import time
print("copy and paste the html line")
src = input()


# In[2]:


# range adj

start = src.find('tbody')
end = src[start+1:].find('tbody')
usable = src[start:start+end]


# In[3]:


# finding points

checklist = []
count = 0

while True :
    count += 1
    restart = usable[1:].find('">')
    usable = usable[restart+1:]
    reend = usable[1:].find('</td>')
    if restart == -1 :
        break
    if count == 1: 
        continue
    insertion = usable[2:reend+1]
    checklist.append(insertion)
    


# In[4]:


# removing annotation

for i in range(len(checklist)) :
    if len(checklist[i]) > 4 :
        checklist[i] = checklist[i][0:4]


# In[5]:


# removing hyphen

for i in range(len(checklist)) :
    checklist[i] = checklist[i][0] + checklist[i][2:]


# In[6]:


# removing gap

for i in range(len(checklist)) :
        checklist[i] = checklist[i].replace(" ", "")


# In[7]:


# changing None

for i in range(len(checklist)) :
        if checklist[i] == '-' :
            checklist[i] = 'xx'


# In[8]:


# numbers and alphabets

from string import ascii_lowercase
numbers = []
abc = list(ascii_lowercase)
xabc = abc[0:20]
abc = abc[0:19]
for i in range (19) :
    numbers.append(i+1)

xabc.reverse()
abc.reverse()


# In[9]:


# x-axis adj 

for i in range(len(checklist)) :
    for k in range (11) :
        if checklist[i][0] == xabc[k] :
            checklist[i] = xabc[k+1] + checklist[i][1:] 
            break


# In[10]:


# y-axis adj

for i in range(len(checklist)) :
    if checklist[i] == 'xx' :
        continue
    for k in range (19) :
        if int(checklist[i][1:]) == numbers[k] :  
            checklist[i] = checklist[i][0] + abc[k]
            break


# In[11]:


# sgf file generation 

sgf = open('gibo.txt', 'w')
sgf.write('(\n')
sgf.write(';')
for i in range (len(checklist)) :
    if i % 2 == 0 :
        text = 'B' + '[' + checklist[i] + ']' + ';'  
    else :
        text = 'W' + '[' + checklist[i] + ']' + ';'
    sgf.write(text)
sgf.write('\n)')
sgf.close()


# In[12]:


# converting to sgf

import os

os.rename('gibo.txt', 'gibo.sgf')


# In[ ]:


print(' Done ')
os.system('pause')

