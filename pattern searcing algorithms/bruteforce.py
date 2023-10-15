def brute_force(s, p):
    n, m = len(s), len(p)
    for i in range(n-m+1):
        if s[i:i+m] == p:
            print(f"Pattern found at index {i}")

my_string = "ABABDABACDABABCABAB"
pattern = "ABCABAB"
brute_force(my_string, pattern)
