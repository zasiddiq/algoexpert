 # https://www.algoexpert.io/questions/Validate%20Subsequence

def isValidSubsequence(array, sequence):
    # Write your code here.
    seq_index = 0
    for i in array:
        if seq_index == len(sequence):
            break
        if sequence[seq_index] == i:
            seq_index += 1
    return seq_index == len(sequence)



if __name__ == '__main__':
    print( isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10] ) )
    print( isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 10]))
    print(isValidSubsequence([1,1,6,1], [1,1,1,6] ) )