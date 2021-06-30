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
S_ARRAY = [

    [
        [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
        [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
        [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
        [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],

    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],

    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],

    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],

    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],

    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],

    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
P_ARRAY = [
    16,  7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26,  5, 18, 31, 10,
     2,  8, 24, 14, 32, 27,  3,  9,
    19, 13, 30,  6, 22, 11,  4, 25
]
KEY_PC1_ARRAY = [
    57, 49, 41, 33, 25, 17,  9,  1,
    58, 50, 42, 34, 26, 18, 10,  2,
    59, 51, 43, 35, 27, 19, 11,  3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15,  7, 62, 54, 46, 38,
    30, 22, 14,  6, 61, 53, 45, 37,
    29, 21, 13,  5, 28, 20, 12,  4
]
KEY_PC2_ARRAY = [
    14, 17, 11, 24,  1,  5,  3, 28,
    15,  6, 21, 10, 23, 19, 12,  4,
    26,  8, 16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]


def initial_permutation(array):
    temp1 = [0] * 32
    temp2 = [0] * 32

    for i in range(32):
        temp1[i] = array[IP_ARRAY[i] - 1]

    for i in range(32, 64):
        temp2[i - 32] = array[IP_ARRAY[i] - 1]

    return temp1, temp2


def final_permutation(lpt, rpt):
    temp_connected_array = []
    temp_array = [0] * 64

    for i in range(32):
        temp_connected_array.append(lpt[i])

    for i in range(32):
        temp_connected_array.append(rpt[i])

    for i in range(64):
        temp_array[i] = temp_connected_array[FP_ARRAY[i] - 1]

    return temp_array


def s_expansion(rpt):
    temp = [0] * 48
    for i in range(48):
        temp[i] = rpt[E_ARRAY[i] - 1]
    return temp


def s_permutation(rpt):
    temp = [0] * 32
    for i in range(32):
        temp[i] = rpt[P_ARRAY[i] - 1]
    return temp


def s_box_substitution(array):
    temp_all = []
    for i in range(8):
        temp = [0] * 6
        for j in range(6):
            temp[j] = array[i * 6 + j]
        temp_row = temp[0] * 2 + temp[5]
        temp_column = temp[1] * 8 + temp[2] * 4 + temp[3] * 2 + temp[4]
        for j in range(3, -1, -1):
            temp_all.append((S_ARRAY[i][temp_row][temp_column] >> j) & 1)
    return temp_all


def f_function(rpt, key):
    expanded_rpt = s_expansion(rpt)
    f_array = xor(expanded_rpt, key)
    f_array = s_box_substitution(f_array)
    f_array = s_permutation(f_array)
    return f_array


def key_permutation(key):
    temp1 = [0] * 28
    for i in range(28):
        temp1[i] = key[KEY_PC1_ARRAY[i] - 1]
    temp2 = [0] * 28
    for i in range(28, 56):
        temp2[i-28] = key[KEY_PC1_ARRAY[i] - 1]
    return temp1, temp2


def key_shift(round_num, key):

    if round_num == 1 or round_num == 2 or round_num == 9 or round_num == 16:
        number = 1
    else:
        number = 2
    temp_array = key
    for i in range(number):
        temp_number = temp_array[0]
        for j in range(len(key) - 1):
            temp_array[j] = temp_array[j+1]
        temp_array[len(key) - 1] = temp_number
    return temp_array


def key_transform(left_key, right_key):
    temp_connected_arrays = []
    temp_array = [0] * 48
    for i in range(28):
        temp_connected_arrays.append(left_key[i])
    for i in range(28):
        temp_connected_arrays.append(right_key[i])
    for i in range(48):
        temp_array[i] = temp_connected_arrays[KEY_PC2_ARRAY[i] - 1]

    return temp_array


def xor(array1, array2):
    temp_array = []
    for i in range(len(array1)):
        temp_array.append(array1[i] ^ array2[i])
    return temp_array


def encryption(lpt, rpt, left_key, right_key):
    temp_left_key = left_key
    temp_right_key = right_key
    temp_lpt = lpt
    temp_rpt = rpt
    for i in range(16):
        temp_right_key = key_shift(i + 1, temp_right_key)
        temp_left_key = key_shift(i + 1, temp_left_key)
        key = key_transform(temp_left_key, temp_right_key)
        f_array = f_function(temp_rpt, key)
        temp = temp_lpt
        temp_lpt = temp_rpt
        temp_rpt = xor(f_array, temp)
    return temp_lpt, temp_rpt


def display_and_write(array):
    for i in range(0, len(array), 4):
        hex_num = array[i] * 8 + array[i+1] * 4 + array[i+2] * 2 + array[i+3]
        print(format(hex_num, 'x'), end='')
        output_file.write(str(format(hex_num, 'x')))
    print("")


def display(array):
    for i in range(0, len(array), 4):
        hex_num = array[i] * 8 + array[i+1] * 4 + array[i+2] * 2 + array[i+3]
        print(format(hex_num, 'x'), end='')
    print("")


data_file = open("input.txt", "rb")
key_file = open("keys.bin", "rb")
output_file = open("output.txt", "w")

data = data_file.read()
keys = key_file.read()

data_array = []
keys_array = []

# reading input data into an array bit by bit
for byte in data:
    for bit_num in range(7, -1, -1):
        data_array.append(byte >> bit_num & 1)

# padding of 0s
if len(data_array) % 64:
    for numb in range(64 - (len(data_array) % 64)):
        data_array.append(0)

# reading input of keys into an array bit by bit
for num in range(len(data_array)):
    for bit_num in range(7, -1, -1):
        keys_array.append(keys[num] >> bit_num & 1)

# DES
for num in range(0, len(data_array), 64):
    # initial permutation
    LPT, RPT = initial_permutation(data_array[num:num + 64])
    LEFT_KEY, RIGHT_KEY = key_permutation(keys_array[num:num + 64])
    # encryption
    LPT, RPT = encryption(LPT, RPT, LEFT_KEY, RIGHT_KEY)
    # final permutation with changed order RPT and LPT
    CIPHER_TEXT = final_permutation(RPT, LPT)

    print("PLAIN TEXT:", end='')
    display(data_array[num:num + 64])
    print("KEY:", end='')
    display(keys_array[num:num + 64])
    print("CIPHER TEXT:", end='')
    display_and_write(CIPHER_TEXT)

