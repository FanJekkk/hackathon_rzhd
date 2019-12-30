import matplotlib.pyplot as plt


def open_data(name):
    f = open(name)
    lines = f.read().split('\n')
    ret = []
    for i in range(0, len(lines) - 1):
        split = lines[i].split('\t')
        new_rec = [int(split[0]), float(split[1]), float(split[2]), int(split[3])]
        ret.append(new_rec)
    return ret


def filter_data(in_data):
    ret = []
    j = 2  # 1 rpm 2 power
    s = 0
    tol = 0.05
    prev = in_data[0][j]
    for rec in in_data:
        if rec[3] > 0 and rec[2] > 0 and rec[1] > 0 and prev > 0:
            if (rec[j] - prev) / prev < tol:
                s += 1
            else:
                s = 0
            if s > 5:
                ret.append(rec)
        else:
            s = 0
        prev = rec[j]
    return ret


# открытие и фильтрация данных
unfiltered = open_data('lokodata_12.txt')
print('Количество записей:\n%i' % len(unfiltered))
filtered = filter_data(unfiltered)
print('Количество записей после фильтрации:\n%i' % len(filtered))

# разделение на чётные и нечётные позиции контроллера
even_x = []
even_y = []
odd_x = []
odd_y = []
for record in filtered:
    if record[3] % 2 == 0:
        even_x.append(record[1])
        even_y.append(record[2])
    else:
        odd_x.append(record[1])
        odd_y.append(record[2])

# отображение
fig = plt.figure()
ax = plt.gca()
ax.scatter(even_x, even_y, c='navy', s=4)
ax.scatter(odd_x, odd_y, c='darkcyan', s=4)
ax.set_xlabel(u'rpm')
ax.set_ylabel(u'power')
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
#fig.savefig('grafs/graf_12')  # сохранение рисунка png в папку с проектом
plt.show()
