# https://www.algoexpert.io/questions/Two%20Number%20Sum

# O(n^2) time and O(1) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)-1):
        first_num = array[i]
        for j in range(i+1, len(array)):
            second_num = array[j]
            if first_num + second_num == targetSum:
                return [first_num, second_num]
    return list()

if __name__ == '__main__':
    print( twoNumberSum( [3, 5, -4, 8, 11, 1, -1, 6], 10) )