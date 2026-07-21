def sum3(nums):
    nums.sort()
    result = []

    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate fixed elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate right values
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif s < 0:
                left += 1
            else:
                right -= 1

    return result


# Test Cases
print(sum3([-1, 0, 1, 2, -1, -4]))   # [[-1, -1, 2], [-1, 0, 1]]
print(sum3([0, 0, 0, 0]))            # [[0, 0, 0]]
print(sum3([-2, 0, 0, 2, 2]))        # [[-2, 0, 2]]
print(sum3([-3, -2, -2, -1, 3]))     # []
