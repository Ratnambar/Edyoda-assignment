#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# l=[2,4,6,3,5]
# ceven=0
# codd=0
# for val in l:
#     if val%2==0:
#         ceven +=1
#     else:
#         codd +=1
# if ceven>codd:
#     for val in l:
#         if val%2 != 0:
#             l.remove(val)
                
# elif codd>ceven:
#     for val in l:
#         if val%2 == 0:
#             l.remove(val)
                
# print(l)
# print(ceven)
# print(codd)


# In[123]:


d={"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"} 

def travel_sequence(d):
    l1=[]
    l2=[]
    l=[]
    l4=[]
    for k,v in d.items():
        l1.append(k)
        l2.append(v)
    l=sorted(list(zip(l1,l2)))
    l4.append(l[0])
    for i in range(0,len(l)):
        for j in range(0,len(l)-1):
            if l[i][1] == l[j+1][0]:
                l4.append(l[j+1])
    return l4
travel_sequence(d)       


# In[118]:
#que-2

states = {'New Hampshire': ['Concord', 'Hanover'],
'Massachusetts': ['Boston', 'Concord', 'Springfield'],
          'Illinois': ['Chicago', 'Springfield', 'Peoria'] }
d={}
def city_with_states(d):
    for key,values in states.items():
        for value in values:
            if value not in d:
                d[value]=[key]
            else:
                d[value].append(key)
city_with_states(d)
print(str(d))


# In[49]:

#que -5
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def num2roman(num):
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman
num=int(input())
num2roman(num)


# In[69]:
#que-9

l=[1, 4, 3, 2, 5]
l1=[]
l2=[]
k=int(input())
m=len(l)-k
for j in range(0,m+1):
    i=j
    count = 1
    for i in range(j,k+1):
        if count<=k:
            if j==0:
                l1.append(l[i])
                count +=1
            else:
                l2.append(l[i])
                count+=1

if l1[0]>l2[0]:
    print(l1)
else:
    print(l2)


# In[3]:
#que-6

import re
fp=open("D:\sample1.txt","r")
count=0
content=fp.readlines()
for  each_line in content:
    count +=1
print(count)
fp.close()


# In[ ]:

#que-7
import re
s=str(input("enter the password"))
lcount=0
luper=0
alnum=0
if len(s)>=8:
    r=re.compile("[A-Za-z\d!@#$%&]{1,19}$")
    m=re.search(r,s) 
#     regexp =re.search(regex,s)  
    if m:
        for i in s:
            if (i.islower()):
                lcount +=1
            elif(i.isupper()):
                luper +=1
            elif(i.isalnum()):
                alnum +=1
                
    else:
        print("invalid")
#     print(lcount)
#     print(luper)
regex = re.compile("[@!#$&]")
if lcount == 0:
    print("Weak",["The password must contain at least 1 lower letter"])
elif luper == 0:
    print("Weak",["The password must contain at least 1 capital letter"])
# elif not (re.match("[@!#$&]", s)):
elif (regex.search(s) == None):
    print("Weak",["The password must contain at least 1 special letter"])
# elif (lcount>0 and luper>0 and (re.match(regex, s))):
#       print("Strong Password")
else:
    print("valid password")
    


# In[ ]:
#que-8

def check_sentence(string): 
    length = len(string) 
    if string[0] < 'A' or string[0] > 'Z': 
        return False
   
    if string[length-1] != '.': 
        return False
  
    prev_state = 0
    curr_state = 0
  
    
    index = 1
  
    while (string[index]): 
        
        if string[index] >= 'A' and string[index] <= 'Z': 
            curr_state = 0
            
        elif string[index] == ' ': 
            curr_state = 1
     
        elif string[index] >= 'a' and string[index] <= 'z': 
            curr_state = 2
         
        elif string[index] == '.': 
            curr_state = 3
  
     
        if prev_state == curr_state and curr_state != 2: 
            return False
          
        if prev_state == 2 and curr_state == 0: 
            return False
  
        if curr_state == 3 and prev_state != 1: 
            return True
  
        index += 1
  
        prev_state = curr_state 
  
    return False
   
string = ["I love cinema.", "The vertex is S.", 
            "I am single.", "My name is KG.", 
            "I lovE cinema.", "GoogleQuiz. is a quiz site.", 
            "I love Google and Googlesquiz.", 
            "  You are my friend.", "I love cinema"] 
string_size = len(string) 
for i in range(string_size): 
    if checkSentence(string[i]): 
        print("\"" +  string[i] + "\" is correct")
    else: 
        print("\"" + string[i] + "\" is incorrect")


# In[ ]:





# In[ ]:




