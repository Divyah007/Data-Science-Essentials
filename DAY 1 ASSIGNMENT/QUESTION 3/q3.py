#!/usr/bin/env python
# coding: utf-8

# # Questions 3:
# Write a program that takes cost price and selling price as input and displays whether the transaction is a
# Profit or a Loss or Neither.
# INPUT FORMAT
# The first line contains the cost price.
# The second line contains the selling price.
# OUTPUT FORMAT
# Print "Profit" if the transaction is a profit or "Loss" if it is a loss. If it is neither
# profit nor loss, print "Neither". (You must not have quotes in your output)
# 
# NOTE:
# Please stick to the input and output format. Don't add anything extra like
# 'Enter cost price', 'Enter selling price', etc.

# In[6]:


cp=float(input())
sp=float(input())
p=sp-cp
l=cp-sp
if(p>l):
    print("Profit")
elif(l>p):
    print("Loss")
else:
    print("Neither")


# In[ ]:





# In[ ]:




