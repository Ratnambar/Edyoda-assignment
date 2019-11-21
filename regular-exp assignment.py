#!/usr/bin/env python
# coding: utf-8

# In[41]:


import re
s="12-06-2019"
r=re.compile("(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})")
m=re.search(r,s)
if m:
    x=int(m.group('year'))
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                print(" leap year")
            else:
                print(" not a leap year")
        else:
            print(" leap year")
    else:
        print("not a leap year")
    print(m.group()+" is a valid date")
else:
    print("invalid date")


# In[10]:





# In[51]:


s = "abcd.1_2@xyz.com"
r = re.compile("^[a-z]*.[0-9]*_[0-9]*@[a-z]*.[a-z]{3}$")
m = re.search(r,s)
if m:
    print(m.group())
else:
    print("Invalid email")


# In[72]:


s1 = "www.edyoda.com/code/python"
s2 = "The code is present at url <a href = {}>{}</a>"
r = re.compile("^[w]{3}.[a-z]*(.com)/[a-z]*/[a-z]*$")
m = re.search(r,s1)
if m:
    x = str(m.group())
    print(x)
    print(s2.format(m.group(),m.group()))
else:
    print("invalid url")


# In[2]:


import re
s="abc.1.2@gmail.com"
r=re.compile("^[a-z]*.[0-9]*.[0-9]*@{1}[a-z]*.com$")
m=re.search(r,s)
if(m):
    print("valid email")
else:
    print("invalid email")


# In[ ]:




