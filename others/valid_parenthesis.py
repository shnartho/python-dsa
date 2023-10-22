def is_valid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else None
            if top_element != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

s = ")({[[(()]]})))"
print(is_valid(s))