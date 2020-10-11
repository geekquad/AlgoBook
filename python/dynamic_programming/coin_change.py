"""
THE COIN CHANGE PROBLEM (SOLVED FROM HACKERRANK- PROBLEM SOLVING)
PROBLEM:
You are working at the cash counter at a fun-fair, and you have different types of coins available 
to you in infinite quantities. The value of each coin is already given.
 Can you determine the number of ways of making change for a particular number of units using the given types of coins?

For example, if you have 4 types of coins, and the value of each type is given as 8,3,1,2 respectively, 
you can make change for 3 units in three ways:{1,1,1} ,{1,2} and {3} .

Input Format

The first line contains two space-separated integers describing the respective values of n and m, where:
n is the number of units
m is the number of coin types
The second line contains m space-separated integers describing the respective values of each coin type :
c=c[0],c[1],c[2]...c[m-1]  (the list of distinct coins available in infinite amounts).

Output Format

Print a long integer denoting the number of ways we can get a sum of  n
from the given infinite supply of m types of coins

Sample Input 0
4 3
1 2 3
Sample Output 0
4
Explanation 0

There are four ways to make change for N=4 using coins with values given by C=[1,2,3] :
1. {1,1,1}
2. {1,1,2}
3. {2,2}
4. {1,3}

Thus, we print 4 as our answer.
"""

def getWays(n, c):
    n_perms = [1]+[0]*n
    for coin in c:
        for i in range(coin, n+1):
            n_perms[i] += n_perms[i-coin]
    return n_perms[n]
    
n, m = map(int, input().split())
c = list(map(int, input().split()))
print(getWays(n, c))