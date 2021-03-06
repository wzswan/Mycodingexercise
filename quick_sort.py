# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:42:59 2016

@author: wzswan
"""

def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(list, low, left - 1)
    quick_sort(lists, left + 1,high)
    reutrn lists