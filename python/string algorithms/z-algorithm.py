'''
For details on the working of the algorithm, refer this video by Tushar Roy:
https://www.youtube.com/watch?v=CpZh4eF8QBw
'''


def Z_algo_search(input_text, pattern): 

    # First we concat the pattern, text and a unique character (i am using @) 
    concat_string = pattern + "@" + input_text 
    l = len(concat_string) 

    # calling the function to build the Z array 
    z = [0] * l 
    getZarr(concat_string, z) 

    # now looping through Z array for matching condition 
    for i in range(l): 

        # z[i] is the length of the matched region.
        # if it equals the length of the pattern, we've found the pattern
        if z[i] == len(pattern): 
            print("Pattern found at index",  str(i - len(pattern) - 1) + " of the text")
            return
    
    print("Pattern not found in the input text")



'''
HIGHLY recommended to watch the video to understand how to build the Z array
'''
def getZarr(string, z): 
    n = len(string) 

    left, right, k = 0, 0, 0
    for i in range(1, n): 

        if i > right: 
            left, right = i, i 

            while right < n and string[right - left] == string[right]: 
                right += 1
            z[i] = right - left 
            right -= 1

        else: 

            if z[k] < right - i + 1: 
                z[i] = z[k] 

            else: 
                left = i 
                while right < n and string[right - left] == string[right]: 
                    right += 1
                z[i] = right - left 
                right -= 1


if __name__ == "__main__":

    print("_______This is the Knuth-Morris-Pratt pattern searching algo________\n\n")
    print("Enter the text body to be searched IN:") 
    input_text = input()

    print("Enter the string to be searched")
    pattern = input()
    Z_algo_search(input_text, pattern) 