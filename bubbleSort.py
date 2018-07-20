#!/usr/bin/python
# -*- coding:utf-8 -*-
# Python 3.6


class SQList:
	def __init__(self, lis=None):
		self.r = lis

	def swarp(self, i, j):
		tmp = self.r[i]
		self.r[i] = self.r[j]
		self.r[j] = tmp

	def bubble_sort_simple(self):
		lis = self.r
		length = len(self.r)
		for i in range(length):
			for j in range(i+1,length):
				if lis[i] > lis[j]:
					self.swarp(i, j)

	def bubble_sort_advance(self):
		lis = self.r
		length = len(self.r)
		flag = True
		i = 0
		while i < length and flag:
			flag = False
			j = length-2
			while j >= i:
				if lis[j] > lis[j+1]:
					self.swarp(j, j+1)
					flag = True
				j -= 1
			i += 1

	def __str__(self):
		ret = ''
		for i in self.r:
			ret += " %s"%i
		return ret

if __name__ == '__main__':
	sqlist = SQList([4,1,7,3,8,5,9,5,2,6])
	print(sqlist)
	#sqlist.bubble_sort_simple()
	sqlist.bubble_sort_advance()
	print(sqlist)
