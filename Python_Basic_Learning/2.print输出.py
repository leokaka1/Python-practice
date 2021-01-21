"""
基本输出
"""
print("Today is very perfect day!")

"""
带1变量输出
"""
test = "day!"
print("Today is very perfect {0}".format(test))

"""
带多变量输出
"""
test1 = "Today"
test2 = "very"

print("{0} is {1} perfect day!".format(test1,test2))

"""
带变量第二种写法
%s : 字符串
%d : 整型
%f : 浮点型
"""
test1 = 123
test2 = "test"
print("说%d,但是这只是个%s"%(test1,test2))