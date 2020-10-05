def editdistance(str1 , str2):
    m = len(str1)
    n = len(str2)

    # intialize with zeros

    dp = [[0 for x in range(n+1)] for x in range(m + 1)]

    for i in range(m + 1):

        for j in range(n+1):
        # if first string empty then add all character of second string

            if i==0:
                dp[i][j] = j

        # if second string is empty then we heva one option to remove all charcetrs from second string.
            elif j==0:
                dp[i][j] = i

        # if both string last character are same then ignore and skip it

            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

        # not if character does not match then we have to check for all possibilites insert, remove and replace

            else:
                dp[i][j] = 1 + min(dp[i][j-1],   # insert
                                   dp[i-1][j],  # remove
                                   dp[i-1][j-1])   # replace

    return dp[m][n]

str_1 = input()
str_2 = input()
print(editdistance(str_1 , str_2))