import tkinter
from tkinter import filedialog, messagebox
import os


def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ("Все файлы ", '*')))
    text['text'] += ('' + filename)
    os.startfile(filename)


def show_instructions():
    instructions = (
        "Инструкция по использованию блокнота:\n"
        "1. Нажмите кнопку 'Выберите файл', чтобы открыть файл для редактирования.\n"
        "2. Редактируйте содержимое файла в открывшемся окне блокнота.\n"
        "3. Файл автоматически открывается для редактирования через стандартный текстовый редактор.\n"
        "4. Для выхода из программы нажмите кнопку 'Выход'."
    )
    messagebox.showinfo("Инструкция", instructions)


window = tkinter.Tk()
window.title("Проводник")
window.geometry('450x350')
window.configure(bg='black')
window.resizable(False, False)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Метка с выбранным файлом
text = tkinter.Label(window, text='Файл:', height=2, width=70, background='silver', foreground='black',
                     font=("Arial", 8, "bold"))
text.grid(column=1, row=1, padx=10, pady=10)

# Кнопка выбора файла
button_select = tkinter.Button(window, width=30, height=2, text='Выберите файл', foreground='black', font=("Arial", 10)
                               , command=file_select)
button_select.grid(column=1, row=3, padx=10, pady=10)

# Кнопка выхода
button_exit = tkinter.Button(window, width=30, height=2, text='Выход', foreground='white', background='#8B1129',
                             font=("Arial", 10), command=window.quit)
button_exit.grid(column=1, row=4, padx=10, pady=10)

# Кнопка с инструкцией
button_help = tkinter.Button(window, width=30, height=2, text='Инструкция', foreground='black', font=("Arial", 10),
                             command=show_instructions)
button_help.grid(column=1, row=5, padx=10, pady=10)

# Метка с версией и разработчиком
version_label = tkinter.Label(window, text='v1.0.0 IL', bg='black', fg='white', font=("Arial", 8, "italic"))
version_label.grid(column=2, row=6, padx=10, pady=10, sticky='se')

window.mainloop()
