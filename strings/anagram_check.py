def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count1 = [0] * 256
    for i in range(len(s)):
        count1[ord(s[i])] += 1
        count1[ord(t[i])] -= 1
    for x in count1:
        if x != 0:
            return False
    return True

if __name__ == "__main__":
    s, t = map(str, input('Enter two strings: ').strip().split())
    print(isAnagram(s.lower(), t.lower()))
