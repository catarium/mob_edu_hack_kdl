from matplotlib import pyplot as plt
import numpy as np
import time


def year_graph_line(values_up: list) -> str:
    plt.clf()
    num = np.arange(1, 13)
    plt.plot(num, values_up, 'r-o')
    plt.xlabel('Номера месяцев')
    plt.ylabel('Очки в месяц')
    plt.title('Успеваемость')
    plt.xticks(num)
    path = f''  # Допиши здесь путь сохранения для сохранения фотки
    plt.savefig(path)
    return path