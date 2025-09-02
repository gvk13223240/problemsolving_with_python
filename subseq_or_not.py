# Iterative approach
def isSubseq(s, t):
    m, n = 0, 0
    while m < len(s) and n < len(t):
        if s[m] == t[n]:
            n += 1
        m += 1
    return n == len(t)

# Recursive approach
def isSubseqRec(s, t, m, n):
    if(n == 0):
        return True
    if m == 0:
        return False
    if s[m-1] == t[n-1]:
        return isSubseqRec(s, t, m-1, n-1)
    return isSubseqRec(s, t, m-1, n)

s, t = map(str, input('Enter two strings: ').strip().split())
print(isSubseq(s, t))
print(isSubseqRec(s, t, len(s), len(t)))
