#!/usr/bin/env python
# coding: utf-8

# ## 문제 1

# In[1]:


def solution(A):
    dic = {}
    for i in A:
        try:
            dic[i] = A.count(i)
        except:
            dic[i] = 1
    maxkey = sorted(list(dic), key=lambda x: dic.get(x), reverse=True)[0]
    maxvalue = dic.get(maxkey)
    if maxvalue > len(dic) / 2:
        return A.index(maxkey)
    else:
        return -1


# In[2]:


A = [3, 4, 3, 2, 3, -1, 3]


# In[3]:


solution(A)


# ## 문제 2

# In[4]:


def palindrome(string):
    ls = list(string.lower())

    ls_alnum = []
    for i in ls:
        if i.isalnum():
            ls_alnum.append(i)

    mid = len(ls_alnum) // 2

    if len(ls_alnum) % 2:
        start = list(range(mid, 0, -1))
        end = list(range(mid+2, len(ls_alnum)+1))
    else:
        start = list(range(mid, 0, -1))
        end = list(range(mid+1, len(ls_alnum)+1))
        
    for i, j in zip(start, end):
        if ls_alnum[i-1] == ls_alnum[j-1]:
            continue
        else:
            return False
        
    return True


# In[5]:


palindrome("a%Zbc!bZ&*()a")


# In[ ]:




