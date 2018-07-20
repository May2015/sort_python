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

	def insert_sort(self):
		length = len(self.r)
		lis = self.r
		for j in range(1,length):
			i = j-1

			while lis[i] > lis[i+1] and i >= 0:
					self.swap(i, i+1)
					i -= 1





	def __str__(self):
		ret = ''
		for i in self.r:
			ret += " %s"%i
		return ret

if __name__ == '__main__':
	sqlist = SQList([4,1,7,3,8,5,9,5,2,6])
	print(sqlist)
	sqlist.insert_sort()
	print(sqlist)
