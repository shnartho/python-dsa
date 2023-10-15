def compute_lps_array(pattern, len_pat, lps):
    i = 0 
    j = 1
    lps[0] = 0
    while j < len_pat:
        if pattern[i] == pattern[j]:
            lps[j] = i + 1
            i += 1
            j += 1
        else:
            if i != 0:
                i = lps[i-1]
            else:
                lps[j] = 0
                j += 1


def kmp_search(text, pattern):
    len_txt = len(text)
    len_pat = len(pattern)
    lps = [0] * len_pat
    compute_lps_array(pattern, len_pat, lps)
    i = 0
    j = 0 
    while i < len_txt:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:    
                j = lps[j-1]
            else: 
                i += 1
        if j == len_pat:
            return (i - j)
            # to keep continuing seaching more matches
            #j= lps[j-1]
    return -1


text = "ABABDABACDABABCABAB"
pattern = "ABCABAB"
result = kmp_search(text, pattern)

if result != -1:
    print(f"Pattern found at index {result}.")
else:
    print("Pattern not found in the text.")