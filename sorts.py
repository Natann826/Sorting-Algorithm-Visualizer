import random as r

# All of this is stolen from geeksforgeeks.org because i SUCK at developing searches

def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        
        list[i], list[min_index] = list[min_index], list[i]
        yield list


def insertionSort(arr):
 
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        yield arr


def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        yield arr
            

 