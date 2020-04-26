import time
import psutil
import os

#***********************************************************************************************************************
# Задача 4.
# Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами:
# натуральные числа от 1 до 1000000.
#***********************************************************************************************************************

def delta_mem(f):      # Декоратор измеряющий потребленную оперативную память функцией f.

    def wrapped(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        mem_start = proc.memory_info().rss/1000000
        f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        mem_finish = proc.memory_info().rss / 1000000
        print('Потребленная оперативная память ', mem_finish - mem_start, 'Mb')
        return f(*args, *kwargs)
    return wrapped

@delta_mem
def cr_list(x):

    x_list = [i**2  for i in range(1, x + 1) ]
    return x_list

@delta_mem
def cr_gen(x):
    for i in range(1, x+1):
        y = i**2
        yield y

print()
print('Задача 2.')
num = 1000000

print('Создание листа c элементами ')
cr_list(num)

print()
print('Создание генератора ')
cr_gen(num)