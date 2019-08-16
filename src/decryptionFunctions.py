# This file uses the pycipher module to create decryption functions


################################## ROT 13 Decrtpy ######################################


def dec_rot13(string):

    upper_num = [ord(c) for c in string.upper()]

    lenght = len(upper_num)

    for i in range(lenght):
        upper_num[i] = upper_num[i] - 52

    for i in range(lenght):
        upper_num[i] = upper_num[i] % 26

    for i in range(lenght):
        upper_num[i] = upper_num[i] + 65

    final_string = [chr(c) for c in upper_num]

    seb = [str(i) for i in final_string]

    res = "".join(seb)

    return res


def dec_ceaser(string):

    upper_num = [ord(c) for c in string.upper()]

    lenght = len(upper_num)

    for i in range(lenght):
        upper_num[i] = upper_num[i] - 65

    common = max(set(upper_num), key=upper_num.count)
    shift = (4 - common) % 26

    for i in range(lenght):
        upper_num[i] = ((upper_num[i] + shift) % 26) + 65

        final_string = [chr(c) for c in upper_num]

    seb = [str(i) for i in final_string]

    # Join list items using join()
    res = "".join(seb)

    return res


#####################################  END ROT 13 Decrypt ###########################

###################################### VIGNERE ######################################

from collections import Counter
from math import fabs
from string import ascii_lowercase
from scipy.stats import pearsonr
from numpy import matrix
from os import system

# Define some constants:
LETTER_CNT = 26
ENGLISH_IC = 1.73

# Cornell English letter frequecy
ENGLISH_LETTERS = "etaoinsrhdlucmfywgpbvkxqjz"
ENGLISH_FREQ = [
    0.1202,
    0.0910,
    0.0812,
    0.0768,
    0.0731,
    0.0695,
    0.0628,
    0.0602,
    0.0592,
    0.0432,
    0.0398,
    0.0288,
    0.0271,
    0.0261,
    0.0230,
    0.0211,
    0.0209,
    0.0203,
    0.0182,
    0.0149,
    0.0111,
    0.0069,
    0.0017,
    0.0011,
    0.0010,
    0.0007,
]
ENGLISH_DICT = dict(zip(list(ENGLISH_LETTERS), ENGLISH_FREQ))
MAX_LEN = 10  # Maximum keyword length


def scrub_string(str):
    """Remove non-alphabetic characters and convert string to lower case. """
    halfway = "".join(ch for ch in str if ch.isalpha())
    half = halfway.upper()
    return half


def string_to_numbers(str):
    """Convert str to a list of numbers giving the position of the letter
    in the alphabet (position of a = 0). str should contain only
    lowercase letters.
    """
    return [ord(ch) - ord("a") for ch in str]


def correct_keyword(string):
    kewowo = []
    for i in range(len(string)):
        kewowo.append(chr(((((ord(string[i]) - 97) + 1) % 26) + 97)))
    kewo2 = "".join(kewowo)
    return kewo2


def numbers_to_string(nums):
    """Convert a list of numbers to a string of letters
    (index of a = 0); the inverse function of string_to_numbers.
    """
    return "".join(chr(n + ord("a")) for n in nums)


def shift_string_by_number(str, shift):
    """Shift the letters in str by the amount shift (either positive
    or negative) modulo 26.
    """
    return numbers_to_string(
        (num + shift) % LETTER_CNT for num in string_to_numbers(str)
    )


def shift_string_by_letter(str, ch, direction):
    """Shift the letters in str by the value of ch, modulo 26.
    Right shift if direction = 1, left shift if direction = -1.
    """
    assert direction in {1, -1}
    return shift_string_by_number(str, (ord(ch) - ord("a") + 1) * direction)


def chunk_string(str):
    """Add a blank between each block of five characters in str."""
    return " ".join(str[i : i + 5] for i in range(0, len(str), 5))


def crypt(text, passphrase, which):
    """Encrypt or decrypt the text, depending on whether which = 1
    or which = -1.
    """
    text = scrub_string(text)
    passphrase = scrub_string(passphrase)
    letters = (
        shift_string_by_letter(ch, passphrase[i % len(passphrase)], which)
        for i, ch in enumerate(text)
    )
    return "".join(letters)


def IC(text, ncol):
    """Divide the text into ncol columns and return the average index
    of coincidence across the columns.
    """
    text = scrub_string(text)
    A = str_to_matrix(scrub_string(text), ncol)
    cum = 0
    for col in A:
        N = len(col)
        cum += sum(n * (n - 1) for n in Counter(col).values()) / (
            N * (N - 1) / LETTER_CNT
        )
    return cum / ncol


def keyword_length(text):
    """Determine keyword length by finding the length that makes
    IC closest to the English plaintext value of 1.73.
    """
    text = scrub_string(text)
    a = [fabs(IC(text, ncol) - ENGLISH_IC) for ncol in range(1, MAX_LEN)]
    return a.index(min(a)) + 1


def correlation(letter_list):
    """Return the correlation of the frequencies of the letters
    in the list with the English letter frequency.
    """
    counts = Counter(letter_list)
    text_freq = [counts[ch] / len(letter_list) for ch in ascii_lowercase]
    english_freq = [ENGLISH_DICT[ch] for ch in ascii_lowercase]
    return pearsonr(text_freq, english_freq)[0]


def find_keyword_letter(letter_list):
    """Return a letter of the keyword, given every nth character
    of the ciphertext, where n = keyword length.
    """
    str = "".join(letter_list)
    cors = [
        correlation(shift_string_by_number(str, -num))
        for num in range(1, LETTER_CNT + 1)
    ]
    return ascii_lowercase[cors.index(max(cors))]


def find_keyword(ciphertext, keyword_length):
    """Return the keyword, given its length and the ciphertext."""
    A = str_to_matrix(scrub_string(ciphertext), keyword_length)
    return "".join([find_keyword_letter(A[j]) for j in range(keyword_length)])


def str_to_matrix(str, ncol):
    """Divide str into ncol lists as in the example below:

    >>> str_to_matrix('abcdefghijk', 4)
    [['a', 'e', 'i'], ['b', 'f', 'j'], ['c', 'g', 'k'], ['d', 'h']]
    """
    A = [list(str[i : i + ncol]) for i in range(0, len(str), ncol)]
    stub = A.pop()
    B = matrix(A).T.tolist()
    for i, ch in enumerate(stub):
        B[i] += ch
    return B


def test_functions():
    """Unit tests for functions in this module."""
    assert shift_string_by_number("unladenswallow", 15) == "jcapstchlpaadl"
    assert shift_string_by_letter("unladenswallow", "M", -1) == "ngetwxglpteehp"
    assert chunk_string("terpsichorean") == "terps ichor ean"
    assert crypt("Hello world!", "mypassword", 1) == "udbmhplgdh"
    assert crypt("udbmhplgdh", "mypassword", -1) == "helloworld"
    assert round(correlation("ganzunglabulich"), 6) == 0.118034

    assert (
        scrub_string("I'm not Doctor bloody Bernofsky!!")
        == "imnotdoctorbloodybernofsky"
    )

    assert string_to_numbers("lemoncurry") == [11, 4, 12, 14, 13, 2, 20, 17, 17, 24]

    assert numbers_to_string([11, 4, 12, 14, 13, 2, 20, 17, 17, 24]) == "lemoncurry"

    assert (
        round(
            IC(
                """QPWKA LVRXC QZIKG RBPFA EOMFL JMSDZ VDHXC XJYEB IMTRQ
    WNMEA IZRVK CVKVL XNEIC FZPZC ZZHKM LVZVZ IZRRQ WDKEC
    HOSNY XXLSP MYKVQ XJTDC IOMEE XDQVS RXLRL KZHOV""",
                5,
            ),
            2,
        )
        == 1.82
    )

    assert (
        keyword_length(
            """QPWKA LVRXC QZIKG RBPFA EOMFL JMSDZ VDHXC XJYEB
    IMTRQ WNMEA IZRVK CVKVL XNEIC FZPZC ZZHKM LVZVZ IZRRQ WDKEC
    HOSNY XXLSP MYKVQ XJTDC IOMEE XDQVS RXLRL KZHOV"""
        )
        == 5
    )

    assert str_to_matrix("abcdefghijk", 4) == [
        ["a", "e", "i"],
        ["b", "f", "j"],
        ["c", "g", "k"],
        ["d", "h"],
    ]


#####################################   END VIGNERE ######################################

#####################################   Cryptanalysis  ###################################


def frequency_list_generate(string):
    new_string = scrub_string(string.lower())
    #
    freq = [0 for _ in range(26)]
    for c in new_string.lower():
        freq[ord(c) - ord("a")] += 1

    return freq


print("abcdefghijklmnop")


# IC(text, ncol) inside vignere

####################################  Cryptanalysis end ##################################
