# Подпрограмма для нахождения ошибок в метео данных
# Горьковец Ксения

from math import sqrt
from error import fun_error

def fun_meteo_data(
        Time, sTime, meteo_data, sost_sen, control_sum):

    check_interv = 5
    i = 0
    k = 0

    for k in range(len(meteo_data) - 1):
        if meteo_data[k] == " 99999" or meteo_data[k] == "//////":
            if k == (len(meteo_data) - 1):
                fun_error("Данные отсутсвуют")
                break
            del Time[k]
            del sTime[k]
            del meteo_data[k]
            del sost_sen[k]
            del control_sum[k]
            k -= 1
            if i > len(meteo_data) - check_interv:
                fun_error("Недостаточно данных для проверки значений")
                break
            i += 1
        continue

    count = 0
    k = 0

    if i < len(meteo_data) - check_interv:

        while True:
            s = 0
            cp = 0
            s_raznosti = 0
            i = 0
            k = count

            while i < check_interv:
                s += float(meteo_data[k].strip())
                i += 1
                k += 1

            cp = s / check_interv

            i = 0
            k = count

            while i < check_interv:
                s_raznosti += (float(meteo_data[k].strip()) - cp) *\
                              (float(meteo_data[k].strip()) - cp)
                i += 1
                k += 1
            cp_kv_otkl = round(sqrt(s_raznosti / len(meteo_data)), 3)

            if cp_kv_otkl < 1:
                cp_kv_otkl = cp_kv_otkl + 1

            cp_kv_otkl = cp_kv_otkl * 3

            if float(meteo_data[count + check_interv]) > cp + cp_kv_otkl or \
                    float(meteo_data[count + check_interv]) < cp - cp_kv_otkl:
                fun_error("Ошибка в значение датчика", Time[count + check_interv] + "\t")

            if count + check_interv == (len(meteo_data) - 1) - check_interv:
                break

            count += 1

        fun_error("Обратная проверка")

        count = len(meteo_data) - 1
        k = 0

        while True:
            s = 0
            cp = 0
            s_raznosti = 0
            i = 0
            k = count
            while i < check_interv:
                s += float(meteo_data[k].strip())
                i += 1
                k -= 1
            cp = s / check_interv

            i = 0
            k = count

            while i < check_interv:
                s_raznosti += (float(meteo_data[k].strip()) - cp) *\
                              (float(meteo_data[k].strip()) - cp)
                i += 1
                k -= 1
            cp_kv_otkl = round(sqrt(s_raznosti / len(meteo_data)), 3)

            if cp_kv_otkl < 1:
                cp_kv_otkl = cp_kv_otkl + 1

            cp_kv_otkl = cp_kv_otkl * 3

            if float(meteo_data[count - check_interv]) > cp + cp_kv_otkl or \
                    float(meteo_data[count - check_interv]) < cp - cp_kv_otkl:
                fun_error("Ошибка в значение датчика", Time[count - check_interv] + "\t")

            if count - check_interv == 0:
                break

            count -= 1
    return None