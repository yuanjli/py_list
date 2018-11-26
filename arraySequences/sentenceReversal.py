# Sentence Reversal
# Problem: Given a string of words, reverse all the words.

# 'This is the best'
# Return: 'best the is This'

# '   Space here' and 'space here   '
# both become 'here space'


### Using built in functions:
# def rev_word1(s):
#     return " ".join(reversed(s.split()))
#
# def rev_word2(s):
#     return " ".join(s.split()[::-1])
#
# print(rev_word1(' Hello, How are you?'))
# print(rev_word2(' Hello, How are you?'))


### write the basic solution:
def rev_word(s):

    words = []
    length = len(s)
    space = [' ']
    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i
            while i < length and s[i] not in space:
                i+=1
            words.append(s[word_start:i])
        i+=1
    return " ".join(reversed(words))

print(rev_word(' Hello, How are you?'))
