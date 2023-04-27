#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# source

print("copy and paste the url")
src = input()


# In[17]:


from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome()
driver.get(src)

guest = driver.find_element("css selector", 'body > div.oa.ltbg > div.fl > div > table > tbody > tr > td:nth-child(3) > button')
guest.click()

time.sleep(5)

driver.switch_to.window(driver.window_handles[1])
element = driver.find_element("css selector", 'body')
src = element.get_attribute('innerHTML')


# In[18]:


# range adj

start = src.find('tbody')
end = src[start+1:].find('tbody')
usable = src[start:start+end]


# In[19]:


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
    


# In[20]:


# removing annotation

for i in range(len(checklist)) :
    if len(checklist[i]) > 4 :
        checklist[i] = checklist[i][0:4]


# In[21]:


# removing hyphen

for i in range(len(checklist)) :
    checklist[i] = checklist[i][0] + checklist[i][2:]


# In[22]:


# removing gap

for i in range(len(checklist)) :
        checklist[i] = checklist[i].replace(" ", "")


# In[23]:


# changing None

for i in range(len(checklist)) :
        if checklist[i] == '-' :
            checklist[i] = 'xx'


# In[24]:


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


# In[25]:


# x-axis adj 

for i in range(len(checklist)) :
    for k in range (11) :
        if checklist[i][0] == xabc[k] :
            checklist[i] = xabc[k+1] + checklist[i][1:] 
            break


# In[26]:


# y-axis adj

for i in range(len(checklist)) :
    if checklist[i] == 'xx' :
        continue
    for k in range (19) :
        if int(checklist[i][1:]) == numbers[k] :  
            checklist[i] = checklist[i][0] + abc[k]
            break


# In[27]:


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


# In[15]:


# converting to sgf

import os

os.rename('gibo.txt', 'gibo.sgf')


# In[ ]:


print(' Done ')
os.system('pause')

