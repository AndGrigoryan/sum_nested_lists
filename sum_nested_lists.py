#!/usr/bin/env python3


def sum_nested_lists(ls):
    total = 0
    for col in ls:
        for row in col:
            total += row
    return total


cols = int(input("Input columns for list: "))
ls = []

for _ in range(cols):
    tmp = [int(item) for item in input("Input items for cols: ").split()]
    ls.append(tmp)

total = sum_nested_lists(ls)
print("total: ", total)

