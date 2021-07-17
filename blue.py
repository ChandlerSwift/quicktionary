import cmudict
from pysyllables import get_syllable_count
from helpers import *

vowels = 'aeiouAEIOU'

def b1(s):
    """Does not contain two vowels next to each other"""
    for a, b in adjacent_pairs(s):
        if a in vowels and b in vowels:
            return False
    
    return True

def b2(s):
    """Has exactly two syllables"""
    return get_syllable_count(s) == 2

def b3(s):
    """Has a double letter"""
    for a, b in adjacent_pairs(s):
        if a == b:
            return True
    
    return False

def b4(s):
    """Is not two syllables"""
    return not b2(s)

def b5(s):
    """Is exactly six letters long"""
    return len(s) == 6

def b6(s):
    """Is not exactly six letters long"""
    return not b5(s)

def b7(s):
    """Does not contain a double letter"""
    return not b3(s)

def b8(s):
    """Has exactly three vowels"""
    return count_vowels(s) == 3

def b9(s):
    """Has exactly three syllables"""
    return get_syllable_count(s) == 3

def b10(s):
    """Is at least ten letters long"""
    return len(s) >= 10

def b11(s):
    """Has an even number of letters"""
    return len(s) % 2 == 0

def b12(s):
    """Is at least seven letters long"""
    return len(s) >= 7

def b13(s):
    """Has at least two different vowels"""
    return len(get_unique_vowels(s)) >= 2

def b14(s):
    """Does not use any letter more than once"""
    return len(set(s)) == len(list(s))

def b15(s):
    """Is exactly nine letters long"""
    return len(s) == 9

def b16(s):
    """Is exactly five letters long"""
    return len(s) == 5

def b17(s):
    """Has an odd number of letters"""
    return not b11(s)

def b18(s):
    """Has at least three different vowels"""
    return len(get_unique_vowels(s)) >= 3

def b19(s):
    """Has a double consonant"""
    for a, b in adjacent_pairs(s):
        if a == b and a not in vowels:
            return True
    return False

def b20(s):
    """Is exactly eight letters long"""
    return len(s) == 8

def b21(s):
    """Has two vowels next to each other"""
    for a, b in adjacent_pairs(s):
        if a == b and a in vowels:
            return True
    return False

def b22(s):
    """Has exactly one syllable"""
    return get_syllable_count(s) == 1    

def b23(s):
    """Is not a plural word"""
    return False

def b24(s):
    """Has more consonants than vowels"""
    cons = 0
    vow = 0
    for char in s:
        if char in vowels:
            vow += 1
        else:
            cons += 1

    return cons > vow


def b25(s):
    """Is exactly seven letters long"""
    return len(s) == 7

def b26(s):
    """Is three or four letters long"""
    return len(s) == 3 or len(s) == 4

def b27(s):
    """Has exactly four syllables"""
    return get_syllable_count(s) == 4

def b28(s):
    """Uses the same vowel twice"""
    contained_vowels = []

    for char in s.lower():
        if char in vowels:
            contained_vowels.append(char)
    
    return len(contained_vowels) != len(set(contained_vowels))

def b29(s):
    """Does not have more than three different consonants"""
    consonants = set()
    for char in s.lower():
        if char not in vowels:
            consonants.add(char)
    
    return len(consonants) <= 3


def b30(s):
    """Does not contain more than one vowel"""
    return len([c for c in s if c in vowels]) <= 1

def b31(s):
    """Begins and ends with the same letter"""
    return s.lower()[0] == s.lower()[-1]

def b32(s):
    """Has an equal number of vowels and consonants"""
    cons = 0
    vow = 0
    for char in s:
        if char in vowels:
            vow += 1
        else:
            cons += 1

    return cons == vow

def b33(s):
    """Is a compound word"""
    return False

def b34(s):
    """Has a silent letter"""
    return False


def test():
    assert b1("Snowball") == True
    assert b1("Moo") == False
    assert b1("Cow") == True
    assert b1("Woah that's really cool") == False
    assert b1("Something") == True
    assert b1("aeiou") == False
    assert b1("") == True
    assert b1("Head") == False

    assert b2("Tomato") == False
    assert b2("Snowball") == True
    assert b2("Cow") == False
    assert b2("Computer") == False

    assert b3("Ball") == True
    assert b3("Quick") == False
    assert b3("Dog") == False
    assert b3("Moo") == True
    assert b3("Potato") == False
    assert b3("Town") == False

    assert b4("Tomato") == True
    assert b4("Snowball") == False
    assert b4("Cow") == True
    assert b4("Computer") == True

    assert b5("Tomato") == True
    assert b5("Snowball") == False
    assert b5("Cow") == False
    assert b5("Computer") == False
    assert b5("") == False
    assert b5("Breads") == True

    assert b6("Tomato") == False
    assert b6("Snowball") == True
    assert b6("Cow") == True
    assert b6("Computer") == True
    assert b6("") == True
    assert b6("Breads") == False

    assert b7("Ball") == False
    assert b7("Quick") == True
    assert b7("Dog") == True
    assert b7("Moo") == False
    assert b7("Potato") == True
    assert b7("Town") == True

    assert b8("Ball") == False
    assert b8("Quick") == False
    assert b8("Dog") == False
    assert b8("Contain") == True
    assert b8("Science") == True
    assert b8("jfkldsjfkdjkfdkkjaei") == True

    assert b9("Tomato") == True
    assert b9("Snowball") == False
    assert b9("Cow") == False
    assert b9("Computer") == True
    assert b9("") == False
    assert b9("Breads") == False

    assert b10("Tomato") == False
    assert b10("Snowball") == False
    assert b10("Cow") == False
    assert b10("Associated") == True
    assert b10("Quicktionary") == True
    assert b10("Tomatopotato") == True

    assert b11("Tomato") == True
    assert b11("Snowball") == True
    assert b11("Cow") == False
    assert b11("Associated") == True
    assert b11("Quicktionary") == True
    assert b11("Tomatopotatos") == False

    assert b12("Tomato") == False
    assert b12("Snowball") == True
    assert b12("Cow") == False
    assert b12("Associated") == True
    assert b12("Quicktionary") == True
    assert b12("Tomatopotato") == True

    assert b13("Tomato") == True
    assert b13("Snowball") == True
    assert b13("Cow") == False
    assert b13("Associated") == True
    assert b13("Quicktionary") == True
    assert b13("Tomatopotato") == True
    assert b13("Moo") == False

    assert b14("Tomato") == False
    assert b14("Snowball") == False
    assert b14("Cow") == True
    assert b14("Associated") == False
    assert b14("Quicktionary") == False
    assert b14("Tomatopotato") == False
    assert b14("Moo") == False
    assert b14("Cat") == True

    assert b15("Tomato") == False
    assert b15("Snowball") == False
    assert b15("Cow") == False
    assert b15("Associated") == False
    assert b15("Squizzing") == True
    assert b15("Jazziness") == True
    assert b15("Moo") == False

    assert b16("Tomato") == False
    assert b16("Heads") == True
    assert b16("Cow") == False
    assert b16("Associated") == False
    assert b16("Squizzing") == False
    assert b16("Jazziness") == False
    assert b16("Crate") == True

    assert b17("Tomato") == False
    assert b17("Snowball") == False
    assert b17("Cow") == True
    assert b17("Associated") == False
    assert b17("Quicktionary") == False
    assert b17("Tomatopotatos") == True

    assert b18("Tomato") == False
    assert b18("Heads") == False
    assert b18("Cow") == False
    assert b18("Associated") == True
    assert b18("Squizzing") == False
    assert b18("Jazziness") == True
    assert b18("Crate") == False

    assert b19("Tomato") == False
    assert b19("Snowball") == True
    assert b19("Cow") == False
    assert b19("Associated") == True
    assert b19("Quicktionary") == False
    assert b19("Tomatopotato") == False

    assert b20("Tomato") == False
    assert b20("Snowball") == True
    assert b20("Cow") == False
    assert b20("Associated") == False
    assert b20("Quicktionary") == False
    assert b20("Zyzzyvas") == True

    assert b21("Tomato") == False
    assert b21("Snowball") == False
    assert b21("Food") == True
    assert b21("Associated") == False
    assert b21("Moo") == True
    assert b21("Zyzzyvas") == False

    assert b22("Tomato") == False
    assert b22("Snowball") == False
    assert b22("Food") == True
    assert b22("Associated") == False
    assert b22("Moo") == True
    assert b22("Zyzzyvas") == False

    assert b24("Tomato") == False
    assert b24("Snowball") == True
    assert b24("Food") == False
    assert b24("Associated") == False
    assert b24("Moo") == False
    assert b24("Zyzzyvas") == True

    assert b25("Tomato") == False
    assert b25("Snowball") == False
    assert b25("Food") == False
    assert b25("Pizzazz") == True
    assert b25("Moo") == False
    assert b25("Zyzzyvas") == False

    assert b26("Tomato") == False
    assert b26("Snowball") == False
    assert b26("Food") == True
    assert b26("Pizzazz") == False
    assert b26("Moo") == True
    assert b26("Zyzzyvas") == False

    assert b27("Tomato") == False
    assert b27("Snowball") == False
    assert b27("Food") == False
    assert b27("Television") == True
    assert b27("Moo") == False
    assert b27("Dictionary") == True

    assert b28("Tomato") == True
    assert b28("Snowball") == False
    assert b28("Food") == True
    assert b28("Associated") == True
    assert b28("Moo") == True
    assert b28("Zyzzyvas") == False

    assert b29("Tomato") == True
    assert b29("Snowball") == False
    assert b29("Food") == True
    assert b29("Associated") == False
    assert b29("Moo") == True
    assert b29("Zyzzyvas") == False

    assert b30("Tomato") == False
    assert b30("Snowball") == False
    assert b30("Food") == False
    assert b30("Associated") == False
    assert b30("Mo") == True
    assert b30("Zyzzyvas") == True

    assert b31("Tomato") == False
    assert b31("Snowball") == False
    assert b31("Foof") == True
    assert b31("Associated") == False
    assert b31("Mom") == True
    assert b31("Zyzzyvas") == False


if __name__ == "__main__":
    test()