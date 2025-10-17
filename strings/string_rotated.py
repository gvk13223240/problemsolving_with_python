def isRotated(s1,s2):
    if len(s1) != len(s2):
        return False
    temp = ''
    temp = s1 + s1
    return temp.find(s2) != -1
t1 = input().strip()
t2 = input().strip()

print(isRotated(t1, t2))