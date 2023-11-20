# TODO Найдите количество книг, которое можно разместить на дискете
ONE_BYTE = 4

count_let = 100
count_str = 50
count_sym = 25

value_disk = 1.44 * 1024 * 1024 #размер диска в байтах
syms = count_sym * count_str * count_let * ONE_BYTE
total = int(value_disk // syms)

print("Количество книг, помещающихся на дискету:", total)
