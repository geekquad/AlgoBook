# PROBLEM STATEMENT:
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# Example [ 1 ,5 , 11, 5] Answer True Explanation : [1,5,5] and [11] are two patitioned with equal sum that's why its said true
# we are simply using dynamic programming and check if include that element and if not include then what happend.

def subset_sum(arr , sum):
    dp = [[False for x in range(sum+1)] for x in range(len(arr) + 1)]

    for i in range(len(arr)+1):
        for j in range(sum+1):

            # sum has value and array contains zero values
            if i == 0:
                dp[i][j] = False

            # sum zero and array contains values ans is empty set so its True.
            elif j == 0:
                dp[i][j] = True

            # array value less then sum then check for include or not include value of array.
            elif j >= arr[i-1]:
                dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
                            #include            # not include

            # otherwise not include the values.
            else:
                dp[i][j] = dp[i-1][j]

    print(dp)
    return dp[len(arr)][sum]


print('enter array and sum deatils:')
arr = list(map(int, input().split(" ")))
sum = int(input())
print(subset_sum(arr,sum))
