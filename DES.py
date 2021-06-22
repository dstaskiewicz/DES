IP_ARRAY = [
    58, 50, 42, 34, 26, 18, 10,  2,
    60, 52, 44, 36, 28, 20, 12,  4,
    62, 54, 46, 38, 30, 22, 14,  6,
    64, 56, 48, 40, 32, 24, 16,  8,
    57, 49, 41, 33, 25, 17,  9,  1,
    59, 51, 43, 35, 27, 19, 11,  3,
    61, 53, 45, 37, 29, 21, 13,  5,
    63, 55, 47, 39, 31, 23, 15,  7
]
FP_ARRAY = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
]
E_ARRAY = [
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
]
S_ROWS = [
    0, 1, 0, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 0, 1, 0, 1,
    2, 3, 2, 3, 2, 3, 2, 3,
    2, 3, 2, 3, 2, 3, 2, 3,
    2, 3, 2, 3, 2, 3, 2, 3,
    2, 3, 2, 3, 2, 3, 2, 3,
]
S_COLUMNS = [
     0,  0,  1,  1,  2,  2,  3,  3,
     4,  4,  5,  5,  6,  6,  7,  7,
     8,  8,  9,  9, 10, 10, 11, 11,
    12, 12, 13, 13, 14, 14, 15, 15,
     0,  0,  1,  1,  2,  2,  3,  3,
     4,  4,  5,  5,  6,  6,  7,  7,
     8,  8,  9,  9, 10, 10, 11, 11,
    12, 12, 13, 13, 14, 14, 15, 15
]
S_ARRAY = [
    [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
    [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
    [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
    [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
]
P_ARRAY = [
    16,  7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26,  5, 18, 31, 10,
     2,  8, 24, 14, 32, 27,  3,  9,
    19, 13, 30,  6, 22, 11,  4, 25
]


def initial_permutation(array):
    temp1 = [0] * 64
    temp2 = [0] * 64
    for i in range(32):
        temp1[i] = array[IP_ARRAY[i] - 1]
    for i in range(32, 64):
        temp2[i] = array[IP_ARRAY[i] - 1]
    return temp1, temp2


def final_permutation(array):
    temp = [0] * 64
    for i in range(64):
        temp[i] = array[FP_ARRAY[i] - 1]
    return temp


def expansion(rpt):
    temp = [0] * 48
    for i in range(48):
        temp[i] = rpt[E_ARRAY[i] - 1]
    return temp


def permutation(rpt):
    temp = [0] * 32
    for i in range(32):
        temp[i] = rpt[P_ARRAY[i] - 1]
    return temp


def s_box_substitution(rpt):
    temp_all = []
    for i in range(8):
        temp = [0] * 6
        temp_number = 0
        for j in range(6):
            temp[j] = rpt[i * 6 + j]
        for j in range(5, -1, -1):
            temp_number += temp[j] * (2 ** j)
        for j in range(3, -1, -1):
            temp_all.append(S_ARRAY[S_ROWS[temp_number]][S_COLUMNS[temp_number]] >> j & 1)
    return temp_all


def encryption(rpt, key):
    expanded_rpt = expansion(rpt)
    # xor with key



file = open("input.txt", "rb")
data = file.read()
nameless_array = []
number_of_bits = 0
for byte in data:
    for bit_num in range(7, -1, -1):
        nameless_array.append(byte >> bit_num & 1)
        number_of_bits += 1
    if number_of_bits == 64:
        # initial permutation
        LPT, RPT = initial_permutation(nameless_array)
        nameless_array = []
        number_of_bits = 0

        # encryption
# for i in range(7, -1, -1):
    # print(124 >> i & 1)