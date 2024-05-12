def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        
        sorted_less = quick_sort(less_than_pivot)
        sorted_greater = quick_sort(greater_than_pivot)
        
        sorted_arr = sorted_less + [pivot] + sorted_greater
        print("Sorting:", sorted_arr)
        return sorted_arr

# 講義的demo data:
demo_data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
sorted_data = quick_sort(demo_data)
print("Sorted array:", sorted_data)


# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:17:07 2024

@author: jxc
"""

