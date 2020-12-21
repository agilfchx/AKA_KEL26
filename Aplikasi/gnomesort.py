import time
from numpy import random
import os

os.system("cls")
panjang = int(input("Masukkan Panjang Array-nya: "))

#Awal Timer
start = time.time()

#Gnome Sort Code
def gnomeSort(arr, n): 
    index = 0
    while index < n: 
        if index == 0: 
            index = index + 1
        if arr[index] >= arr[index - 1]: 
            index = index + 1
        else: 
            arr[index], arr[index-1] = arr[index-1], arr[index] 
            index = index - 1
  
    return arr 

#Proses Pemasukan Sorting
data = random.randint(1000,size=(panjang))
n = len(data)
print("Index Sebelum di Sorting :",data)
arr = gnomeSort(data, n) 

#Berakhirnya Timer
end = time.time()

#Output
print ("Index Setelah di Sorting :",data)
print(f"Running Time Gnome Sort dengan panjang ", panjang, "adalah", end - start)