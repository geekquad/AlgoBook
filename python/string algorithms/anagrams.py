from typing import *
"""
contributor github handle(s):
@krissteea

file: valid_anagrams.py

The following contains solutions to checking if two strings are anagrams
"""

class AnagramSolutions:
    def anagrams_with_sort(self, string1: str, string2: str) -> bool:
        """
        This function will determine if two strings are anagrams of one another
        by sorting them and seeing if they form the same string

        Args:
            string1 (str)
            string2 (str)
            
        Returns:
            valid (bool): Will return True if the strings are anagram, False
            otherwise
        """
        if(len(string1) == len(string2)):    
            # Sort both words
            string1 = sorted(string1)
            string2 = sorted(string2)
        
            return(string1 == string2)
        else:
            return(False)
            
    def valid_anagrams(self, string1: str, string2: str) -> bool:
        """
        This function will determine if two strings are anagrams of one another
        utilizing a dictionary

        Args:
            string1 (str)
            string2 (str)
            
        Returns:
            valid (bool): Will return True if the strings are anagram, False
            otherwise
        """
        string1 = string1.replace(' ', '')
        string2 = string2.replace(' ', '')
        # if the lengths of s and t differ, they are not anagrams
        if(len(string1) != len(string2)):
            return(False)
        else:
            lettersDict: Dict[str, str] = {}

            # count how many times a letter occurs in s
            for letter in string1:
                if(letter in lettersDict):
                    lettersDict[letter] += 1
                else:
                    lettersDict[letter] = 1

            # see if all the letters in t match in s
            for t_letter in string2:
                if(t_letter in lettersDict):
                    lettersDict[t_letter] -= 1
                    if(lettersDict[t_letter] == 0):
                        popped = lettersDict.pop(t_letter)
                else:
                    lettersDict[t_letter] = 1

            return(lettersDict == {})
            
if __name__ == "__main__":
    test = AnagramSolutions()
    s = input("Please provide the first string: ")
    t = input("Please provide the second string: ")
    
    print("Calling method using sorted()")
    result1 = test.anagrams_with_sort(s, t)
    print("Result: %s" % result1)
    
    print("\nCalling method utilizing dictionary")
    result2 = test.valid_anagrams(s, t)
    print("Result: %s" % result2)
