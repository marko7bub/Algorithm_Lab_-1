def insertion_sort(arr): 
    '''
    Function for sorting arrays using insertion algorithm
    list -> list
    '''
    comparisons = 0
    for i in range(1, len(arr)): 
        marker = arr[i] 
        j = i-1
        check = 0
        while j >= 0 and marker < arr[j]:
            comparisons += 1
            check += 1
            arr[j + 1] = arr[j] 
            j -= 1
        if check == 0:
            comparisons += 1
        arr[j + 1] = marker
    return arr, comparisons
