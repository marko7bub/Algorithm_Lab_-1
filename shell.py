def shell_sort(arr): 
    '''
    Function for sorting arrays using shell algorithm
    list -> list
    '''
    comparisons = 0
    n = len(arr) 
    gap = n//2
    while gap > 0: 
        comparisons += 1
        for i in range(gap, n):
            comparisons += 1 
            temp = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] > temp: 
                comparisons += 1
                arr[j] = arr[j-gap] 
                j -= gap 
            arr[j] = temp 
        gap //= 2
    return arr, comparisons

