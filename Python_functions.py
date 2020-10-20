#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def rule_1(c,A_err):
    q = c * A_err
    return q

def rule_2(a,b,c,d):
    q = abs(a * c * b**(c-1)) * d
    return q
    
def rule_3(A_err,B_err):
    q = np.sqrt(A_err**2 + B_err**2)
    return q

def rule_4(Q,A,A_err,m,B,B_err,n):
    q_err = abs(Q)*np.sqrt((m*(A_err/A))**2+(n*(B_err/B))**2)
    return q_err


print(rule_4(0.782383,1.4248,0.050636,1,10.5,3.1,-1))
  
    


# ### This computed value matches the original computed value

# In[4]:


x = [1.1, 1.3, 1.4, 0.9, 0.95, 1.05]

print('average =', np.average(x))
print('standard deviation =',np.std(x))


# $ \delta Q = \sqrt{(\delta A)^2 + (\delta B)^2} $

# $ \delta F = |F|\sqrt{(\frac{\delta m}{m})^2 + (-1\frac{\delta slope}{slope})^2} $ 

# In[ ]:




