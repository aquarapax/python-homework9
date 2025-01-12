import os
import shutil
from contextlib import contextmanager

@contextmanager
def safe_write(filename):
    # Сохраняем оригинальное состояние файла
    tmp_filename = filename + '.tmp'
    if os.path.exists(filename):
        shutil.copyfile(filename, tmp_filename)  # создаем резервную копию
    else:
        open(tmp_filename, 'w').close()  # создаем пустой файл, если его нет

    try:
        with open(filename, 'w') as file:
            yield file
    except Exception as e:
        # В случае ошибки, восстанавливаем оригинальный файл
        shutil.move(tmp_filename, filename)  # восстанавливаем оригинал
        print(f'Во время записи в файл было возбуждено исключение {type(e).__name__}')
    else:
        # Если все успешно, удаляем временный файл
        os.remove(tmp_filename)

# Тестирование
if __name__ == "__main__":
    # Вход 1
    with safe_write('data.txt') as file:
        file.write('Я знаю, что ничего не знаю, но другие не знают и этого.')

    with open('data.txt') as file:
        print(file.read())

    # Вход 2
    with safe_write('data.txt') as file:
        file.write('Я знаю, что ничего не знаю, но другие не знают и этого. \n')

    try:
        with safe_write('data.txt') as file:
            print('Если ты будешь любознательным, то будешь много знающим.', file=file, flush=True)
            raise ValueError
    except Exception:
        pass  # Игнорируем выброшенное исключение для этого примера

    with open('data.txt') as file:
        print(file.read())