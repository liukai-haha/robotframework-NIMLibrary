# coding=utf-8
import random
import string
import os
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
	def run_python_script(self,filepath):
		"""
		传入python脚本文件路径，运行该脚本，用法事例(注意！！！路径中请用双斜杠，不要问我为什么)：
		|run_python_script|D:\\\\test.py|
		"""
		#os.system("python C:\\Users\\hzliukai1\\Desktop\\IM_Script\\IMwebsite_md5check.py")
		#execfile('C:\\Users\\hzliukai1\\Desktop\\IM_Script\\IMwebsite_md5check.py')
		dir='python'+' '+filepath
		print dir
		os.system(dir)
