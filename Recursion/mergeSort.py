# merge sort recursive algorithm
def mergeSort (list):
    # list is already sorted
    if len(list) <= 1:
        return list
    # split the list in half
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    # sort each side of the list; recombine into two sorted lists
    leftSorted = mergeSort(leftList)
    rightSorted = mergeSort(rightList)
    sortedList = []
    i = 0
    j = 0
    while i < len(leftSorted) and j < len(rightSorted):
        if leftSorted [i] <= rightSorted[j]:
            sortedList += [leftSorted[i]]
            i += 1
        else:
            sortedList += [rightSorted[j]]
            j += 1
    if i == len(leftSorted):
        sortedList += rightSorted[j:]
    else:
        sortedList += leftSorted[i:]
    return sortedList

print(mergeSort([38, 27, 43, 3, 9, 82, 10]))




