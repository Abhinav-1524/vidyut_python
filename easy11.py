def count_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for word in sentence.split():
        for letter in word:
            if letter in vowels:
                count += 1
    return count

print(count_vowels("The quick brown fox jumps over the lazy dog"))
print(count_vowels("Hello, World!"))
print(count_vowels("Python is a high-level programming language."))

print(count) # NameError: name 'count' is not defined
