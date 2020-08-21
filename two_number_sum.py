# https://www.algoexpert.io/questions/Two%20Number%20Sum

# O(n) time and O(n) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = dict()
    for num in array:
        potential_match = targetSum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True
    return list()

if __name__ == '__main__':
    print( twoNumberSum( [3, 5, -4, 8, 11, 1, -1, 6], 10) )