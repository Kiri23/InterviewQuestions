# Find the sum of two number exist in the array
# For example find the smallest number that sum up to 9
def twoSum(nums, target):
    map = {}
    for index, num in enumerate(nums):
        looking_for = target - num
        if looking_for in map:
            return [map[looking_for], index]
        else:
            map[num] = index
    return []


sum = [2, 7, 11, 15]
result = twoSum(sum, 9)
print(result)
