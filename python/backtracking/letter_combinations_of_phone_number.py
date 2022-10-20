# Leetcode 17. Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

def letterCombinations(digits) :
  digit_letters = {
      "0":["0"],
      "1":["1"],
      "2":["a","b","c"],
      "3":["d","e","f"],
      "4":["g","h","i"],
      "5":["j","k","l"],
      "6":["m","n","o"],
      "7":["p","q","r","s"],
      "8":["t","u","v"],
      "9":["w","x","y","z"],
      }

  if len(digits) ==1:
      return digit_letters[digits]
  if len(digits)==0:
      return []
  res=[]
  for char in digit_letters[digits[0]]:
      for combination in letterCombinations(digits[1:]):
          res.append(char+combination)
  return res

letterCombinations("23")