p = 31 # change to 53 if string may contain both uppercase and lowercase
m = int(1e9 + 9)
def compute_power(p_pow, p):
    p_pow = p_pow % m
    res = 1
    while p > 0:
        if p % 2 == 1 :
            res = res * p_pow % m 
        p_pow = p_pow * p_pow % m
        p = p // 2 
    return res

# compute_hash(s) = s[0] + s[1]*p + s[2]*p^2 + ... + s[n-1]*p^(n-1) mod m 
def compute_hash(s): # function to calculate hash of each word in string
    hash_value = 0
    p_pow = 1
    for c in s :
        hash_value = (hash_value + ord(c) * p_pow) % m 
        p_pow = compute_power(p_pow,p) % m 
    return hash_value

def get_hashes(st): # function which calculates hash of the input string
    words = st.split(' ')
    hashes = []
    for i in range(len(words)): 
        hashes.append((compute_hash(words[i]), i))
    return hashes

if __name__ == '__main__' :
	st = input("Enter the String: ")
	words = st.split(' ')
	hashes = get_hashes(st)
	for i in range(len(hashes)) :
		print("Hash Value of",words[hashes[i][1]],":",hashes[i][0])
    