def reverse_string(name):
    rn = ""
    for c in name:
        rn = c + rn
    return rn

name = "nayem"
reversed_name = reverse_string(name)
print(reversed_name)