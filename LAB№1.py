import csv

with open('Книга1.csv') as File:
    reader = csv.reader(File)
    # Переменные:

    # - для 2 и 3 пунктов
    kol_zapicey = 0
    kol_zapicey_bolee30 = 0

    # - для 4 пункта
    autor = input("")
    poisk_po_autoru = []
    m1 = []

    # - для 5 пункта
    zapicey_20 = []
    m2 = []

    for row in reader:
        # преобразование строк в массивы с разделением каждой характеристики в строчный тип данных
        i = ''.join(row)
        i = i.replace(";;", ";")
        f = i.split(";")
        # счётчик для подсчёта записей
        kol_zapicey += 1
        # 3 пункт
        if len(f[1]) > 30:
            kol_zapicey_bolee30 += 1
        # 4 пункт
        if (autor in f[3]) and (("2015" in f[6]) or ("2018" in f[6])):
            poisk_po_autoru.append(f)
        # 5 пункт
        if 2 <= kol_zapicey <= 21:
            zapicey_20.append(f)

    numeratsia = 0
    # для удобства при реализации 4 пункта
    for n in poisk_po_autoru:
        numeratsia += 1
        s = str(numeratsia) + ". " + n[0] + ", " + n[1] + ", " + n[2] + ", " + n[3] + ", " + n[4] + ", " + n[5] + ", " + \
            n[
                6] + ", " + n[7] + ", " + n[8] + ", " + n[9] + ", " + n[
                10] + ";"
        m1.append(s)
    n1 = ''.join(m1)
    f0 = n1.split(";")
    # создание файла текстового формата для удобства
    fail = open("spisok4.txt", "w")
    fail.writelines("%s\n" % i for i in f0)
    fail.close()
    fail0 = open("spisok4.txt", "r").read()

    numeratsia1 = 0
    # 5 пункт
    # формирование 20 записей: библиографических ссылок вида <автор>. <название> - <год>
    for i in zapicey_20:
        numeratsia1 += 1
        s = str(numeratsia1) + ". " + i[3] + ". " + i[1] + " - " + i[6] + ";"
        m2.append(s)
    i1 = ''.join(m2)
    f1 = i1.split(";")
    # создание файла текстового формата
    fail1 = open("spisok5.txt", "w")
    fail1.writelines("%s\n" % i for i in f1)
    fail1.close()
    fail2 = open("spisok5.txt", "r").read()

print("2 пункт: ", kol_zapicey)
print("3 пункт: ", kol_zapicey_bolee30)
print("4 пункт: ")
print(fail0)
print("5 пункт:")
print(fail2)
