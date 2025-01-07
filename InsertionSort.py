def InsertionSort(a):
    for i in range(1, len(a)):
        j = i #Setting j from index 1 (second value) of the array, assuming the index 0 (first value)
              #is already sorted
              '''
              Assuming the idx 0 (first value) is already sorted, we traverse from idx 1 (second value).
              In the first 'while' iteration, j = idx 1 (value=8), 8 and 2 are compared.
              Since 2 < 8, while condition is not met. 
              Code goes out of while loop and i increments to 2.
              In the second 'for' iteration, i = 2, j = 2, a[j] = 5.  
              Code enters 'while' loop. j > 0 and a[1]==8 > a[2]. Hence, swap happens.
              But unlike iteration 1, j is idx 2. It has 2 values to compare itself to. 
              Hence, j is decremented by 1.
              And the comparison condition is checked for again.   
              '''
        while j > 0 and a[j-1] > a[j]: 
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
    return a

if __name__ == '__main__':
    n = int(input("Enter the size of the array: "))
    a = [int(input(f"Enter the {i+1} element: ")) for i in range(n)]
    sortedArr = InsertionSort(a)
    print(sortedArr)