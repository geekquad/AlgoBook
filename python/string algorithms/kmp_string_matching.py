'''
For details on the working of the algorithm, refer this video by Abdul Bari:
https://www.youtube.com/watch?v=V5-7GzOfADQ
'''

'''
Defining the KMP Search function
'''
def KMPSearchfn(pattern, input_text): 
    len_pattern = len(pattern) 
    len_input = len(input_text) 
  
    pi = [0]*len_pattern #pi is the piArray that is used in KMP computation

    j = 0 #j is the iterator for pattern
  
    # computing the pi array of prefix-suffix values 
    piArray(pattern, len_pattern, pi) 
  
    i = 0 #iterator for input_text

    while i < len_input:
        #if the current letters match, we move both in text & pattern 
        if pattern[j] == input_text[i]: 
            i += 1
            j += 1
  
        #if we reach the end of the pattern, that means that the whole pattern
        #is matched. Hence, we can return the index
        if j == len_pattern: 
            print ("Found pattern at index " + str(i-j) + " of the string") 
            j = pi[j-1] 

        #if neither of the above case AND the chars don't match,
        #we move j backwards acc. to the pi array values
        elif i < len_input and pattern[j] != input_text[i]: 

            if j != 0: 
                j = pi[j-1]
            
            #in this subcase, j cannot be moves backwards, so we move i forwards      
            else: 
                i += 1

    #if we complete our search and final value of j<len_pattern, then we
    #can conclude that we didn't find the string
    if(j<len_pattern):
        print("The pattern is not present in the string")


'''
Defining the piArray auxillary function, which constructs the piArray
used during KMP searching 
'''


def piArray(pattern, len_pattern, pi): 
    l = 0 # length of the previous longest prefix suffix 
  
    pi[0] # pi[0] is 0, since it is the starting 
    i = 1
  
    # the loop calculates pi[i] for i = 1 to (len_pattern-1)
    while i < len_pattern: 
        if pattern[i]== pattern[l]: 
            l += 1
            pi[i] = l
            i += 1

        else:  
            if l != 0: 
                l = pi[l-1] 

            else: 
                pi[i] = 0
                i += 1


if __name__ == "__main__":
    
    print("_______This is the Knuth-Morris-Pratt pattern searching algo________\n\n")
    print("Enter the text body to be searched IN:")
    input_text = input()

    print("Enter the string to be searched")
    pattern = input()

    KMPSearchfn(pattern, input_text)