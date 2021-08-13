#!/usr/bin/env python
# coding: utf-8

# #                             Factorial

# In[ ]:


def fic(n):
    if(n < 0):
        return "Enter Valid number i.e(greater than or equal 0)"
    if(n == 1 or n==0):
        return 1
    else:
        return n * fib(n-1)


# # Fibonacci Series

# In[ ]:


def fib(n):
    if(n==1 or n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)


# # Fibonacci Series with O(n) Running Time

# In[ ]:


def fib(n,memo={}):
    if (n in memo):
        return memo[n]
    elif( n <=2):
        return 1
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    print(memo)
    return memo[n]


# # Grid With O(M*N) Running Time

# In[ ]:


def grid(m,n,memo={}):
    x=str(m)
    y=str(n)
    key=x+','+y
    if(key in memo):
        return memo[key]
    if(m == 1 and n==1):
        return 1
    elif(m==0 or n==0):
        return 0
    else:
        memo[key] = grid(m-1,n,memo) + grid(m,n-1,memo)
        return memo[key]


# # Cansum 

# In[33]:


def Cansum(targetSum,numbers):
    if( targetSum==0):
        return True
    elif( targetSum < 0):
        return False
    else:
        for i in numbers:
            reminder=targetSum-i
            if Cansum(reminder,numbers) == True:
                return True
        return False
numbers=[14,7]
targetSum=300
Cansum(targetSum,numbers)


# # Cansum with memoization

# In[30]:


def Cansum(targetSum,numbers,memo={}):
    if(targetSum==0):
        return True
    elif(targetSum < 0):
        return False
    elif(targetSum in memo):
        return memo[targetSum]
    else:
        for i in numbers:
            reminder=targetSum-i
            memo[reminder]=Cansum(reminder,numbers,memo)
            if memo[reminder] == True:
                return True
        return False
numbers=[14,6]
targetSum=30
print(Cansum(targetSum,numbers))


# #  Print Sum of numbers equal to TargetSum

# In[29]:


def howsum(targetSum,numbers,memo={}):
    if(targetSum in memo):
        return memo[targetSum]
    if(targetSum == 0):
        return []
    elif(targetSum < 0):
        return None
    else:
        for i in numbers:
            reminder =  targetSum - i
            x=howsum(reminder,numbers,memo)
            if( x != None):
                x.append(i)
                memo[targetSum]=x
                return memo[targetSum]
numbers=[14,6]
targetSum=30
print(howsum(targetSum,numbers))


# In[ ]:




