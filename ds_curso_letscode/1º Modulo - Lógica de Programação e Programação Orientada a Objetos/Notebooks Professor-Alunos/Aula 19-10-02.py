#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install datetime')


# In[2]:


import math


# In[3]:


math.pow(3,0.5)


# In[4]:


math.ceil(3**0.5)


# In[5]:


help(math.ceil)


# In[6]:


help(math.pow)


# In[7]:


dir(math) #exibe todos atributos que podem ser usados


# In[8]:


get_ipython().system('pip install pygame ')


# In[9]:


# pygame.org / pypi.org


# In[10]:


import pygame


# In[11]:


from math import factorial, log10


# In[12]:


factorial (5)


# In[13]:


log10(5)


# In[14]:


from math import *


# In[15]:


e


# In[16]:


pi


# In[17]:


from math import factorial as fact


# In[18]:


fact(5)


# In[19]:


import math as m


# In[20]:


m.tan(5)


# In[21]:


import datetime


# In[22]:


from datetime import time


# In[23]:


dir(time)


# In[24]:


some_time = time(12, 30, 46)


# In[25]:


print(some_time)


# In[26]:


some_time = time(0,0,10)


# In[27]:


print(some_time)


# In[28]:


some_time.microsecond


# In[29]:


from datetime import date


# In[30]:


some_day = date(day=1,month=4,year=1996)


# In[31]:


print("birthday: ", some_day)


# In[32]:


some_time = time(second=12, hour=15, minute=21)


# In[33]:


print(some_time)


# In[34]:


# timestamp: valor em segundo que define a data, calcula a partir de 01 de 01 de 1970


# In[35]:


minutes = 60
hour = minutes*60
day = hour*24
other_day = date.fromtimestamp(day)
print(other_day)


# In[36]:


from datetime import datetime


# In[37]:


now = datetime.now()
print(now)


# In[38]:


now.strftime("%d/%m/%Y")


# In[39]:


now.strftime("%Y/%m/%d")


# In[40]:


now.strftime("%d %B %Y")


# In[41]:


#import locale


# In[42]:


class Bolo:
    def assar(self, novo_sabor):
        self.sabor=""


# In[43]:


choco=Bolo()
choco.assar("chocolate crocante")


# In[44]:


a=now.strftime("%d %B %Y")
print(a)


# In[45]:


d=datetime.strptime("02/10/2019", "%d/%m/%Y")


# In[46]:


d


# In[47]:


d=datetime.strptime("02/10/2019", "%d/%m/%Y")


# In[48]:


data=input("Informe sua data de nascimento")


# In[49]:


print(data)


# In[50]:


type(data)


# In[51]:


data1=datetime.strptime(data, "%Y/%m/%d")


# In[52]:


data1


# In[53]:


variacao=datetime.now()-d


# In[54]:


print(variacao.microseconds)
#print(variacao.seconds 60 * 24)
variacao.seconds


# In[55]:


variacao.days


# In[56]:


from utilidades_by_rodrigo_soares import matematica


# In[57]:


result = matematica.soma(5,5)


# In[58]:


result


# Try

# In[62]:


n1=float(input("Informe o primeiro valor"))
n2=float(input("Informe o segundo valor"))


# In[63]:


try:
    result=n1/n2
except:
    print("Erro devido a divisão por zero")


# In[64]:


2/0


# In[ ]:




