from Tasks.sort_str_task_1 import sort_str
from Tasks.call_func_task_2 import find_true_value
from Tasks.signals_task_3 import signals

if __name__ == "__main__":
    print("Первое задание: ")
    sort_str()

    print("Второе задание: ")
    true_a = 10
    true_b = None
    true_c = None
    iteration_count, true_value = find_true_value(true_a=true_a, true_b=true_b, true_c=true_c)
    print(f'Количество итераций: {iteration_count}')
    if true_value:
        print(f'Найдено истинное значение: a={true_value[0]}, b={true_value[1]}, c={true_value[2]}')
    else:
        print('Истинное значение не найдено')

    print("Третье задание: ")
    signals()