#!/usr/bin/env python
#coding: utf-8

def test():
        print ("hello, world!")
	
	print ("你好, 世界!")

	# for 循环 遍历序列索引
	fruits = ["banna", "apple", "mango"]
	for index in range(len(fruits)):
		print ("Current fruit:" , fruits[index])
		print (index)
		print (fruits[index])
	print ("Good bye!")

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
	
	
if __name__ == "__main__":
        test()
