###Standard Merge Sort with branching factor 2 running in 6nlogn + 6n here###
def mergeSort(shuffled_list):
    print("Splitting in 2 branches: ", shuffled_list)
    if len(shuffled_list) > 1:
        mid = len(shuffled_list) // 2
        left_branch = shuffled_list[:mid]
        right_branch = shuffled_list[mid:]

        mergeSort(left_branch)
        mergeSort(right_branch)

        i = 0
        j = 0
        k = 0
        while i < len(left_branch) and j < len(right_branch):
            if left_branch[i] < right_branch[j]:
                shuffled_list[k] = left_branch[i]
                i = i + 1
            else:
                shuffled_list[k] = right_branch[j]
                j = j + 1
            k = k + 1

        while i < len(left_branch):
            shuffled_list[k] = left_branch[i]
            i = i + 1
            k = k + 1

        while j < len(right_branch):
            shuffled_list[k] = right_branch[j]
            j = j + 1
            k = k + 1
    print("Merging 2 branches: ", shuffled_list)

test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(test_list)
print(test_list)
