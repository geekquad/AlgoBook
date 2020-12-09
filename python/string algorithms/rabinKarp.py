string = input("Original string : ")
pattern = input("String to be searched : ")

n = len(string)
m = len(pattern)


# constants
d = 256
p = 31
patternHash = 0
stringHash = 0
h = 1

for i in range(m - 1):
    h = (h * d) % p
 

# find hash function of the first substring of length m in string , and of the pattern  
for i in range(m):
    patternHash = (d * patternHash + ord(pattern[i])) % p 
    stringHash = (d * stringHash + ord(string[i])) % p 

for i in range(n - m + 1):
    if patternHash == stringHash :
        found = True

        # if the hash function matches, then check if string[i..i + m - 1] == patterm
        for j in range(m):
            if pattern[j] != string[i + j] :
                found = False
                break

        if found == True:
            print(f"Pattern {pattern} is present at index : {i}")

    # update stringHash      
    if i < (n - m):
        stringHash = (d * (stringHash - ord(string[i]) * h) + ord(string[i + m])) % p
        if stringHash < 0 :
            stringHash = stringHash + p


 

