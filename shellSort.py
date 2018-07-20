#!/usr/bin/python
# -*- coding:utf-8 -*-
# Python 3.6


class SQList:
	def __init__(self, lis=None):
		self.r = lis

	def shell_sort(self):
		lis = self.r
		length = len(lis)
		increment = length

		while increment > 1:
			increment = int(increment/3)+1
			for i in range(increment, length):
				if lis[i] < lis[i-increment]:
					temp = lis[i]
					j = i - increment
					while j >= 0 and temp < lis[j]:
						lis[j+increment] = lis[j]
						j -= increment
					lis[j+increment] = temp
	


	def __str__(self):
		ret = ''
		for i in self.r:
			ret += " %s"%i
		return ret

if __name__ == '__main__':
	sqlist = SQList([4,1,7,3,8,5,9,5,2,6])
	sqlist.shell_sort()
	print(sqlist)
