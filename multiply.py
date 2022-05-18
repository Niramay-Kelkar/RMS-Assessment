import numpy as np
import pandas as pd

def main():
    # Used for testing purposes
    # df = pd.read_csv('TechConsultingTestGrid.csv', header=None)
    # find_greatest_product_of_contiguous_integers(df, 3)

def find_greatest_product_of_contiguous_integers(matrix, num):
    # Converting the input matrix into a numpy array
    arr = np.array(matrix)

    #Finding the row and column count
    rows, cols = arr.shape

    # Reshaping the numpy array into a matrix
    arr = np.reshape(arr, (rows, cols))

    # Checking if the matrix is empty
    if not np.any(arr) :
        print("Matrix is Empty")
        return -1
    # Checking if the contiguous number entered is valid or not
    elif num == None or num == 0:
        print("Invalid")
        return -1
    else:
        # Initializing variables
        curr_prod = 0
        curr_itr = 0
        right = 0
        numbers = 0
        down = 0
        numdown = 0
        left = 0
        numleft = 0
        rightDiag = 0
        numright = 0
        up = 0
        numup = 0

        # Fetching the greatest product from right adjacent
        right, numbers = findRightAdjacent(arr, num, rows, cols)

        # Fetching the greatest product from down adjacent
        down, numdown = findDownAdjacent(arr, num, rows, cols)

        # Fetching the greatest product from left diagonally
        leftDiag, numleft = findLeftDiagonal(arr, num, rows, cols)

        # Fetching the greatest product from right diagonally
        rightDiag, numright = findRightDiagonal(arr, num, rows, cols)

        up, numup = findUpAdjacent(arr, num, rows, cols)
        print(up, numup)

        # Fetching the maximum product from all the combinations
        curr_prod = max(right, down, leftDiag, rightDiag)

        # Fetching the number combination for the maximum product
        if curr_prod == right:
            curr_itr = numbers
        elif curr_prod == down:
            curr_itr = numdown
        elif curr_prod == leftDiag:
            curr_itr = numleft
        elif curr_prod == rightDiag:
            curr_itr = rightDiag
        else:
            curr_itr = -1

        print(f"The greatest product in all directions is: {curr_prod}")
        print(f"The number which gives the greatest product are: {curr_itr}")
            
'''
The function accepts following parameters
@param1 : matrix for computation
@param2 : contiguous number 
@param3 : number of rows in the matrix
@param4 : number of columns in the matrix

Searches diagonally in the down direction from the current number
'''
def findDownAdjacent(arr, num, rows, cols):
    curr_prod = 0
    curr_itr = 0
    for i in range(rows):
        for j in range(cols-num+1):
            numbers = arr[j:j+num, i]
            prod = np.prod(numbers)

            if prod > curr_prod:
                curr_prod = prod
                curr_itr = numbers
    return curr_prod, curr_itr

'''
The function accepts following parameters
@param1 : matrix for computation
@param2 : contiguous number 
@param3 : number of rows in the matrix
@param4 : number of columns in the matrix

Searches diagonally in the upper direction from the current number
'''
def findUpAdjacent(arr, num, rows, cols):
    curr_prod = 0
    curr_itr = 0
    for i in range(rows-num+1):
        for j in range(cols):
            numbers = arr[j:j+num, i]
            prod = np.prod(numbers)

            if prod > curr_prod:
                curr_prod = prod
                curr_itr = numbers
    return curr_prod, curr_itr

'''
The function accepts following parameters
@param1 : matrix for computation
@param2 : contiguous number 
@param3 : number of rows in the matrix
@param4 : number of columns in the matrix

Searches diagonally in the left direction from the current number
'''
def findLeftDiagonal(arr, num, rows, col):
    curr_prod = 0
    curr_itr = 0
    for i in range(rows * -1, col, 1):
        leftdiag = arr.diagonal(offset=i)

        if len(leftdiag) > num:
            for i in range(len(leftdiag)-num-1):
                sub_diagonal = leftdiag[i: i+num]
                prod = np.prod(sub_diagonal)
                if prod > curr_prod:
                    curr_prod = prod
                    curr_itr = sub_diagonal
            return curr_prod, curr_itr

        elif len(leftdiag) == num:
            prod = np.prod(leftdiag)
            if prod > curr_prod:
                curr_prod = prod
                curr_itr = leftdiag
            return curr_prod, curr_itr
    
'''
The function accepts following parameters
@param1 : matrix for computation
@param2 : contiguous number 
@param3 : number of rows in the matrix
@param4 : number of columns in the matrix

Searches diagonally in the right direction from the current number
'''
def findRightDiagonal(arr, num, rows, col):
    curr_prod = 0
    curr_itr = 0
    flipped = np.fliplr(arr)
    for i in range(rows * -1, col, 1):
        rightdiag = flipped.diagonal(offset=i)

        if len(rightdiag) > 3:
            for i in range(len(rightdiag)-2):
                sub_diagonal = rightdiag[i: i+3]
                prod = np.prod(sub_diagonal)
                if prod > curr_prod:
                    curr_prod = prod
                    curr_itr = sub_diagonal
            return curr_prod, curr_itr

        elif len(rightdiag) == 3:
            prod = np.prod(rightdiag)
            if prod > curr_prod:
                curr_prod = prod
                curr_itr = rightdiag
            return curr_prod, curr_itr

'''
The function accepts following parameters
@param1 : matrix for computation
@param2 : contiguous number 
@param3 : number of rows in the matrix
@param4 : number of columns in the matrix

Searches diagonally in the right direction from the current number
'''
def findRightAdjacent(arr, num, rows, cols):
    curr_prod = 0
    curr_itr = 0
    for i in range(rows):
        for j in range(cols-num+1):
            numbers = arr[i, j:j+num]
            prod = np.prod(numbers)
    
            if prod > curr_prod:
                curr_prod = prod
                curr_itr = numbers
    return curr_prod, curr_itr

if __name__ == '__main__':
    main()
