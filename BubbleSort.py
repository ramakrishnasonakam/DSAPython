def BubbleSort(a):
    for i in range(len(a)):
        swapped = False
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

if __name__  == '__main__':
    n = int(input("Enter the size of the array: "))
    a = [int(input(f"Enter the {x+1} element: ")) for x in range(n)]
    sortedArr = BubbleSort(a)
    print(sortedArr)
