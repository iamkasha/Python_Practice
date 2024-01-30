def selection_sort(nums):
    x = len(nums)
    for i in range(0, x):
        minpos = i
        for j in range(i, x):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [5, 3, 8, 6, 7, 2]
selection_sort(nums)

print(nums)
