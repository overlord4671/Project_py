import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog


def calculate_coefficients(K, T1, T2, T3):
    # Вычисление коэффициентов передаточной функции
    a0 = K + 1
    a1 = (T1 + T2 + T3)
    a2 = (T1 * T2 + T1 * T3 + T2 * T3)
    a3 = T1 * T2 * T3

    return a0, a1, a2, a3


def compute_U_V(omega, a0, a1, a2, a3):
    U_values = a0 - a2 * omega ** 2
    V_values = a1 * omega - a3 * omega ** 3
    return U_values, V_values


def plot_michailov(a0, a1, a2, a3):
    # Массив значений ω
    omega = np.linspace(0, 10, 400)

    # Вычисляем значения U и V
    U_values, V_values = compute_U_V(omega, a0, a1, a2, a3)

    # Определение устойчивости системы
    crossings = np.sum(np.diff(np.sign(U_values)) != 0)
    is_stable = crossings == 0

    # Строим график
    plt.figure(figsize=(10, 6))
    plt.plot(U_values, V_values, label='Годограф Михайлова', color='b')

    # Настраиваем оси и легенду
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('Действительная часть (U)')
    plt.ylabel('Мнимая часть (V)')
    plt.title('Годограф Михайлова')
    plt.legend()

    # Вывод устойчивости системы
    if is_stable:
        plt.text(min(U_values), max(V_values), 'Система устойчива', fontsize=12, color='g')
    else:
        plt.text(min(U_values), max(V_values), 'Система неустойчива', fontsize=12, color='r')

    plt.show()


def get_inputs():
    # Создание окна для ввода данных
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно

    K = float(simpledialog.askstring("Input", "Введите значение K:", parent=root))
    T1 = float(simpledialog.askstring("Input", "Введите значение T1:", parent=root))
    T2 = float(simpledialog.askstring("Input", "Введите значение T2:", parent=root))
    T3 = float(simpledialog.askstring("Input", "Введите значение T3:", parent=root))

    return K, T1, T2, T3


if __name__ == "__main__":
    K, T1, T2, T3 = get_inputs()
    a0, a1, a2, a3 = calculate_coefficients(K, T1, T2, T3)
    plot_michailov(a0, a1, a2, a3)
