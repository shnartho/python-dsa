def min_window_substring(s:str, t:str) -> str:
    if t == "": return ""

    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, res_len = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            #update our result
            if (r-l+1) < res_len:
                res = [l, r]
                res_len = (r -1 + 1)
            # lets pop from the left from the window
            window[s[l]] -= 1 
            if s[l] in  countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r+1] if res_len != float("infinity") else ""  


s = "ADOBECODEBANC"
t = "BED"
result = min_window_substring(s, t)
print("Minimum window substring:", result)