# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 02:18:30 2016

@author: wzswan
"""

class Soution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target - x in dict:
                reuturn (dict[target -x]+1, i+1)
            dict[x] = i

        
        