#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# 定义一个函数
## 可以定义函数, 已提供所需的功能. 下面是在Python 定义一个函数的简单规则:
### 函数块首先以 def 关键字后跟函数名 和括号 (())
### 任何输入参数 或参数 应放在这些括号内. 还可以定义一些括号内的参数.
### 函数的第一个语句 可以是 一个可选的声明- 函数的文档字符串或文档字符串.
### 每个函数中的代码块用 冒号(:)开始和缩进.
### 该语句返回[表达]退出函数, 可选地传递回一个表达式给调用者. 不带参数的 return 语返回 None 是一样的 

def printme(str):
	str += "___hello world"
	print (str)
	return

# Python 模块
## 模块允许在逻辑上组织Python代码. 将相关代码放到一个模块使嗲吗更容易理解和使用.
## 模块可以绑定和产考任意命名的属性的 Python对象/
## 简单的说, 一个模块是由Python代码的文件组成. 模块可以定义函数, 类 和变量. 模块也可以包括可运行的代码. 






if __name__ == "__main__":
        printme ("I'm first call to user defined funcation!")






