nums = [4,1,2,1,2]
unique = reduce(lambda x, y: x ^ y, nums)
print(unique)
