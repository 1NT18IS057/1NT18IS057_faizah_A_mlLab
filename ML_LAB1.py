#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[2]:


str="Jupyter"


# In[3]:


print(str)


# In[4]:


a=2
print(a)


# In[6]:


n1=5
n2=6
sum=n1+n2
print(sum)


# In[23]:


n1=5
n2=6
sum=n1+n2
print("sum=",sum)


# In[ ]:





# In[7]:


a=3
b=7
a=a+b
b=a-b
a=a-b
print(a)
print(b)


# In[21]:


def check(lang):
    if lang=="eng":
        print("English")
    elif lang=="hin":
        print("Hindi")
    else:
        print("Other language")
lang=input("Enter the language :")
check(lang)


# In[9]:


check("eng")


# In[10]:


for i in range(20):
    print(i)


# In[18]:


def calc(a,b,op):
    if op=="+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op=="*":
        print(a*b)
    elif op=="/":
        print(a/b)
    elif op=="%":
        print(a-b)
    else:
        print("Invalid operator")
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
op=input("Enter the operand:")
calc(a,b,op)


# In[22]:


a=10
if a<20:
    print("success")
else:
    print("failure")


# In[24]:


def concat(str1,str2):
    print("concatenated string : ",str1+str2)
str1=input("Enter the 1st String:")
str2=input("Enter the 2nd String:")
concat(str1,str2)


# In[27]:


def compare(str1,str2):
    if str1.lower()==str2.lower():
        print("strings are equal")
    elif str1.lower()>str2.lower():
        print("First string is greater")
    else:
        print("Second string is greater")
str1=input("Enter the 1st String:")
str2=input("Enter the 2nd String:")
compare(str1,str2)


# In[30]:


def reverse(str):
    rev=""
    for i in str:
        rev=i+rev
    print("Reversed string :",rev)


# In[31]:


reverse("machine")


# In[32]:


def reverse(str):
    print(str[::-1])


# In[33]:


reverse("hello")


# In[34]:


def copy(str1):
    str2=str1
    print("string copied is :",str2)


# In[35]:


copy("strcopy")


# In[39]:


a=[1,2,3,4,5,6,7,8,9,10]
b=slice(0,9,2)
print(a[b])


# In[38]:


b


# In[40]:


l1=[10,20,30,40,50]
l1[2]=50
l1[2]


# In[41]:


l1[1:3]


# In[42]:


l1.append(60)
l1


# In[43]:


l1.pop()


# In[44]:


l1


# In[62]:


l1.remove(50)
l1


# In[46]:


l1


# In[47]:


l2=[10,"hello",78.34]
for i in l2:
    print(i)


# In[49]:


t=(4,"ml",7.77)
t


# In[52]:


l2[-1]


# In[53]:


l1.extend(l2)


# In[54]:


l1


# In[63]:


d={"name":"Faizah","age":21,"place":"blore"}
d


# In[59]:


d


# In[61]:


d['name']


# In[64]:


t=("Jomonkey",[1,2,3],(2,9))
t


# In[65]:


dict={"one":"hello","two":"bonjour",3:"welcome"}
dict['one']


# In[72]:


for key,value in dict.items():
    print(key,value)


# In[ ]:




