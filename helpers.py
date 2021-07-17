
vowels = 'aeiou'

def adjacent_pairs(it):
    it = iter(it)
    try:
        a, b = next(it), next(it)
    except StopIteration:
        return
    while True:
        yield a, b
        try:
            a, b = b, next(it)
        except StopIteration:
            return

def count_vowels(s):
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    
    return count

def get_unique_vowels(s):
    contained_vowels = set()
    for char in s:
        if char in vowels:
            contained_vowels.add(char)
    return contained_vowels