#!/usr/bin/env python
#-*- coding: UTF-8 -*-


# 导入hello.py 文件 和 

import hello
import pythontest
import pythondef

#hello.print_func("World")

# Python 读写文件 
# 1.打开文件 使用 open 打开文件后, 一定要记得调用文件对象的close()方法,比如可用try/finally 语句来确保最后能关闭文件. 

file_object = open("testfile")

print(file_object.name)

try:
	all_the_test = file_object.read()
	hello.print_func(all_the_test)
finally:
	file_object.close()


#2. 读文件 读文本文件
input = open("data","r")

# 第二个属性默认为r
input = open("data")

# 读二进制文件 
input = open("data","rb")

# 读取所有内容
file_object = open("thefile.txt")

try:
#	print (file_object.readline())
#	print(file_object.encoding)
	all_the_test = file_object.read()
#       hello.print_func(all_the_test)
finally:
        file_object.close()


# 读取固定字节
file_object = open("abinfile","rb")

try:
	while True:
		chunk = file_object.read(100)
#		hello.print_func(chunk)
		if not chunk:
			break
#		print("not chunk:", chunk)
finally:
	file_object.close()



# 写文件 写文本文件
output = open("data","w")

# 写二进制文件 
output = open("data","wb")

# 追加写文件
output = open("data","w+")

#写数据 

all_the_text = "1.打开文件 使用 open 打开文件后, 一定要记得调用文件对象的close()方法,比如可用try/finally 语句来确保最后能关闭文件."

file_object = open("thefile.tex","w+")

#print (file_object.readline())

file_object.write(all_the_text)

file_object.writelines(all_the_text)
print (file_object.readline())

file_object.close


