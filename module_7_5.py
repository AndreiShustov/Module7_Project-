# Домашнее задание по теме "Файлы в операционной системе"

# Цель задания:
# Освоить работу с файловой системой в Python, используя модуль os.
#
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
# и использование модуля time для корректного отображения времени.
#
# Задание:
#
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.
#
# Комментарии к заданию:
#
# Ключевая идея – использование вложенного for
#
# for root, dirs, files in os.walk(directory):
#     for file in files:
#       filepath = ?
#       filetime = ?
#       formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#       filesize = ?
#       parent_dir = ?
#       print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,
#               Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
#
#
# Так как в разных операционных системах разная схема расположения папок,
# тестировать проще всего в папке проекта (directory = “.”)
#
# Пример возможного вывода:
#
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11,
# Родительская директория.

import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):

    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)

        print(f'Обнаружен файл: {file},'
              f' Путь: {file_path}, '
              f'Размер: {file_size} байт, '
              f'Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
