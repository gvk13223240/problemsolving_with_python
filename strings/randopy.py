# for printing each with freq in sorted order
s = input().strip()
final = {}
for ch in s:
    final[ch] = final.get(ch, 0) + 1
for key, value in sorted(final.items()):
    print(key, ":", value)

cnt = [0] * 256
res = ''
for ch in s:
    cnt[ord(ch)] += 1
for i in range(256):
    if cnt[i] > 0:
        res += chr(i) * cnt[i]
print(res)