# This file creates functions for keyless decryption algoritms

from decryptionFunctions import frequency_list_generate
import itertools
from collections import OrderedDict
import operator

from collections import Counter
from math import fabs
from string import ascii_lowercase
from scipy.stats import pearsonr
from numpy import matrix
from os import system

from cryptanalysis import *

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

############################################  Tools for Keyless decryption  ###################################
def scrub_string(str):
    """Remove non-alphabetic characters and convert string to lower case. """
    return "".join(ch for ch in str if ch.isalpha() or ch.isdigit()).lower()


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


def format_freq_order(string):
    frequency_list = frequency_list_generate(string.lower())
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    final = dict(zip(alphabet, frequency_list))
    result = sorted(final.items(), key=operator.itemgetter(1))
    rev_result = result[len(result) : 0 : -1]
    return rev_result


def most_common_letters_sorted(diction):
    most_probable_keys = []
    for c in range(len(diction)):
        most_probable_keys.append(diction[c][0])
    return most_probable_keys


############################################  End of Keyless decryption tools###################################
def key_ceaser(string):
    frequency_list = format_freq_order(string)
    ordered_key_list = most_common_letters_sorted(frequency_list)
    most_common_numbers = string_to_numbers(ordered_key_list)
    for i in range(len(most_common_numbers)):
        most_common_numbers[i] = (most_common_numbers[i] - 4) % 26
    return most_common_numbers


# example returns most common strings
# print(key_ceaser('aaaaaaaaaaaaaaaqwqwedrstdftzxcgfzcxbnvnmnmkjjgkfdhllpooiiuyu'))


########################################### Keyless vignere string  ############################################
# try to split input to every nth letter
string = "OVPJTNVEIHMERQYIDZRRVTQOGPYITBKDTUITMZJNTIZMRNTRUUZHMUASYCDKOEBOVUWRNVIPSNAALRMOQEFQTUCNTFXKKWZSVVYWAZUFIMMGOHRLKNWIIGQUVCAAGZKMAVYOMTIFMOJMXQBXLHLOVUJNYGCWCYYCTGVHNWVBNASXOALGZMBRBEZPDGAABYBVVTNZKCGVBYMGAZPMOMXWFKLNVZAOWOIMGADZCVNOMRCEVONBWIWVLKZRZFVVOBWJNFBNMHVLYMXXOGMFBXMSAEEVYJOIAAIYIBYBNUHWCNAEMGTGJTEMKAHMERAGZSIOGIZILJNBUOKUMOHXHCHDNPTALSVVNZOMHTOSXRIBOSCMIQSNTUIZPOQEVVJMDZNQMTBZTEIWRDSYAGZAVYVNQJXIBXHRAGAORALBUBCREEIHWJZOGPKZDGAABYBCXOZXKBSAOEAAVZDGUBZZSZSGMTLHJBRTUVUGIIMJACHEEMGKVDNTAKDSMAYBNWINAALEMOMSBTJBFZEFPGDSWERVOVSSIFBKVQZFBZSQZGIBVEMOMSVBOASNTVUGBSYTUIZBVZRRIXMXPSGWBMFORVTRQCIMNBAZSORRMYQBOHREUZZY"
print(string[0 : len(string) : 2])
# find bhattaryya of every nth letter


def probable_key_length(string):
    nth_strings = []
    for i in range(14):
        nth_strings.append(string[0 : len(string) : i + 1])
    nth_strings_bhat = []
    for i in nth_strings:
        nth_strings_bhat.append(IC(i, 1))
    create_list = []
    for i in range(len(nth_strings_bhat)):
        create_list.append(i + 1)
    indexed_IOC = dict(zip(create_list, nth_strings_bhat))
    sort_index_IOC = sorted(
        indexed_IOC, key=lambda dict_key: abs(indexed_IOC[dict_key])
    )
    return sort_index_IOC[::-1]


print(probable_key_length(string))

# new_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# divided_string = []
# for i in range(7):
#    divided_string.append(string[i::7])

# nestlist = []
# for i in range(len(divided_string)):
#    nestlist.append(key_ceaser(divided_string[i]))
# print(nestlist)

# keys = []
# answers = []
# for j in range(9):
#    for i in range(len(divided_string)):
#        answers.append(chr(nestlist[i][j] + 97))
#    keys.append("".join(answers))
#    answers = []

# print(answers)
# print(keys)
# print(nestlist[0][0])


def get_vigenere_keys(string, key_length):
    divided_string = []
    for i in range(key_length):
        divided_string.append(string[i::key_length])
    nestlist = []
    for i in range(len(divided_string)):
        nestlist.append(key_ceaser(divided_string[i]))
    keys = []
    answers = []
    for j in range(9):
        for i in range(len(divided_string)):
            answers.append(chr(nestlist[i][j] + 97))
        keys.append("".join(answers))
        answers = []
    return keys


print(get_vigenere_keys(string, 7))

########list of unindexed IOC's


# print(nth_strings)
# print(nth_strings_bhat)


# order lowest to highest

# lowest most probable key lenght


############################################  End of Keyless decryption tools###################################

