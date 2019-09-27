# Подпрограмма для нахождения ошибок в состояние датчика
# Горьковец Ксения

from error import fun_error

def fun_sost_sen(
        Time, sTime, meteo_data, sost_sen, control_sum):
    k = 0

    for sost in sost_sen:
        if sost != "НОРМА":
            if sost == "СБОЙ ":
                fun_error("Состояние датчика СБОЙ", Time[k] + "\t")
                k += 1
                continue
            if sost == "РЕЖИМ":
                fun_error("Состояние датчика РЕЖИМ", Time[k] + "\t")
                k += 1
                continue
            fun_error("Ошибка в состояние датчика", Time[k] + "\t")
            del Time[k]
            del sTime[k]
            del meteo_data[k]
            del sost_sen[k]
            del control_sum[k]

        k += 1
    return