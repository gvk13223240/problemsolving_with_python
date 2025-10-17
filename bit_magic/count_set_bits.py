# Count set bits
# Naive Approach
n = int(input('Enter a decimal number: '))
count = 0
while n > 0:
    if n & 1:  # Check if the least significant bit is set
        count += 1
    n = n >> 1  # Right shift n to check the next bit
print(f'The number of set bits is: {count} and {bin(n)}')  # Display binary representation
# Brian Kernighan’s Algorithm
print('Using Brian Kernighan’s Algorithm')
n = int(input('Enter a decimal number: '))
res = 0
while n:
    n = n & ( n - 1)
    res += 1
print(f'The number of set bits is: {res} and {bin(n)}')
# explaination: Each time we do n = n & (n - 1), the rightmost set bit of n is cleared. This continues until n becomes 0. The number of times this operation is performed gives the count of set bits.
# Step by Step Example:
# Let's take n = 13 (binary 1101)
# 1st Iteration: n = 13 (1101) -> n - 1 = 12 (1100) -> n & (n - 1) = 12 (1100) -> count = 1
# 2nd Iteration: n = 12 (1100) -> n - 1 = 11 (1011) -> n & (n - 1) = 8 (1000) -> count = 2
# 3rd Iteration: n = 8 (1000)  -> n - 1 = 7 (0111)  -> n & (n - 1) = 0 (0000) -> count = 3
print('Using inbuilt function')
n = int(input('Enter a decimal number: '))
print(f'The number of set bits is: {bin(n).count("1")} and {bin(n)}')
# explaination: The bin() function converts the number to its binary representation as a string. The count("1") method counts the number of '1's in that string, which corresponds to the number of set bits.