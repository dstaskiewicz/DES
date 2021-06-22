IP_ARRAY = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
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
# def encryption:


file = open("input.txt", "rb")
data = file.read()
nameless_array = []

for i in range(len(data)):
    nameless_array.append(data[i])
    if i % 64 == 63:
        # initial permutation
        LPT, RPT = initial_permutation(nameless_array)
        nameless_array = []

        # encryption

