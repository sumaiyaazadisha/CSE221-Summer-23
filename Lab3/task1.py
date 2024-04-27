# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JmAOcyQU6-YeKoL08Es7J3eFuk62yjX4
"""

#task-01
input = open('/content/input1.txt', 'r')
output_file = open('/content/output1.txt','w')
N = int(input.readline().strip())
arr = input.readline().strip().split(" ")
array = []
for ele in arr:
  array.append(int(ele))

def mergeSort(array):
    if len(array) == 1:
        return array, 0
    elif len(array) > 1:
        mid = len(array) // 2
        left_part, l_count = mergeSort(array[:mid])
        right_part, r_count = mergeSort(array[mid:])
        merged, t_count = merge(left_part, right_part)
    return merged, l_count + r_count + t_count


def merge(left_part, right_part):
    output = []
    i = 0
    j = 0
    count = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            output.append(left_part[i])
            i += 1
        else:
            output.append(right_part[j])
            j += 1
            count += len(left_part) - i
    output += left_part[i:]
    output += right_part[j:]

    return output, count


print(mergeSort(array)[1], file = output_file)
output_file.close()