import time

#***********************************************************************************************************************
# Задача 1.
# Написать декоратор, замеряющий время выполнение декорируемой функции.
#***********************************************************************************************************************

def delta_time(ff):

    def obertka(*args, **kwargs):
        time_start = time.time()
        ff(*args, **kwargs)
        time_finish = time.time()
        delta_time = time_finish - time_start
        print('Время выполнения :', delta_time, ' c')
    return obertka


@delta_time
def my_add(x,y):
    for i in range(10000000):
        k = 0
    return  print('Сумма равна',x+y)

print()
print('Задача 1.')
print()
my_add(100,300)

#***********************************************************************************************************************
# Задача 2.
# Сравнить время создания генератора и списка с элементами:
# натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).
#***********************************************************************************************************************

def cr_list()
    return


#***********************************************************************************************************************
# Задача 3.
# Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
#***********************************************************************************************************************

#***********************************************************************************************************************
# Задача 4.
# Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами:
# натуральные числа от 1 до 1000000.
#***********************************************************************************************************************