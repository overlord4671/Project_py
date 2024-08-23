import tkinter as tk


def get_values():
    num1 = int(number_1_entry.get())
    num2 = int(number_2_entry.get())
    return num1, num2


def insert_values(values):
    number_3_entry.delete(0, 'end')
    number_3_entry.insert(0, values)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('400x350')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=6, height=3, command=add)
button_add.place(x=10, y=250)
button_sub = tk.Button(window, text='-', width=6, height=3, command=sub)
button_sub.place(x=120, y=250)
button_mul = tk.Button(window, text='*', width=6, height=3, command=mul)
button_mul.place(x=240, y=250)
button_div = tk.Button(window, text='/', width=6, height=3, command=div)
button_div.place(x=340, y=250)

number_1_entry = tk.Entry(window, width=25)
number_1_entry.place(x=15, y=50)
number_1_label = tk.Label(window, text='Введите первое число:')
number_1_label.place(x=15, y=25)

number_2_entry = tk.Entry(window, width=25)
number_2_entry.place(x=235, y=50)
number_2_label = tk.Label(window, text='Введите второе число:')
number_2_label.place(x=235, y=25)

number_3_entry = tk.Entry(window, width=35)
number_3_entry.place(x=100, y=150)
number_3_label = tk.Label(window, text='Ответ:')
number_3_label.place(x=100, y=125)
window.mainloop()
