# n = int(input('Enter a number: '))
# val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 5, 4, 1]
# sym = ['M','CM','D','CD','C','XC','L','XL','X','V','IV','I']
# res = ''
# for i in range(len(val)):
#     c = n // val[i]
#     res += sym[i] * c
#     n -= c*val[i]
#     if n <= 0:
#         break
# print(res)

mat = [[1,1,1],[1,0,0],[1,1,1]]
cnt = 0
r = []
c = []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 0:
            r.append(i)
            c.append(j)
for i in r:
    for j in range(len(mat[0])):
        mat[i][j] = 0
for i in range(len(mat)):
    for j in c:
        mat[i][j] = 0
print(mat)