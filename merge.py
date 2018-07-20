#!/usr/bin/python
# -*- coding:utf-8 -*-
# Python 3.6


def merge(a, b):
	c = []
	h = j = 0
	while j < len(a) and h < len(b):
		if a[j] < b[h]:
			c.append(a[j])
			j += 1
		else:
			c.append(b[h])
			h += 1

	if j == len(a):
		for i in b[h:]:
			c.append(i)
	else:
		for i in a[j:]:
			c.append(i)
	return c



def merge_sort(lists):
	if len(lists) <=1:
		return lists
	middle = int(len(lists)/2)
	left = merge_sort(lists[:middle])
	right = merge_sort(lists[middle:])
	return merge(left, right)

if __name__ == '__main__':
	arr = [4,8,1,2,6,5,4,5,8,7,9,10]
	print(merge_sort(arr))