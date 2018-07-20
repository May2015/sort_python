#!/usr/bin/python
# -*- coding:utf-8 -*-
# Python 3.6


class SQList:
	def __init__(self, lis=None):
		self.r = lis

	def swap(self, i, j):
		tmp = self.r[i]
		self.r[i] = self.r[j]
		self.r[j] = tmp

	def select_sort(self):
		length = len(self.r)
		lis = self.r

		for i in range(length):
			min_num = self.r[i]
			min_index = i
			for j in range(i+1, length):
				if lis[j] < min_num:
					min_num = lis[j]
					min_index = j
			self.swap(i, min_index)


	def __str__(self):
		ret = ''
		for i in self.r:
			ret += " %s"%i
		return ret

if __name__ == '__main__':
	sqlist = SQList([4,1,7,3,8,5,9,5,2,6])
	print(sqlist)
	sqlist.select_sort()
	print(sqlist)
