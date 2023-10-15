def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    d = 256 # base
    q = 13 # modules
    h = pow(d, m-1) % q
    pattern_hash = 0
    text_hash = 0

    #calculate hash value for pattern and first window of text
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    # slide the windoes over the text and compare hashes
    for i in range(n-m+1):
        if pattern_hash == text_hash:
            #hashes match check characters
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                return i 
        if i < n-m:
            text_hash = (d*(text_hash-ord(text[i])* h) + ord(text[i+m])) % q 
            if text_hash < 0 : 
                text_hash += q
    return -1 


text = "ABABDABACDABABCABAB"
pattern = "CABAB"
result = rabin_karp(text, pattern)

if result != -1:
    print(f"Pattern found at index {result}.")
else:
    print("Pattern not found in the text.")
