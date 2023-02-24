

def reverse(word):
  size = len(word)
  if size == 0 :
    return 
  last_char = word[size-1]
 
  return reverse(word[0:size-1])
  

