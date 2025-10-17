# Illustration of Bitwise Operators in Python
a = 29  # In binary: 11101
b = 15  # In binary: 01111
print("a =", a, "b =", b)
print("a & b =", a & b)   # Bitwise AND
print("a | b =", a | b)   # Bitwise OR
print("a ^ b =", a ^ b)   # Bitwise XOR
print("~a =", ~a)         # Bitwise NOT
print("a << 2 =", a << 2) # Left Shift
print("b >> 2 =", b >> 2) # Right Shift
print('Left shift multiplication by 2 and right shift division by 2')
num = 5
print(num, '<< 1 =', num << 1)  # Equivalent to num * 2
print(num, '>> 1 =', num >> 1)  # Equivalent to num // 2
print('a << b means a * (2 ** b) and a >> b means a // (2 ** b)')
print(a << 1)