def reverse_words(s):
    words = s.strip().split()
    return ' '.join(reversed(words))


s = "the sky is blue"
print(reverse_words(s))
