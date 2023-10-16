from collections import defaultdict

def longest_sub(s, k):
    if k <= 0:
        return ""
    
    char_count = {}
    start = 0
    max_length = 0
    max_substring = ""

    for end in range(len(s)):
        c = s[end]
        char_count[c] = char_count.get(c, 0) + 1

        while len(char_count) > k:
            left_char = s[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            start += 1
        
        if end-start+1 > max_length:
            max_length = end - start + 1
            max_substring = s[start:end+1]

    return max_substring

# Example usage:
s = "abbcddlpppp"
k = 2
result = longest_sub(s, k)
print("string: " + str(result) + " | "+ "len: "+ str(len(result))) 