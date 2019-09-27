 # Программа для чтения архивного файла и нахождения в нём ошибок
 # Горьковец Ксения

from math import sqrt, fabs
from error import fun_error
from interval_test import fun_interval
from sost_sen_test import fun_sost_sen
from meteo_data_test import fun_meteo_data

# открываем файл ошибок для очистки
with open("error.txt", "w+", encoding='utf-8') as error_txt:
    txterror = error_txt.read()

with open("PPP_043.TXT", "r+", encoding='utf-8') as file_txt:
    first_line = file_txt.readline()
    a = first_line.find("Датчик")
    sencer = first_line[a:a+10]
    nom_sen = int(first_line[a+7:a+10])  # номер датчика

    Time = []      # Время в ч,м,с
    sTime = []     # Время в сек
    interval = []  # Интервал времени
    meteo_data = []
    sost_sen = []
    control_sum = []

    i = 0

    # Делаем проверку на время
    for line in file_txt.readlines():
        if line[0] < "0" and line[0] > "9":
            continue
        if line[1] < "0" and line[1] > "9":
            continue
        if line[2] != ":":
            continue
        if line[3] < "0" and line[3] > "9":
            continue
        if line[4] < "0" and line[4] > "9":
            continue
        if line[5] != ":":
            continue
        if line[6] < "0" and line[6] > "9":
            continue
        if line[7] < "0" and line[7] > "9":
            continue

        # Часы
        if line[0:2] < "00" or line[0:2] > "23":
            fun_error("Ошибка в часах", line[0:8] + "\t")
            continue
        T = float(line[0:2]) *3600

        # Минуты
        if line[3:5] < "00" or line[3:5] > "59":
            fun_error("Ошибка в минутах", line[0:8] + "\t")
            continue
        T = float(line[3:5]) *60 + T

        # Секунды
        if line[6:8] < "00" or line[6:8] > "59":
            fun_error("Ошибка в секундах", line[0:8] + "\t")
            continue
        sTime.append(float(line[6:8]) + T)
        Time.append(line[0:8])

        # Записываем интервал времени не с нуля
        if i > 0 and i < len(sTime):
            interval.append(fabs(sTime[i-1]-sTime[i]))
        i += 1

        meteo_data.append(line[11:17])
        sost_sen.append(line[-10:-5])
        control_sum.append(line[-4:-1])

    fun_interval(Time, sTime, meteo_data, sost_sen, control_sum, interval)
    fun_sost_sen(Time, sTime, meteo_data, sost_sen, control_sum)
    fun_meteo_data(Time, sTime, meteo_data, sost_sen, control_sum)
    
    fun_error("Проверка завершена")