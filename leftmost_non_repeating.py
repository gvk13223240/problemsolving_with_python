def leftmost_non_repeating_character_optimized(s):
    cnt = [0] * 256
    for i in range(len(s)):
        cnt[ord(s[i])] += 1
    for i in range(len(s)):
        if cnt[ord(s[i])] == 1:
            return i
    return -1
print('Testing Optimized Approach for Leftmost Non-Repeating Character')
print(leftmost_non_repeating_character_optimized(input('Enter a string: ').strip()))