n = int(input('Enter a decimal number: '))
k = int(input('Enter the value of k: '))
print(bin(n)[2:].zfill(32))
if (n & (1 << k)) != 0:  # 1 shifted left by k positions
    print(f'The {k}th bit is set.')
else:
    print(f'The {k}th bit is not set.')
# explaination: (1 << k) creates a number with only the kth bit set. The AND operation checks if that bit is also set in n.

# using right shift
if (n >> k) & 1 == 1: # Right shift n by k and check the least significant bit
    print(f'The {k}th bit is set.')
else:
    print(f'The {k}th bit is not set.')
# explaination: Right shifting n by k positions moves the kth bit to the least significant position. The AND operation with 1 checks if that bit is set.
