import time
import psutil
import os

#***********************************************************************************************************************
# Задача 3.
# Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
#***********************************************************************************************************************

def delta_mem(f):      # Декоратор измеряющий потребленную оперативную память функцией f.

    def wrapped(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        mem_start = proc.memory_info().rss/1000000
        print('Используемая память до выполнения ф-ции delta_time', mem_start)
        f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        mem_finish = proc.memory_info().rss / 1000000
        print('Используемая память после выполнения ф-ции delta_time', mem_finish)
        print('Потребленная оперативная память ', mem_finish - mem_start, 'Mb')
        return f(*args, *kwargs)
    return wrapped

@delta_mem
def delta_time(ff):     # Декоратор измеряющий затраченное время на выполнение функции f.

    def wrapped(*args, **kwargs):
        time_start = time.time()
        ff(*args, **kwargs)
        time_finish = time.time()
        delta_time = time_finish - time_start
        print('Время выполнения :', delta_time, ' c')
    return wrapped

@delta_time
def cr_list(x):

    x_list = [i**2  for i in range(1, x + 1) ]
    return x_list

print()
print('Задача 2.')
num = 1000000

print('Создание листа c элементами ')
cr_list(num)
