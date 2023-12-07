#!/usr/bin/env python
# coding: utf-8

# In[14]:


#数组版本
#计算生日概率的Mathematica代码
import matplotlib.pyplot as plt

#初始化“生日在同一天”和“生日不在同一天”的概率列表,因为递归化需要存储之前的值

#开始时, 生日不在同一天的概率是100% 
noshare = [[1,1]]

#开始时, 生日在同一天的概率是0
share = [[1,0]]

#当前生日不在同一天的概率
currentnoshare =1 

#将计算前50个人的情况
for i in range(2,50):
    newfactor = (365-(i-1))/365 #乘积的第二项
    currentnoshare *= newfactor
    noshare.append([i,currentnoshare]) #更新‘生日不在同一天的概率‘
    share.append([i,1.0-currentnoshare])#更新‘生日在同一天的概率‘

x = [item[0] for item in share]
y = [item[1] for item in share]
plt.plot(x,y)
plt.xlabel('n')
plt.ylabel('Probability')
plt.show()


# In[13]:


#pandas版
import pandas as pd
import matplotlib.pyplot as plt

# 计算生日在同一天的概率
df = pd.DataFrame({'n': range(1, 51)})
df['share_probability'] = 1 - (364 / 365) ** (df['n'] * (df['n'] - 1) / 2)

# 绘制图表
plt.plot(df['n'], df['share_probability'])
plt.xlabel('n')
plt.ylabel('Probability')
plt.show()


# In[ ]:




