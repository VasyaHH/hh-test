# 1. Тропический остров
# Предположим, в один прекрасный день вы оказались на острове прямоугольный формы.
# Ландшафт этого острова можно описать с помощью целочисленной матрицы размером MxN,
# каждый элемент которой задаёт высоту соответствующей области острова над уровнем моря.
#
# К примеру, вот небольшой остров размером 3x3:
# 4 5 4
# 3 1 5
# 5 4 1
#
# В сезон дождей остров полностью заливает водой и в низинах скапливается вода.
# Низиной будем считать такую область острова, клетки которой граничат с клетками,
# большими по высоте. При этом диагональные соседи не учитываются, а уровень моря
# принимается за 0. В приведённом выше примере на острове есть только одна низина —
# это клетка со значением 1 в середине острова (она граничит с клетками высотой 3, 5, 5 и 4).
#
# Таким образом, после дождя высота клеток острова изменится и станет следующей:
# 4 5 4
# 3 3 5
# 5 4 1
#
# Мы видим что в данном примере высота низины изменилась с 1 до 3,
# после чего вода начала переливаться на соседние клетки,
# а затем — в море. Общий объём воды, скопившейся на острове — 2 кубические клетки.
#
# Вот пример посложнее:
#
# 5 3 4 5
# 6 2 1 4
# 3 1 1 4
# 8 5 4 3
#
# После дождя карта острова принимает следующую форму:
#
# 5 3 4 5
# 6 3 3 4
# 3 3 3 4
# 8 5 4 2
#
# Общий объём скопившейся после дождя воды на таком острове
# составляет целых 7 кубических клеток!
#
# Ваша программа должна читать входные данные из stdin.
# В первой строке указывается количество островов K,
# после чего в следующих строках описываются эти K островов.
# В первой строке описания острова задаются его размеры N и M —
# целые числа в диапазоне [1, 50], разделённые пробелом.
# В следующих строках описывается матрица NxM со значениями
# высот клеток острова, которые могут принимать значения из диапазона [1, 1000].
#
# Вот пример входных данных:
#
# 3
# 3 3
# 4 5 4
# 3 1 5
# 5 4 1
# 4 4
# 5 3 4 5
# 6 2 1 4
# 3 1 1 4
# 8 5 4 3
# 4 3
# 2 2 2
# 2 1 2
# 2 1 2
# 2 1 2
#
# Ваша программа должна выводить в stdout значения общего объёма воды,
# скапливающейся на острове после сезона дождей для каждого из входных примеров.
# Для приведённых выше данных, вывод программы должен быть следующим:
#
# 2
# 7
# 0

import sys


def generate_low_map(isle):
    row_count = len(isle)
    row_len = len(isle[0])

    def is_low_elem(strn, elemn):
        for cell in [[strn, elemn - 1], [strn, elemn + 1], [strn - 1, elemn], [strn + 1, elemn]]:
            try:
                if isle[strn][elemn] > isle[cell[0]][cell[1]]:
                    return False
            except IndexError:
                pass
        return True

    lows = [([0]*row_len) for i in range(row_count)]
    for x, row in enumerate(isle):
        for y, el in enumerate(row):
            if is_low_elem(x, y):
                lows[x][y] = 1
    return lows


def is_can_save_water(low_map):

    def zero_neighbour(zx, zy):
        for xy in [[zx, zy-1], [zx, zy+1], [zx-1, zy], [zx+1, zy]]:
            try:
                if low_map[xy[0]][xy[1]] == 1:
                    low_map[xy[0]][xy[1]] = 0
                    zero_neighbour(xy[0], xy[1])

            except IndexError:
                pass
                # print("out of range")

    row_len = len(low_map[0])
    row_count = len(low_map)

    for x in range(row_count):
        for y in range(row_len):
            if x in [0, row_count-1] or y in [0, row_len-1]:
                if low_map[x][y] == 1:
                    low_map[x][y] = 0
                    zero_neighbour(x, y)
    for x in range(row_count):
        for y in range(row_len):
            if low_map[x][y] == 1:
                return True
    return False


def answer(island):
    low_map = generate_low_map(island)
    summ = 0
    while is_can_save_water(low_map):
        for s in low_map:
            summ += sum(s)

        row_len = len(island[0])
        row_count = len(island)

        for x in range(row_count):
            for y in range(row_len):
                island[x][y] += low_map[x][y]
        low_map = generate_low_map(island)
    return summ

# print("COUNT")
count = sys.stdin.readline().strip('\n')
if not count.isdigit():
    exit("Wrong islands count")

for s in range(int(count)):
    # print("SIZE:")
    size = sys.stdin.readline().strip("\n").split(" ")
    size = [int(x) for x in size if x.isdigit() and 1 <= int(x) <= 50]
    if len(size) != 2:
        exit("Wrong island size")
    # print("LINES")
    island_map = list()
    n = size[1]
    for m in range(size[0]):
        line = sys.stdin.readline().strip('\n').split(" ")
        line = [int(x) for x in line if x.isdigit() and 1 <= int(x) <= 1000]
        if len(line) != n:
            exit("Wrong island map")
        island_map.append(line)
    print(answer(island_map))




