# 2. Бесконечная последовательность
# Возьмём бесконечную цифровую последовательность, образованную склеиванием
# последовательных положительных чисел: S = 123456789101112131415...
# Определите первое вхождение заданной подпоследовательности A в бесконечной
# последовательности S (нумерация начинается с 1).
#
# Программа должна читать данные из stdin и выводить ответы в stdout.
#
# Пример входных данных (по одной подпоследовательности на строку,
# максимальная длина подпоследовательности — 50 символов):
# 6789
# 111
#
# Пример выходных данных:
# 6
# 12

import sys


def get_full_number(num1, num2):
    # фунция находит два полных числа последовательности, если имеются только их обрывки
    # 8466, 8467 -> 6684
    # и возвращает первое их них
    full_number = -1
    for i in range(max(len(num1), len(num2))+1, len(num1+num2)+1, ):
        r = list("1".rjust(i, "0"))
        x1 = list(num1.rjust(i, "x"))
        x2 = list(num2.ljust(i, "x"))
        # print(x2)
        # print(x1)
        n = len(x2)-1
        of = 0
        while x2[n] == "x":
            if int(x1[n]) + int(r[n]) + of > 9:
                x2[n] = str(int(x1[n]) + int(r[n]) + of - 10)
                of = 1
            else:
                x2[n] = str(int(x1[n]) + int(r[n]) + of)
                of = 0
            n -= 1

        fnum = int("".join(x2)) - 1
        for g in range(len(x1)):
            if x1[g] == "x":
                x1[g] = str(fnum)[g]

        # print(x2)
        # print(x1)
        if int("".join(x2)) - int("".join(x1)) == 1:
            if full_number == -1:
                full_number = int("".join(x1))
            else:
                if int("".join(x1)) <= full_number:
                    full_number = int("".join(x1))
        # print()
        # print(x2)
        # print(x1)
    return full_number


def get_sequence_number(test):
    if int(test) == 0:
        return int("1"+test)
    min_number = -1
    begin = 0
    for elem_len1 in range(1, len(test) - begin + 1):
        for begin in range(elem_len1+1):
            start = begin
            elem_len = elem_len1
            val = int(test[start:start + elem_len])
            while True:
                str_elem = test[start:start + elem_len]
                if str_elem[0] == "0":
                    break
                elem = int(str_elem)
                # print(elem)

                # элемент не с начала строки
                if start == begin and start != 0:

                    # если число состоит из обрезков: конца и начала 1234 1235 -> 3412
                    res = int(get_full_number(test[0:start], test[start:]))
                    if min_number == -1 or min_number >= res:
                        min_number = res

                        # если берем элемент не с начала строки, то вычитаем из него 1,
                        # и сравниваем с предыдущим обрезанным элементом
                    ddd = str(elem-1)[len(str(elem-1))-len(test[0:start]):]
                    if ddd != test[0:start]:
                        break
                    # print("x%s" % ddd)
                    # print(elem-1)
                    val = elem - 1



                # print(elem)

                pos = test.find(str(elem + 1))
                if pos != start + len(str(elem)):
                    if start + len(str(elem)) == len(test):
                        # это последний элемент в введенном числе
                        # print("OP11111111111111111")  # JOB DONE
                        if min_number == -1:
                            return val
                        else:
                            return min(val, min_number)
                    elif len(test) - start - elem_len < len(str(elem + 1)):
                        # если мы здесь, то последний элемент последовательности получился обрезанным
                        # его и проверим на принадлежность к последовательности
                        cutted_full_element = str(elem + 1)[0:len(test) - start - elem_len]
                        # print("Обрезанный до нужной длины полный элемент - %s" % cutted_full_element)
                        # print("Ожидаемый последний элемент - %d" % (elem + 1))
                        last_cutted_element = test[start + elem_len:]
                        # print("Обрезанный последний элемент - %s" % last_cutted_element)
                        if cutted_full_element == last_cutted_element:
                            # print("OP22222222222222222")
                            if min_number == -1:
                                return val
                            else:
                                return min(val, min_number)
                    # print("QUIT BY BREAK")
                    break

                start = pos
                elem += 1
                elem_len = len(str(elem))
    return min_number


def get_pos(first_subseq_number, subsequence):
    summ = 0
    num = first_subseq_number-1
    for x in range(len(str(first_subseq_number))-1):
        summ += 9*(10**x)*(x+1)
        num -= 9*10**x
    summ += num*len(str(first_subseq_number))
    st = ""
    for x in range(first_subseq_number, first_subseq_number + len(subsequence)//len(str(first_subseq_number))+2):
        st += str(x)
    pos = st.find(subsequence)
    if pos != -1:
        summ += pos+1
    else:
        print("WARNING WARNING!!!!!!!")

    return summ


for input_number in sys.stdin:
    input_number = input_number.strip('\n')
    if len(input_number) <= 50 and input_number.isdigit():
        print(get_pos(get_sequence_number(input_number), input_number))
