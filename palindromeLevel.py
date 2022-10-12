
from math import ceil


def palindrome_level(words, level=0):
    """
    [Palindrom level]
    Return the palindrome level of a given string
    PARAMETER
    words: str
    """
    no_space_words = words.replace(" ", "").upper(
    )  # remove whitespace and convert string to uppercase
    # count number of letters of a half string
    half_len = ceil(len(no_space_words)/2)

    # slice half string forward and backward
    fwdsubstring = no_space_words[:half_len]
    bwdsubstring = no_space_words[-1:-(half_len+1):-1]

    # base mode
    if fwdsubstring != bwdsubstring:
        return f"that was a palindrome level {level}"
    # recursive mode
    else:
        level += 1
        return palindrome_level(fwdsubstring, level)


print(palindrom_level("abbaabba"))
