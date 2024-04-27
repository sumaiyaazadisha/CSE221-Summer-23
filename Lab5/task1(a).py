# -*- coding: utf-8 -*-
"""task1(a)ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xMkANoZxgOFN3mB6DHguDImgz9izEh-B
"""

#Task-01(a)(DFS)
input = open('/content/input1.txt', 'r')
output = open('/content/output1(a).txt', 'w')
vertex,edge = map(int, input.readline().rstrip().split())
G = {}
for i in range(1, vertex + 1):
    G[i] = []
for x in range(edge):
    v,e = map(int, input.readline().rstrip().split())
    G[v].append(e)

color = ["White"] * (vertex + 1)
start_time = [0] * (vertex + 1)
end_time = [0] * (vertex + 1)
time = 0


def DFS_visit(G, u):
    global time
    time = time + 1
    start_time[u] = time
    color[u] = "Grey"

    for v in G[u]:
        if color[v] == "White":
            DFS_visit(G, v)
    color[u] = "Black"
    time = time + 1
    end_time[u] = time


# for cycle check
def check(V, visited, stack):
    if stack[V] == True:
        return True

    if visited[V] == True:
        return False

    visited[V] = True
    stack[V] = True
    for ver in G[V]:
        if check(ver, visited, stack) == True:
            return True
    stack[V] = False
    return False

def cycle_check(G, Start, Target):
    visited = [False] * (Start + 1)
    stack = [False] * (Start + 1)
    for key in G.keys():
        if check(key, visited, stack) == True:
            return True
    return False


if cycle_check(G, vertex, edge) == True:
    print("IMPOSSIBLE", file = output)
else:
    for key in G.keys():
        if color[key] == "White":
            DFS_visit(G, key)

    for i in range(1, len(end_time)):
        m = max(end_time)
        l = end_time.index(m)
        print(l, end=" ", file = output)
        end_time[l] = 0

output.close()