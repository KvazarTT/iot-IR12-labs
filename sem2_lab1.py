def two_sum(nums, target):
    """
    Знаходить індекси двох елементів сума яких дорівнює target
    """
    seen = {}
    for i, num in enumerate(nums):
        c = target - num
        if c in seen:
            return [seen[c], i]
        seen[num] = i
    return -1

def is_monotonic(nums):
    """
    Перевіряє чи є масив монотонним
    """
    if len(nums) < 2:
        return True

    is_increasing = True
    is_decreasing = True

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            is_increasing = False
        if nums[i] < nums[i + 1]:
            is_decreasing = False
    return is_increasing or is_decreasing

def find_unsorted_subarray(nums):
    """
    Знаходить межі найменшого підмасиву який потрібно відсортувати
    """
    n = len(nums)
    if n < 2:
        return (-1, -1)

    max_val = nums[0]
    end = -1
    for i in range(n):
        if nums[i] < max_val:
            end = i
        else:
            max_val = nums[i]
    if end == -1:
        return (-1, -1)

    min_val = nums[n - 1]
    start = -1
    for i in range(n - 1, -1, -1):
        if nums[i] > min_val:
            start = i
        else:
            min_val = nums[i]

    return (start, end)
