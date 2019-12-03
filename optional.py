def function(n):
    return -n[1]

f = open('new.txt', encoding = 'utf-8')
file = f.read().split()
a = [[file[0], 1]]
lenth_a = 1
for item in file:
    word = 0
    flag_if_word = True
    for i in item:
        if not ((i >= 'а' and i <= 'я') or (i >= 'А' and i <= 'Я') or i == 'ё' or i == 'Ё' or (i == '-' and word > 0)): #проверяю, слово ли это или знак
            flag_if_word = False
        word += 1
    i = 0
    while flag_if_word and i < lenth_a and a[i][0] != item:
        i += 1
    if i == lenth_a:
        a.append([item, 1])
        lenth_a += 1
    elif a[i][0] == item:
        a[i][1] += 1
a.sort(key = function)
print((', ').join([a[i][0] for i in range(min(len(a), 10))]), end = '')


f.close()