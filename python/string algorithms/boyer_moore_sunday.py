#import pdb;pdb.set_trace()

def search_letter_in_pattern(pattern,letter):
    """
    Search the letter inside in pattern if no converge return -1
    """
    m = len(pattern)
    count = 1

    for i in range(m-1,-1,-1):
        if letter==pattern[i]:
            return count
        
        count = count+1
    
    return -1


def boyern_sunday(text,pattern):
    """
    text:str
    pattern:str


    """
    coincidence = 0
    n = len(text)
    m = len(pattern)
    j = m-1
    i = m-1
    iterations = 0

    while(i<=n-1):
        if j==m-1:
            h = i  #the rightmost value
        
        
        if text[i]==pattern[j]:
            
            if j==0:
                
                coincidence = coincidence+1
                
                
                j = m-1
                i = (i+m-1)+j
                iterations = iterations+1
                
            else:
                i = i-1
                j = j-1
        else:

            #If it enters here it is because the last one no longer converges and there is no need to compare more
            if h==n-1:
                return coincidence


            j = m-1
            
            l  = search_letter_in_pattern(pattern,text[h+1])
            
           

            if l<0:
                #the next move is the pattern quantity +1
                i = h+m+1
                iterations = iterations+1
                
            else:
              
                i = h+l
                iterations = iterations+1
    
  
   
    return coincidence
        



print(boyern_sunday("jairo jandresja","ja"))





