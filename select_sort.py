# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:11:54 2016

@author: wzswan
"""

def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
            lists[min], lists[i] =lists[i], lists[min]
    return lists