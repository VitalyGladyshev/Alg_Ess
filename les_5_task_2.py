def get_hex_list(str_num):
    str_num = str_num.lower()
    hex_number_list = []
    corr_val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for letter in str_num:
        if letter in corr_val:
            hex_number_list.append(letter)
        else:
            return -1
    return hex_number_list


def get_digit(letter):
    to_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
                'c': 12, 'd': 13, 'e': 14, 'f': 15}
    return to_digit[letter]


def get_letter(digit):
    to_letter = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    return to_letter[digit]


def make_res(inc_res):
    res = []
    for el in reversed(inc_res):
        res.append(el)
    return res


def hex_sum(num_1, num_2):
    tmp_num_1 = num_1.copy()
    tmp_num_2 = num_2.copy()
    res_tmp = []
    transfer = 0
    len_1 = len(tmp_num_1)
    len_2 = len(tmp_num_2)
    if len_1 > len_2:
        for i in range(len_1 - len_2):
            tmp_num_2.insert(0, '0')
    elif len_1 < len_2:
        for i in range(len_2 - len_1):
            tmp_num_1.insert(0, '0')
    for c_1, c_2 in zip(reversed(tmp_num_1), reversed(tmp_num_2)):
        sm = get_digit(c_1) + get_digit(c_2) + transfer
        if sm < 16:
            res_tmp.append(get_letter(sm))
            transfer = 0
        else:
            res_tmp.append(get_letter(sm - 16))
            transfer = 1
    if transfer:
        res_tmp.append(get_letter(1))
    return make_res(res_tmp)


def hex_mult_on_one_digit(num, digit):
    res_tmp = []
    m_transfer = 0
    for el in reversed(num):
        sm = get_digit(el) * get_digit(digit) + m_transfer
        if sm < 16:
            res_tmp.append(get_letter(sm))
            m_transfer = 0
        else:
            res_tmp.append(get_letter(sm & 15))
            m_transfer = sm >> 4
    if m_transfer:
        res_tmp.append(get_letter(m_transfer))
    return make_res(res_tmp)


def hex_mult(num_1, num_2):
    sum_of_mul = []
    for el, ind in zip(reversed(num_2), range(len(num_2))):
        tmp = hex_mult_on_one_digit(num_1, el)
        for tr in range(ind):
            tmp.append('0')
        sum_of_mul = hex_sum(sum_of_mul, tmp)
    return sum_of_mul


number_1 = get_hex_list(input("Введите первое шестнадцатеричное число: "))
if number_1 == -1:
    print("Некорректный ввод!")
    exit()
number_2 = get_hex_list(input("Введите второе шестнадцатеричное число: "))
if number_2 == -1:
    print("Некорректный ввод!")
    exit()

print(f'Сумма чисел: {hex_sum(number_1, number_2)}')
print(f'Произведение чисел: {hex_mult(number_1, number_2)}')
