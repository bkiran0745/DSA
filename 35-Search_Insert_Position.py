def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i
    return len(nums)
        
n = [1,3,5,6] 
t = 2
print(searchInsert(n,t))
        
