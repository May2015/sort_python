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

	def quick_sort(self):
		self.qsort(0, len(self.r)-1)

	def qsort(self, low, high):
		if low < high:
			pivot = self.partition(low, high)
			self.qsort(low, pivot-1)
			self.qsort(pivot+1, high)

	def partition(self, low, high):
		lis = self.r
		pivot_key = lis[low]
		i = low
		j = high

		while i < j:
			while i < j and lis[j] >= pivot_key:
				j -= 1
			self.swap(i, j)
			while i < j and lis[i] <= pivot_key:
				i += 1
			self.swap(i, j)
		return i




	def __str__(self):
		ret = ''
		for i in self.r:
			ret += " %s"%i
		return ret

if __name__ == '__main__':
	sqlist = SQList([4,1,7,3,8,5,9,5,2,6])
	sqlist.quick_sort()
	print(sqlist)



