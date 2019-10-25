
# coding: utf-8

# In[1]:

#字符串
str="Hello,world!"


# In[2]:

str[5]


# In[3]:

len(str)


# In[4]:

max(str)


# In[5]:

print(str.upper())


# In[6]:

print(str.lower())


# In[7]:

print(str.title())


# In[8]:

#任何一个有返回值的函数在原则上都不会改变字符串自身


# In[9]:

str="hello"
name="zm"
print(str+name)


# In[10]:

str.join(name)#把name的每一个元素取出，中间用str进行连接


# In[11]:

numbers="12345"
" + ".join(numbers)


# In[12]:

"hello,%s"%"world"


# In[14]:

x=3
print("{}={}*{}".format(x*x,x,x))
print("{1}={0}*{0}".format(x,x*x))


# In[41]:

print("my name is {name},my age is {age}".format(name="zm",age="22"))
name="zm"
age=22
print(f'my name is {name},my age is {age}')


# In[38]:

"hello".center(11)


# In[39]:

"hello".center(11,"*")


# In[40]:

print("*"*40)
print("hello".center(38).center(40,"*"))
print("*"*40)


# In[43]:

answer=input("do you like python?")
if answer.lower() =="yes":
   print("Great!")


# In[44]:

"hello".replace("h","H")


# In[45]:

"hello,#name#".replace("#name#","zm")


# In[49]:

name ='zm'
age = 20
print(f'my name is {name},my age is {age}')


# In[51]:

#dictionary
names=["zs","ls","ww","ml"]
scores=[100,90,80,70]
name=input("please input a name")
print(scores[names.index(name)])


# In[52]:

scores={"zs":100,"ls":90,"ww":80,"ml":70}
name=input("please input a name")
print(scores[name])


# In[54]:

scores={}

scores["zs"]=100
scores


# In[55]:

"zs" in scores


# In[56]:

name=input("please input a name:")
if name in scores:
    print(scores[name])
else:
    print("name not found")


# In[57]:

del scores["zs"]
scores


# In[60]:

scores["ls"]=90
scores


# In[61]:

s2=scores
s2["zs"]=100
scores


# In[63]:

scores={}.fromkeys(["zs","ls","ww","ml"],100)
scores


# In[68]:

str="hello,this is a test,i desigh the test last night"
count=dict.fromkeys("aeiou",0)
for ch in str:
    if ch in "aeiou":
        count[ch]+=1
print(count)


# In[70]:

print(count.get("a"))


# In[78]:

student=dict.fromkeys(["name","score"])
student["name"]=input("please input a name:")
student["score"]=int(input("please input a score:"))
print("{}'s scors is {}".format(student["name"],student["score"]))


# In[80]:

first_names=["san","si","wu","liu","jia","yi","bing"]
last_names=["zhao","qian","sun","li","zhou","wu","zheng","wang"]
names=list()
for first_name in first_names:
    for last_name in last_names:
        names.append(first_name+" "+last_name)
print(names)


# In[91]:

import random
import math
for i in range(0,100):
    score=math.ceil(random.gauss(75,20))
    if score>100:
        score=100
    elif score<0:
        score=0
    print(score,end=" ")


# In[98]:

score_db={}
score_template={}.fromkeys(["physics","Math","Python"])
for name in names:
    scores=score_template.copy()
    
    score=math.ceil(random.gauss(75,20))
    if score>100:
        score=100
    elif score<0:
        score=0
    scores["physics"]=score

    score=math.ceil(random.gauss(75,20))
    if score>100:
        score=100
    elif score<0:
        score=0
    scores["Math"]=score
    
    score=math.ceil(random.gauss(75,20))
    if score>100:
        score=100
    elif score<0:
        score=0
    scores["Python"]=score
    score_db[name]=scores
    
print(score_db)


# In[99]:

def add(a,b):
    return a+b
print(add(3,4))


# In[100]:

name=input('please input a name:')
if name in score_db:
    print("physics:",score_db[name]["physics"])
    print("Math:",score_db[name]["Math"])
    print("Python:",score_db[name]["Python"])
else:
    print("not found")
    


# In[ ]:



