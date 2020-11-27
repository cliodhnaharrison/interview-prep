#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bubblesort(a):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        last_unsorted = len(a)- 1
        for i in range(last_unsorted):
            if a[i] > a[i+1]:
                tmp = a[i+1]
                a[i+1] = a[i]
                a[i] = tmp
                is_sorted = False
        last_unsorted -= 1

    return a

print(bubblesort([10, 3, 5, 12, 9, 20]))
