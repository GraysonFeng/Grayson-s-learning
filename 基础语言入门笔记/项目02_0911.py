
# coding: utf-8

# In[ ]:


'''
【项目02】  基于Python的算法函数创建

作业要求：
根据不同题目，完成代码书写并成功运行

'''


# In[2]:


# 题目1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的两位数？都是多少？
# 该题目不用创建函数
# 答案1：
n = 0
m = []
for i in range(1,5):
    for j in range(1,5):
        if i != j:
            n += 1
            num ='%i%i'% (i,j)
            m.append(num)
print('满足条件的数字一共有%i个.'%n)
print(m)


# In[8]:


# 题目2：输入三个整数x,y,z，请把这三个数由小到大输出，可调用input()。（需要加判断：判断输入数据是否为数字）
# 提示：判断是否为数字：.isdigit()
# 该题目需要创建函数
# 答案2：
def f(n):
    lst = []
    for i in range(1,n+1):
        num = input('请输入第%i个数字: '%i)
        while num.isdigit()== False:
            num = input('输入的内容不为数字，请重新输入第%i个数字 '%i)
        else:
            lst.append(float(num))
    return(sorted(lst))
f(3)


# In[14]:


# 题目3：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 提示：利用while语句,条件为输入的字符不为'\n'.
# 该题目不需要创建函数
# 答案3
st = input('请输入一行字符:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in st:
    if c.isalpha():
        letters +=1
    elif c.isdigit():
        digit +=1
    elif c.isspace():
        space +=1
    else:
        others +=1
print('输入的字符中，有%i个字母，有%i个空格，有%i个数字及其它字符%i个。'%(letters,space,digit,others))
print('输入的字符中，有{}个字母，有{}个空格，有{}个数字及其它字符{}个.'.format(letters,space,digit,others))


# In[15]:


# 题目4：猴子吃桃问题
# 猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个,
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少?
# 提示：采取逆向思维的方法，从后往前推断。
# 该题目不需要创建函数
# 答案4：
n = 1
for day in range(9,0,-1):
    m = (n+1)*2
    n = m
    print('第%i天剩%i个桃子'%(day,n))
print('第一天共摘了%i个桃子'%n)


# In[16]:


# 题目5：猜数字问题，要求如下：
# ① 随机生成一个整数
# ② 猜一个数字并输入
# ③ 判断是大是小，直到猜正确
# ④ 判断时间
# 提示：需要用time模块、random模块
# 该题目不需要创建函数
# 答案5：
#导入模块
import time
import random
n = random.randint(0,1000)
c = int(input('请输入一个数字（小于1000）：'))#转换成整数型
start = time.time()#记录开始时间点

while c != n:
    if c > n:
        print('猜大了')
        c = int(input('请重新输入一个数字（小于1000）：'))
    else:
        print('猜小了')
        c = int(input('请重新输入一个数字（小于1000）：'))
end = time.time()
tm = end - start
print('恭喜猜对了，正确答案是%i'%n)
print('共耗时%f秒'%tm)

