#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# 创建类
## class 语句创建一个新的类定义. 类的名称紧跟在关键字class后, 接着又跟一个冒号.

class Employee:
	def __init__(self, name, empCount):
		self.name = name
		self.empCount = empCount

	def str(self):
		return self.name, self.empCount

	def displayEmployee(self):
		print (self.name)
		return

emp1 = Employee("mamam",100)

emp2 = Employee("soul", 200)

#print ( emp2.str())

#emp1.name = "mamam"

#emp2 = Employee("Manni", 5000)

#emp1.displayEmployee()


#print ("Total Employee %d"%Employee.empCount)

# 类继承 

class Parent: 
	def myMethod(self):
		print("Calling parent method")
		return


class Child(Parent):
	def myMethod(self):
		print("Calling child method")
		return


c = Child()

c.myMethod()




# 运算符重载 __init__(self[,args...]): 构造函数(参数可选) obj = className(args)
# __del__(self) 析构函数, 删除对象 dell obj
# __repr__(self) 求值的字符串表示  repr(obj)
# __str__(self) 打印字符串表示  str(obj)
# __cmp__(self, x) 对象比较  cmp(obj, x)

class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b

#	def __str__(self):
#		return "Vector(%d,%d)"%(self.a, self.b)

	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)

v2 = Vector(5, -2)

#print v1 + v2 

#str(v1)



# 数据隐藏 一个对象的属性可以或不可以在类定义外部可见. 对于这些情况, 可以命名以双下划线前缀属性, 这些属性将不会直接外部可见:

class JustCounter:
	__secretCount = 0

	def count(self):
		self.__secretCount += 1
		print (self.__secretCount)

counter = JustCounter()

#counter.count()
#counter.count()

#print counter.__secretCount  打印不出来 出错 AttributeError: JustCounter instance has no attribute '__secretCount'

# 正则表达式 是字符的特殊序列, 可以帮助匹配或查找其他字符串或设置字符串, 使用模式在特殊的语法. 正则表达式被广泛应用于 UNIX 的世界.
# Python 中的模块re 提供了Perl般的正则表达式的全面支持. 如果在编译或使用正则表达式时发生错误,re模块引发异常 re.error.
# 我们将包括在其中将用于处理的正则表达式的两个重要功能. 但是, 首先: 当他们在正则表达式中使用这些字符将有特殊的含义. 为了避免任何混乱当使用正则表达式处理时, 我们会用原始字符串为 r'expression'.

#match 函数 
# 此函数尝试重新模式匹配字符串并可选标准(flags).
# re.match(pattern, string, flags = 0)
# 参数说明: 
# pattern : 这是正则表达式将要匹配
# string : 这是一个僬侥搜索匹配的模式的字符串
# flags : 可以以互斥指定不同的标志 OR(|). 这些事用于下表中的修辞符.

#re.match 函数成功返回匹配对象, 失败返回None. 我们可以使用group(num) 或 groups()匹配对象的函数来获取匹配的表达式. 
# group(num = 0) 这个方法返回整个匹配(或指定分组num) 
# groups() 方法返回所有的子组中的一个元组(空, 如果没有发现任何)

# search 函数
# 此函数查找字符串内使用可选的标志第一次出现的RE 模式. 
# re.search(patter, string, flags=0)
# 同match








