#!/usr/bin/env python
#-*- coding: UTF-8 -*-

def test():
        print ("hello, world!")
	print("Hello world!")
	# 列表列表是最通用的 Python 复合数据类型。列表包含在方括号 ([]) 内用逗号分隔，包含的各种数据类型的项目。
	print("列表")		
	list = ["abcd", 789, 2.32, "john", 70.2]
	tinylist = [123, "john"]
	print list #打印列表
	print list[0] #打印列表的第0个元素
	print list[2:] # 打印列表第2个元素开始的所有元素
	print list[1:3] # 打印列表 第1个元素 到 第3个元素
	print tinylist *2 # 打印两次列表
	print tinylist + list # 打印 tinylist 和 list 列表拼接完成之后的新列表
	
	# 元组元组是类似于另一列表序列的数据类型. 元组中由数个逗号分隔每一个值. 不想列表, 元组中括号括起来
	# 元组可以被认为是只读列表
	
	print ("元组")
	tuple = ("abcd", 789, 2.23, "john", 70.2)
	tinytuple = (123, "john")
	print tuple
	print tuple[0]
	print tuple[1:3]
	print tuple[2:]
	print tinytuple * 2
	print tuple + tinytuple
 	
	# 字典 python 的字典是哈希表类型. 他们运作就像关联数组或类似在Perl 中的哈希, 由键值对组成. 
	print ("字典")
	dict = {"one":"john", 2:6734, "dept": "sales"}
	tinydict = {"name":"john", "code":6734, "dept": "sales"}
	print dict["one"]
	print dict[2]
	print tinydict

	print tinydict.keys()
	print tinydict.values()
	
	# for 循环 遍历序列索引
	fruits = ["banna", "apple", "mango"]
	for index in range(len(fruits)):
		print ("Current fruit:" , fruits[index])
		print (index)
		print (fruits[index])
	print ("Good bye!")
	
	#break 语句

	for letter in "Python":
		if letter == "h":
			break;
		print ("Current Letter:",letter)

	var = 10
	while var > 0:
		print ("Current variable value: ", var)
		var = var - 1
		if var == 5:
			break
		print ("GoodBye!")

    	# continue 语句 在Python 中, continue 语句返回控制while循环的开始. continue 语句拒绝执行循环的当前爹地所有剩余的语句, 并移动控制回到循环的顶部(开始位置).
    	# continue 语句 可以在while 和 for 两个循环中使用.
	
	for letter in "Python":
		if letter == "h":
			continue
		print("CurrentLetter ",letter)
	
	var = 10
	
	while var > 0:	
		print ("CurrentVar:",var)
		var -= 1
		if var == 5:
			continue

	print("GoodBye!")


	# pass 语句
	for letter in "Python":
		if letter == "h":
			pass
			print ("This is pass block")
		print ("CurrentLetter:",letter)
	
	print ("GoodBye")

	print(len(range(44, 13000, 89 )))
	
if __name__ == "__main__":
        test()
