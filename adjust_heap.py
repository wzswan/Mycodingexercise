# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:26:51 2016

@author: wzswan
"""

def adjust_heap(lists, i, size):
    lchid = 2 * i + 1
    rchid = 2 * i + 2
    max = i
    if i < size / 2:
        if lchid < size and lists[lchild] > lists[maxs]:
            max = lchid
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)
        
def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)