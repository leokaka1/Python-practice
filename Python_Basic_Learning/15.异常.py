"""
异常的写法
语法
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""

try:
    f = open("./File/test.txt",'r')
except:
    f = open("./File/test.txt","w")

"""
捕获指定的异常
语法
try:
    可能发生错误的代码
except 异常类型:
    如果捕获到该异常执行的代码
"""

try:
    print(num)
except NameError:
    print("有错误")

"""
捕获多个异常
"""
try:
    print( 1/ 0)
except(NameError,ZeroDivisionError):
    print("有错误")


"""
捕获异常描述信息
"""
try:
    print(num)
except(NameError,ZeroDivisionError) as result:
    print(result)

"""
捕获所有异常
"""
try:
    print(num)
except Exception as result:
    print(result)

"""
异常的else
表示没有异常执行的代码
"""

try:
    print(1)
except Exception as result:
    print(result)
else:
    print("没有异常")

"""
异常的finally
"""
try:
    f = open("./File/test.txt","r")
except Exception as result:
    f = open("./File/test.txt","w")
else:
    print("没有异常")
finally:
    f.close()


