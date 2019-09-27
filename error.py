# Подпрограмма для записи ошибок в файл
# Горьковец Ксения

def fun_error(txt, line_t=""):  # Функция записи ошибок в файл
    with open("error.txt", "a", encoding='utf-8') as error_txt:  # открываем файл ошибок
        error_txt.write(line_t + txt + "\n")
    return