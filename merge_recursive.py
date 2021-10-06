merge_counter = 0

def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    global merge_counter
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            merge_counter += 1
            result.append(left[i])
            i+= 1
        else:
            merge_counter += 1
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
 
    return result
 
def merge_sort(list):
    '''
    Function for sorting arrays using merge algorithm
    list -> list
    '''
    if len(list) < 2:
        return list
 
    middle = len(list)//2

    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    
    return merge(left, right)