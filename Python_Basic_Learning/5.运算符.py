"""
算数运算符
赋值运算符
复合赋值运算符
⽐较运算符
逻辑运算符

+               加
-               减
*               乘
/               除
//              整除
%               取余
**              指数
()              调整优先级
"""

a = 10
b = 20
c = 30
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

"""
复合赋值运算符
+=                  加法赋值运算符
-=                  减法赋值运算符
*=                  乘法赋值运算符
/=                  除法赋值运算符
//=                 整除赋值运算符
%=                  取余赋值运算符
**=                 幂赋值运算符
"""


"""
逻辑运算符
and             x and y         布尔"与"：如果 x 为 False，x and y 返回False，否则它返回 y 的值。
or              x or y          布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值。
not             not x           布尔"⾮"：如果 x 为 True，返回 False 。如果 x为False，它返回 True。
"""
a = 1
b = 2
c = 3
print((a < b) and (b < c)) # True
print((a > b) and (b < c)) # False
print((a > b) or (b < c)) # True
print(not (a > b)) # True

a = 0
b = 1
c = 2

# and运算符，只要有⼀个值为0，则结果为0，否则结果为最后⼀个⾮0数字
print(a and b) # 0
print(b and a) # 0
print(a and c) # 0
print(c and a) # 0
print(b and c) # 2
print(c and b) # 1

# or运算符，只有所有值为0结果才为0，否则结果为第⼀个⾮0数字
print(a or b) # 1
print(a or c) # 2
print(b or c) # 1