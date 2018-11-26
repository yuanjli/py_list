# Sentence Reversal
# Problem: Given a string of words, reverse all the words.

# 'This is the best'
# Return: 'best the is This'

# '   Space here' and 'space here   '
# both become 'here space'

def rev_word1(s):
    return " ".join(reversed(s.split()))

def rev_word2(s):
    return " ".join(s.split()[::-1])

print(rev_word1(' Hello, How are you?'))
print(rev_word2(' Hello, How are you?'))