# Using Recursion
def subser(s, curr, ind):
    if ind == len(s):
        print(curr, end=' ')
        return
    subser(s, curr + s[ind], ind + 1)
    subser(s, curr, ind + 1)

print('All subsets of a string are:')
subser("abc", "", 0)