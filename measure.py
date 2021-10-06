import random
import insertion
import selection
import shell
import time

for i in range(1, 5):
    for j in range(7, 16):
        arr = []
        arr1 = []
        arr2 = []
        arr3 = []
        if i == 1:
            for s in range(2**j):
                arr.append(random.randint(0, 101))
        if i == 2:
            for s in range(2**j):
                arr.append(random.randint(0, 101))
            arr = sorted(arr)
        if i == 3:
            for s in range(2**j):
                arr.append(random.randint(0, 101))
            arr = sorted(arr)
            arr.reverse()
        if i == 4:
            for s in range(2**j):
                arr1.append(random.randint(1, 3))
                arr2.append(random.randint(1, 3))
                arr3.append(random.randint(1, 3))
        original_arr = tuple(arr)
        original_arr1 = tuple(arr1)
        original_arr2 = tuple(arr2)
        original_arr3 = tuple(arr3)
        for k in ["selection", "insertion", "merge", "shell"]:
            if k == "selection":
                if i == 4:
                    start1 = time.time()
                    sorted_arr, comparisons1 = selection.selection_sort(arr1)
                    end1 = time.time()
                    start2 = time.time()
                    sorted_arr, comparisons2 = selection.selection_sort(arr1)
                    end2 = time.time()
                    start3 = time.time()
                    sorted_arr, comparisons3 = selection.selection_sort(arr1)
                    end3 = time.time()
                    runtime = round((end1 - start1 + end2 - start2 + end3 - start3)/3, 6)
                    comparisons = (comparisons1 + comparisons2 + comparisons3)/3
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in time: {}".format(
                            i, 2**j, k, runtime))
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in comparisons: {}".format(
                            i, 2**j, k, comparisons))
                    arr1 = list(original_arr1)
                    arr2 = list(original_arr2)
                    arr3 = list(original_arr3)
                else:
                    start = time.time()
                    sorted_arr, comparisons = selection.selection_sort(arr)
                    end = time.time()
                    runtime = round(end - start, 6)
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in time: {}".format(
                            i, 2**j, k, runtime))
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in comparisons: {}".format(
                            i, 2**j, k, comparisons))
                    arr = list(original_arr)
            if k == "insertion":
                if i == 4:
                    start1 = time.time()
                    sorted_arr, comparisons1 = insertion.insertion_sort(arr1)
                    end1 = time.time()
                    start2 = time.time()
                    sorted_arr, comparisons2 = insertion.insertion_sort(arr1)
                    end2 = time.time()
                    start3 = time.time()
                    sorted_arr, comparisons3 = insertion.insertion_sort(arr1)
                    end3 = time.time()
                    runtime = round((end1 - start1 + end2 - start2 + end3 - start3)/3, 6)
                    comparisons = (comparisons1 + comparisons2 + comparisons3)/3
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in time: {}".format(
                            i, 2**j, k, runtime))
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in comparisons: {}".format(
                            i, 2**j, k, comparisons))
                    arr1 = list(original_arr1)
                    arr2 = list(original_arr2)
                    arr3 = list(original_arr3)
                else:
                    start = time.time()
                    sorted_arr, comparisons = insertion.insertion_sort(arr)
                    end = time.time()
                    runtime = round(end - start, 6)
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in time: {}".format(
                            i, 2**j, k, runtime))
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in comparisons: {}".format(
                            i, 2**j, k, comparisons))
                    arr = list(original_arr)
            if k == "merge":
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
                
                if i == 4:
                    start1 = time.time()
                    sorted_arr = merge_sort(arr1)
                    end1 = time.time()
                    start2 = time.time()
                    sorted_arr = merge_sort(arr1)
                    end2 = time.time()
                    start3 = time.time()
                    sorted_arr = merge_sort(arr1)
                    end3 = time.time()
                    runtime = round((end1 - start1 + end2 - start2 + end3 - start3)/3, 6)
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in time: {}".format(
                            i, 2**j, k, runtime))
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in comparisons: {}".format(
                            i, 2**j, k, merge_counter))
                    arr1 = list(original_arr1)
                    arr2 = list(original_arr2)
                    arr3 = list(original_arr3)
                    merge_counter = 0
                else:
                    start = time.time()
                    sorted_arr = merge_sort(arr)
                    end = time.time()
                    runtime = round(end - start, 6)
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in time: {}".format(
                            i, 2**j, k, runtime))
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in comparisons: {}".format(
                            i, 2**j, k, merge_counter))
                    arr = list(original_arr)
                    merge_counter = 0
            if k == "shell":
                if i == 4:
                    start1 = time.time()
                    sorted_arr, comparisons1 = shell.shell_sort(arr1)
                    end1 = time.time()
                    start2 = time.time()
                    sorted_arr, comparisons2 = shell.shell_sort(arr1)
                    end2 = time.time()
                    start3 = time.time()
                    sorted_arr, comparisons3 = shell.shell_sort(arr1)
                    end3 = time.time()
                    runtime = round((end1 - start1 + end2 - start2 + end3 - start3)/3, 6)
                    comparisons = (comparisons1 + comparisons2 + comparisons3)/3
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in time: {}".format(
                            i, 2**j, k, runtime))
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in comparisons: {}".format(
                            i, 2**j, k, comparisons))
                    arr1 = list(original_arr1)
                    arr2 = list(original_arr2)
                    arr3 = list(original_arr3)
                else:
                    start = time.time()
                    sorted_arr, comparisons = shell.shell_sort(arr)
                    end = time.time()
                    runtime = round(end - start, 6)
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in time: {}".format(
                            i, 2**j, k, runtime))
                    print(
                        "Result of experiment #{} in size {} using {} algorythm in comparisons: {}".format(
                            i, 2**j, k, comparisons))
                    arr = list(original_arr)
