# You can use a stack approach
def reverse_words_in_line(s):
    stack = [] # this is a stack to hold words we implemented using a stack using list
    word = ''
    for char in s:
        if char == ' ':
            if word: # Why this -> ? To avoid appending empty strings
                stack.append(word)
                word = ''
        else:
            word += char
    if word: # why this out of loop -> ? To append the last word if it exists
        stack.append(word)
    reversed_line = ' '.join(reversed(stack))
    return reversed_line

print(reverse_words_in_line("Hello World"))

