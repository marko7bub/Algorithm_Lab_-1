def selection_sort(arr):
    '''
    Function for sorting arrays using seletion algorithm
    list -> list
    '''
    comparisons = 0
    for i in range(len(arr)): 
        minimal = i
        for j in range(i+1, len(arr)):
            if arr[minimal] > arr[j]:
                comparisons += 1 
                minimal = j
            else:
                comparisons += 1 
        arr[i], arr[minimal] = arr[minimal], arr[i] 
    return arr, comparisons
