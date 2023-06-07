import time
import os
from platform import system

#CLEAR TERMINAL
def clear_terminal():
    # Clear command for Windows
    if system() == 'Windows':
        os.system('cls')
    # Clear command for Unix-based systems (Linux, macOS)
    else:
        os.system('clear')


#SELECTION SORT
def selection_sort(array):
    start_time = time.time()
    length = len(array)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if array[k] < array[least]:
                least = k
        array[least], array[i] = (array[i], array[least])
    end_time = time.time()
    execution_time = end_time - start_time
    print('-'*50)
    print(f"Tempo de execução no \033[7;33;46mSelection Sort\033[m: {execution_time} segundos.")
    print('-'*50)
    return array

#BUBBLE SORT
def bubble_sort(array):
    start_time = time.time()
    n = len(array)
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(n - 1 - i):
            # Swap adjacent elements if they are in the wrong order
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    end_time = time.time()
    execution_time = end_time - start_time
    print('-'*50)
    print(f"Tempo de execução no \033[7;32;46mBubble Sort\033[m: {execution_time} segundos.")
    print('-'*50)
    return array

#INSERTION SORT
def insertion_sort(array):
 
    start_time = time.time()
    length=len(array)
    for i in range(1,length):
        key=array[i]
        j=i-1
        while(j>=0 and array[j]>key):
            array[j + 1] = array[j]
            j=j-1
        array[j+1]=key
    end_time = time.time()
    execution_time = end_time - start_time
    print('-'*50)
    print(f"Tempo de execução no \033[7;35;46mInsertion Sort\033[m: {execution_time} segundos.")
    print('-'*50)
    return array


#MERGE SORT
def merge_sort(array):

        #start_time = time.time()
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            merge_sort(left)
            merge_sort(right)
            i = 0
            j = 0
            
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
            
                k += 1
                
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k]=right[j]
                j += 1
                k += 1
                
#QUICK SORT

def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high] # pivot element
   for j in range(low , high):
      # If current element is smaller
      if arr[j] <= pivot:
         # increment
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )
# sort
def quick_sort(array,low,high):
    
    if low < high:
        # index
        pi = partition(array,low,high)
        # sort the partitions
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)

    


clear_terminal()
file_path = 'c:/Users/kenny/Documents/Projeto Python/UFPB/Estrutura_de_Dados/instancias-num/num.1000.4.in'  # Replace with the actual file path

try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        numbers = [int(num) for num in file_contents.split() if num.isdigit()]
        #print(numbers)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"An error occurred while reading the file.")


para_selection_sort = selection_sort(numbers)
para_bubble_sort = bubble_sort(numbers)
para_insertion_sort = insertion_sort(numbers)

#SOMATÓRIA DO TEMPO PARA O MERGE SORT
start_time = time.time()
para_merge_sort = merge_sort(numbers)
end_time = time.time()
execution_time = end_time - start_time
print('-'*50)
print(f"Tempo de execução no \033[7;36;46mMerge Sort\033[m: {execution_time} segundos.")
print('-'*50)

start_time = time.time()
para_quick_sort = quick_sort(numbers, 0, len(numbers)-1)
end_time = time.time()
execution_time = end_time - start_time
print('-'*50)
print(f"Tempo de execução no \033[7;37;46mQuick Sort\033[m: {execution_time} segundos.")
print('-'*50)