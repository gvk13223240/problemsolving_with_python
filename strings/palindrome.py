# Two pointer approach
def isPalin(s):
    l, r = 0, len(s)-1
    while l < r:
        if(s[l] != s[r]):
            return False
        l += 1
        r -= 1
    else:
        return True  
# Using slicing
def isPalinSlice(s):
    return s == s[::-1]
s = input('Enter a string: ').strip()
print(isPalin(s))
print(isPalinSlice(s))