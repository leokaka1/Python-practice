"""
去空格或者特殊符号
"""
from filecmp import cmp

s = " hello , world !"
print(s.strip())
print(s.lstrip())
print(s.rstrip())


"""
连接字符串
"""
sStr1 = "strcat"
sStr2 = "append"
sStr1 += sStr2
print(sStr1)

"""
查找字符串
"""
sStr1 = "strchr"
sStr2 = "r"
nPos = sStr1.index(sStr2)
print(nPos)

"""
字符串比较
"""
sStr1 = "strchr"
sStr2 = "strch"


