from locale import currency
import numpy as np
import pandas as pd

def find_greatest_product_of_contiguous_integers(matrix, contiguous_integers):
    # Initilization of result
    max_prod = 1

    # Converting the input matrix into a numpy array
    a = np.array(matrix)
    
    # Flattening out the numpy array so that it can be easy for multiplication
    a = a.flatten()

    n = len(a)
    print(n)
    # Length of flattened array must be greater than the contiguous_integers
    if(n<contiguous_integers):
        print("Invalid")
        return -1


    for i in range(n - contiguous_integers + 1):
        val_arr = []
        current_prod = 1
        for j in range(contiguous_integers):
            current_prod = current_prod * a[i+j]
            val_arr.append(a[i+j])


        max_prod = max(current_prod, max_prod)

    return max_prod, val_arr


df = pd.read_csv('TechConsultingTestGrid.csv', header=None)
max_prod, val_arr = find_greatest_product_of_contiguous_integers(df, 3)
print(max_prod)
print(val_arr)
