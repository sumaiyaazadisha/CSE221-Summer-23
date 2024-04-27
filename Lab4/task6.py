# -*- coding: utf-8 -*-
"""task6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y9nXmvYW9c63a-L1-efgk1klmyzNGCGe
"""

#task06
input = open("/content/input6.txt", 'r')
list1 = input.readline().strip().split()
R = int(list1[0])
C = int(list1[1])
array = []
for line in input:
    array.append([i for i in line.rstrip()])


def dfs(k, j):
    global columns, rows
    if k < 0 or k >= R or j < 0 or j >= C:
        return
    elif array[k][j] == '#':
        return
    else:
        if array[k][j] == 'D':
            global diamonds
            diamonds += 1
        array[k][j] = '#'
        dfs(k + 1, j)
        dfs(k - 1, j)
        dfs(k, j + 1)
        dfs(k, j - 1)


def FloodFill():
    global rows, columns, diamonds
    diamondsArray = []
    for val1 in range(R):
        for val2 in range(C):
            diamonds = 0
            if array[val1][val2] != "#":
                dfs(val1, val2)
                diamondsArray.append(diamonds)
    return diamondsArray


maximum_Diamonds = max(FloodFill())
print(maximum_Diamonds)