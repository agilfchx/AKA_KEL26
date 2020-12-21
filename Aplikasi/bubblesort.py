import time
from numpy import random
import os

os.system("cls")
panjang = int(input("Masukkan Panjang Array-nya: "))

#Awal Timer
start = time.time()

#Bubble Sort Code
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

#Proses Pemasukan Sorting
data = random.randint(1000,size=(panjang))
print("Index Sebelum di Sorting", data)
bubbleSort(data) 

#Berakhirnya Timer
end = time.time()

#Output
print ("Index Setelah di Sorting", data)  
print(f"Running Time Bubble Sort dengan panjang", panjang, "adalah", end - start)