# coding=utf-8
import random
import string
class NimClass(object):
	def __init__(self):
		pass
 
	def Get_random_string(self):
		"""
		返回随机字符串=“0-10000中的随机记数字“+”两个随机字母“，用法：
		
		| ${string} | Get_random_string |
		"""
		letterlist=[]
		letterlist.append(str(random.randint(0,10000)))
		for i in range(0,2):
			letterlist.append(chr(random.randint(97, 122)))
		letter_string=''.join(letterlist)
		return letter_string