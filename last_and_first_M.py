
def search(nums, target):
    if len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        else:
            return [-1, -1]
    high = len(nums)
    low = 0
    start = -1
    last = -1
    while(low < high):
        mid = (low+high)//2
        if target > nums[mid]:
            low = mid+1
        elif target < nums[mid]:
            high = mid
        elif target == nums[mid]:
            i = mid
            start = mid
            while nums[i] == target and i >= 0:
                start = i
                i -= 1
            i = mid
            last = mid
            while i < len(nums) and nums[i] == target:
                last = i
                i += 1
            break

    res = [start, last]
    print(res)


search([5, 7, 7, 8, 8, 10], 8)
