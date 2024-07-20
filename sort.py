from random import random

size = 10
l = [random()*1000//1 for _ in range(size)]

def sort(l: list):
    for i in range(size-1, 0, -1):
        index = 0
        for j in range(0, i+1):
            if l[j] > l[index]:
                index = j
        tmp = l[index]
        l[index] = l[i]
        l[i] = tmp

print(l)
sort(l)
print(l)
###