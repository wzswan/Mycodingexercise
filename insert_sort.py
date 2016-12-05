# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:03:37 2016

@author: wzswan
"""

def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i -1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
             j -= 1
    return lists