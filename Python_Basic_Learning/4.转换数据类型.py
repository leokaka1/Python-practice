"""
⼀. 转换数据类型的作⽤
int(x [,base ])             将x转换为⼀个整数
float(x )                   将x转换为⼀个浮点数
complex(real [,imag ])      创建⼀个复数，real为实部，imag为虚部
str(x )                     将对象 x 转换为字符串
tuple(s )                   将序列 s 转换为⼀个元组
list(s )                    将序列 s 转换为⼀个列表
"""

# 1. 接收用户输入
num = input("请输入您的幸运数字")

# 2. 打印结果
print("您的幸运数字是{0}".format(num))

# 3. 检测接收用户输入类型
print(type(num))

# 4. 转换数据类型为整型
print(type(str(num)))


# 1. float() -- 转换成浮点型
num1 = 1
print(float(num1))
print(type(float(num1)))

# 2. str() -- 转换成字符串类型
num2 = 10
print(type(str(num2)))

# 3. tuple() -- 将⼀个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))

# 4. list() -- 将⼀个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))
print(type(list(t1)))

# 5. eval() -- 将字符串中的数据转换成Python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
