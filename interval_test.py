# Подпрограмма для нахождения ошибок в интервале времени
# Горьковец Ксения

from math import sqrt
from error import fun_error

def fun_interval(
        Time, sTime, meteo_data, sost_sen, control_sum, interval):

    i = 0
    k = 0
    s = 0
    cp = 0
    s_raznosti = 0  # Сумма разности между значением интервала и его средним значением
    cp_kv_otkl = 0

    for i in interval:
        s += i

    cp = s/len(sTime)

    for i in interval:
        s_raznosti += (i-cp)*(i-cp)

    cp_kv_otkl = round(sqrt(s_raznosti/len(sTime)),3)

    if cp_kv_otkl < 1:
        cp_kv_otkl = cp_kv_otkl + 1

    cp_kv_otkl = cp_kv_otkl * 3

    cp_cp_kv_otkl = cp - cp_kv_otkl

    if cp_cp_kv_otkl < 0:
        cp_cp_kv_otkl = 0.001

    i = 0
    count = -1

    for i in interval:
        count += 1
        k += 1

        if interval[count] > (cp+cp_kv_otkl) or interval[count] < cp_cp_kv_otkl:
            fun_error("Ошибка в интервале времени", Time[k] + "\t")
            del Time[k]
            del sTime[k]
            del meteo_data[k]
            del sost_sen[k]
            del control_sum[k]
            del interval[count]
            k -= 1
            count -= 1

    return