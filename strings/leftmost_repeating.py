# Naive Approach -> O(n^2)
def leftmost_repeating_character(s):

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return i
    return -1
print('Testing Naive Approach')
print(leftmost_repeating_character(input('Enter a string: ').strip()))

# Optimized Approach -> O(n)
def leftmost_repeating_character_optimized(s):
    cnt = [0] * 256
    for i in range(len(s)):
        cnt[ord(s[i])] += 1
    for i in range(len(s)):
        if cnt[ord(s[i])] > 1:
            return i
    return -1

print('Now Testing Optimized Approach')
print(leftmost_repeating_character_optimized(input('Enter a string: ').strip()))

# More Optimized Approach 
import sys
CHAR = 256
def leftmost_repeating_character_more_optimized(s):
    fIndex = [-1] * CHAR
    res = sys.maxsize
    for i in range(len(s)):
        if fIndex[ord(s[i])] == -1:
            fIndex[ord(s[i])] = i
        else:
            res = min(res, fIndex[ord(s[i])])
    return res if res != sys.maxsize else -1
print('Now Testing More Optimized Approach')
print(leftmost_repeating_character_more_optimized(input('Enter a string: ').strip()))

# the more optimized approach
# Leftmost Repeating Character
# Efficient 2

CHAR = 256
def leftmost(st) :
    vis = [False] * CHAR
    res = -1
    for i in range(len(st)-1,-1,-1) :
        if (vis[ord(st[i])]==True) :
            res = i
        else :
            vis[ord(st[i])] = True
    
    return res
        
st = "abccbd"
print(leftmost(st))