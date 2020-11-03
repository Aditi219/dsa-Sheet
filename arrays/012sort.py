def sort012(nums):
    if len(nums) == 0 or len(nums) == 1:
        return
    start = 0
    end = len(nums)-1
    index = 0
    while index <= end and start < end:
        if nums[index] == 0:
            nums[index] = nums[start]
            nums[start] = 0
            start += 1
            index += 1
        elif nums[index] == 2:
            nums[index] = nums[end]
            nums[end] = 2
            end -= 1
        elif nums[index] == 1:
            index += 1
    print(nums)


a = list(map(int, input().split()))
sort012(a)
