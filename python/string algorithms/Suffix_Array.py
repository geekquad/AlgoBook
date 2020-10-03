   
class SuffixArray(object):
    def __init__(self,array,n):
        self.array = self.array #initial array
        self.n = n #size of array
        
    #dividing a word into its suffixes   
    def divideWordToSuffixes(self,word):
        suffixes = []
        n = len(word)
        suffixes.append("$") #end terminal, starting symbol
        for i in range(n):
            suffixes.append(word[i::] + "$")
        return suffixes
    
    #sorting suffixes
    def sortSuffixes(self,suffixes):
        return sorted(suffixes)
    
    def createSuffixArray(self):
        suffix_array = []
        for i in range(self.n):
            suffix_array.append(self.divideWordsToSuffixes(self.array[i]))
        return self.sortSuffixes(suffix_array)
    
    #searching element in O(logn) for pattern matching purposes
    def binarySearch(self,data,lo,hi,target):
        if(lo < hi):
            return False
        mid = (lo + hi)//2
        if(data[mid] == target):
            return mid
        elif(data[mid] < target):
            self.binarySearch(data,mid+1,hi,target)
        else:
            self.binarySearch(data,lo,mid-1,target)
    #finding out whether some pattern P matches our word
    def is_P_Matches(self,P,suffix_array):
        m = len(P)
        lo = 0
        hi = m-1
        found = self.binarySearch(suffix_array,lo,hi,P)
        if(!found):
            return False
        else:
            return found
    
    #finding all branching words
    def collectBrachingWords(self,suffix_array):
        n = len(suffix_array)
        braching_words = []
        for i in range(n):
            j = i+1
            branching_word = ""
            while(j < n):
                k = 0
                while(k < len(suffix_array[i])):
                    if(suffix_array[i][k] == suffix_array[j][k]):
                        braching_word += suffix_array[i][k]
                    else:
                        break
                    k += 1
                branching_words.append(braching_word)
                j += 1
        return braching_words

    #finding longest common prefix
    def LCP(self,suffix_array):
        pass
    
    def longestSubstring(self,suffix_array):
        return self.LCP(suffix_array)
    
def main():
    array = ["SDU","is","located","in","Kaskelen"]
    SuffixArray = SuffixArray(array,len(array))