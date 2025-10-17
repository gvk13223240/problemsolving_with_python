# Check is Power of 2 or not
n = int(input('Enter a decimal number: '))
if n & (n - 1) == 0 and n != 0:
    print(f'{n} is a power of 2')
else:  
    print(f'{n} is not a power of 2')

# navie approach
count = 0   
temp = n
while temp > 1:
    temp = temp // 2
    count += 1
if 2 ** count == n:
    print(f'{n} is a power of 2')

else:  
    print(f'{n} is not a power of 2')

# explaination: A number n is a power of 2 if it has exactly one set bit in its binary representation. The expression n & (n - 1) clears the least significant set bit of n. If n is a power of 2, this operation will result in 0.


# Odd one out
n = int(input('Enter the number of elements: '))
result = 0 
print('Enter the elements:')
for _ in range(n):
    num = int(input())
    result ^= num  # XOR operation to find the odd one out
print(f'The odd one out is: {result}')

# naive approach
n = int(input('Enter the number of elements: '))   
elements = []
print('Enter the elements:')
for _ in range(n):
    num = int(input())
    elements.append(num)
frequencies = {}
for num in elements:
    if num in frequencies:
        frequencies[num] += 1
    else:
        frequencies[num] = 1
for num, freq in frequencies.items():
    if freq % 2 != 0:
        print(f'The odd one out is: {num}')
        break