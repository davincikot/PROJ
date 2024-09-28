from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from datetime import datetime as dt
import requests

# Инициализируем переменные и рабочий словарь.
b_code, t1_code, t2_code, coef = '', '', '', 0
vlt = {'RUB': '₽ Рубль (Россия)',
   'USD': '$ Доллар (США)',
   'EUR': '€ Евро (Евросоюз)',
   'GBP': '£ Фунт (Великобритания)',
   'CNY': 'Ұ Юань (Китай)',
   'JPY': '¥ Йена (Япония)',
   'KZT': '₸ Тенге (Казахстан)'}
first_num, second_num, result_num, operation = 0, 0, 0, ''
exchange_history = []

# Объявляем функции обновления полей кодов валют и запуска рабочей функции для работы с обменом валют.
def update_b(event):
    b_label.config(text=vlt[b_combo.get()])
    exchange()


def update_t1(event):
    t1_label.config(text=vlt[t1_combo.get()])
    exchange()


def update_t2(event):
    t2_label.config(text=vlt[t2_combo.get()])
    exchange()

# Объявляем функции для работы с обменом валют и отрисовки дополнительного окна с калькулятором.
def exchange():
    b_code, t1_code, t2_code = b_combo.get(), t1_combo.get(), t2_combo.get()
    if coef != 0 and b_code != '' and (t1_code != '' or t2_code != ''):
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}'); response.raise_for_status()
            if t1_code in response.json()['rates']:
                exchange_rate_t1 = response.json()['rates'][t1_code]
                result_t1 = (exchange_rate_t1 * coef)
                t1_info.config(text=f'{result_t1:.2f}')
                exchange_history.append(f'{dt.now().strftime('%d.%m.%Y %H:%M:%S')} Поле №1: обмен {round(coef, 2)} {vlt[b_code]} на {result_t1:.2f} {vlt[t1_code]}.')
            if t2_code in response.json()['rates']:
                exchange_rate_t2 = response.json()['rates'][t2_code]
                result_t2 = (exchange_rate_t2 * coef)
                t2_info.config(text=f'{result_t2:.2f}')
                exchange_history.append(f'{dt.now().strftime('%d.%m.%Y %H:%M:%S')} Поле №2: обмен {round(coef, 2)} {vlt[b_code]} на {result_t2:.2f} {vlt[t2_code]}.')
                exchange_history.append('\n')
        except Exception as e:
                mb.showerror('Ошибка!', f'Произошла ошибка: {e}.')


def start_exchange():
    global coef
    try:
        b_info.config(text=str(round(float(entry.get()), 2)))
        coef = float(entry.get())
        win_set.destroy()
        exchange()
    except Exception:
        mb.showerror('Ошибка!', 'Поле ввода не может быть пустым!')
        entry.focus()


def set_exchange():
    global entry, win_set, b_code, t1_code, t2_code
    b_code, t1_code, t2_code = b_combo.get(), t1_combo.get(), t2_combo.get()
    if b_code and (t1_code or t2_code):
        win_set = Toplevel()
        win_set.title('Введите сумму!')
        w = win_set.winfo_screenwidth() // 2 - 192
        h = win_set.winfo_screenheight() // 2 - 115
        win_set.geometry(f'384x230+{w}+{h}')
        win_set.resizable(False, False)

        entry = ttk.Entry(win_set, justify='c'); entry.grid(row=0, column=0, columnspan=4, sticky=ew)
        entry.bind('<KeyRelease>', lambda event: number_validate())
        entry.bind('<Return>', lambda eventr: start_exchange())
        entry.focus()

        ttk.Button(win_set, text='1', command=lambda: [number('1'), entry.focus()]).grid(row=1, column=0)
        ttk.Button(win_set, text='2', command=lambda: [number('2'), entry.focus()]).grid(row=1, column=1)
        ttk.Button(win_set, text='3', command=lambda: [number('3'), entry.focus()]).grid(row=1, column=2)
        ttk.Button(win_set, text='4', command=lambda: [number('4'), entry.focus()]).grid(row=2, column=0)
        ttk.Button(win_set, text='5', command=lambda: [number('5'), entry.focus()]).grid(row=2, column=1)
        ttk.Button(win_set, text='6', command=lambda: [number('6'), entry.focus()]).grid(row=2, column=2)
        ttk.Button(win_set, text='7', command=lambda: [number('7'), entry.focus()]).grid(row=3, column=0)
        ttk.Button(win_set, text='8', command=lambda: [number('8'), entry.focus()]).grid(row=3, column=1)
        ttk.Button(win_set, text='9', command=lambda: [number('9'), entry.focus()]).grid(row=3, column=2)
        ttk.Button(win_set, text='0', command=lambda: [number('0'), entry.focus()]).grid(row=4, column=0, columnspan=2, sticky='ew')
        ttk.Button(win_set, text='.', command=lambda: [number('.'), number_validate(), entry.focus()]).grid(row=4, column=2)
        ttk.Button(win_set, text='+', command=lambda: [calc_operation('+'), entry.focus()]).grid(row=1, column=3)
        ttk.Button(win_set, text='-', command=lambda: [calc_operation('-'), entry.focus()]).grid(row=2, column=3)
        ttk.Button(win_set, text='*', command=lambda: [calc_operation('*'), entry.focus()]).grid(row=3, column=3)
        ttk.Button(win_set, text='/', command=lambda: [calc_operation('/'), entry.focus()]).grid(row=4, column=3)
        ttk.Button(win_set, text='C', command=lambda: [entry.delete(0, END), entry.focus()]).grid(row=5, column=0)
        ttk.Button(win_set, text='AC', command=lambda: [calc_clear(), entry.focus()]).grid(row=5, column=1)
        ttk.Button(win_set, text='=', command=lambda: [calc(), entry.focus()]).grid(row=5, column=2, columnspan=2, sticky='ew')
      
        ttk.Button(win_set, text='КОНВЕРТИРОВАТЬ',
                   command=start_exchange).grid(row=6, column=0, columnspan=4, sticky='ew')
        
        Button(win_set, text='О КАЛЬКУЛЯТОРЕ',relief=FLAT, width=31, font='Arial 8',
                    command=calc_about).grid(row=7, column=1, columnspan=2, sticky='ew', pady=5)
    else:
        mb.showwarning('Внимание!', 'Выберите код базовой валюты\nи коды одной или двух целевых валют!')

# Объявляем функции для проверки корректности заполнения поля ввода суммы для обмена.
def number(num):
    entry.insert(END, num)


def number_validate():
    entry_number = entry.get()
    smb = .join(i for i in entry_number if i in '1234567890.,')
    if smb.find(','):
        smb = smb.replace(',', '.')
    if smb.count('.') > 1:
        smb = smb[:-1]
    if smb.startswith('.'):
        smb = '0' + smb[0:]
    if smb.startswith(','):
        smb = '0.' + smb[1:]
    if entry_number != smb:
        entry.delete(0, END)
        entry.insert(0, smb)

# Объявляем функции для работы с калькулятором.
def calc():
    if first_num:
        if first_num != '':
            try:
                second_num = float(entry.get())
                if operation == '+':
                    result_num = first_num + second_num
                elif operation == '-':
                    result_num = first_num - second_num
                elif operation == '*':
                    result_num = first_num * second_num
                elif operation == '/':
                    try:
                        result_num = first_num / second_num
                    except Exception:
                        mb.showerror('Ошибка!', 'Деление на ноль!')
                entry.delete(0, END)
                entry.insert(0, str(result_num))
            except Exception:
                mb.showerror('Ошибка!', 'Введите число для совершения операции!')


def calc_operation(op):
    global first_num, operation
    try:
        first_num = float(entry.get())
        operation = op
        entry.delete(0, END)
    except Exception:
        mb.showerror('Ошибка!', 'Поле ввода не может быть пустым!')

def calc_clear():
    global first_num, operation
    operation = ''
    first_num = ''
    entry.delete(0, END)
    entry.focus()


def calc_about():
    mb.showinfo('Информация!', '''Для корректной работы:
после выполнения '+', '-', '*', '/'
и последующего ввода числа
необходимо выполнять '=' ''')

# Объявляем функции для работы с историей обменов и отрисовки интерфейса дополнительного окна.
def history():
    global win_his, exchange_history
    win_his = Toplevel()
    win_his.title('История операций')
    w = win_his.winfo_screenwidth() // 2 - 406
    h = win_his.winfo_screenheight() // 2 - 200
    win_his.geometry(f'812x400+{w}+{h}')
    win_his.resizable(False, False)

    exchange_var = StringVar(value=exchange_history)
    txt_his = Listbox(win_his, listvariable=exchange_var, width=90, height=20); txt_his.grid(row=0, column=0)

    ttk.Button(win_his, text='ОЧИСТИТЬ',
               command=lambda: [exchange_history.clear(), win_his.destroy()]).grid(row=1, column=0, sticky='ew')
    
    ttk.Button(win_his, text='СОХРАНИТЬ',
               command=history_save).grid(row=2, column=0, sticky='ew')


def history_save():
    file = fd.asksaveasfile(filetypes=[('TXT Files', '*.txt')], defaultextension='.txt')
    if file != None:
        file.write(f'\n'.join(exchange_history))
    win_his.focus()

# Объявляем сервисную функцию очистки всех данных интерфейса основного окна.
def clear():
    global b_code, t1_code, t2_code, coef
    b_code, t1_code, t2_code, coef = '', '', '', 0
    b_combo.set('')
    b_label['text'] = ''
    b_info['text'] = ''
    t1_combo.set('')
    t1_label['text'] = ''
    t1_info['text'] = ''
    t2_combo.set('')
    t2_label['text'] = ''
    t2_info['text'] = ''

# Выполняем отрисовку интерфейса главного окна.
window = Tk()
window.title('ExChange Master')
w = window.winfo_screenwidth() // 2 - 200
h = window.winfo_screenheight() // 2 - 100
window.geometry(f'400x200+{w}+{h}')
window.resizable(False, False)
window.columnconfigure(index=2, weight=1)

Label(text='Выберите базовую валюту для продажи:', bg='gray', fg='white', font='Arial 14 bold', anchor='w').grid(row=0, column=0, columnspan=3, sticky='ew')

b_combo = ttk.Combobox(width=3, values=list(vlt.keys()), state='readonly'); b_combo.grid(row=1, column=0)
b_combo.bind('<<ComboboxSelected>>', update_b)
b_label = ttk.Label(anchor='w'); b_label.grid(row=1, column=1, padx=5, sticky='w')
b_info = Label(font='Arial 14 bold', justify='right'); b_info.grid(row=1, column=2, sticky='e')

Label(text='Выберите целевую валюту для покупки:', bg='gray', fg='white', font='Arial 14 bold', anchor='w').grid(row=2, column=0, columnspan=3, sticky='ew')

t1_combo = ttk.Combobox(width=3, values=list(vlt.keys()), state='readonly'); t1_combo.grid(row=3, column=0)
t1_combo.bind('<<ComboboxSelected>>', update_t1)
t1_label = ttk.Label(anchor='w'); t1_label.grid(row=3, column=1, padx=5, sticky='ew')
t1_info = Label(font='Arial 14 bold', justify='right'); t1_info.grid(row=3, column=2, sticky='e')

t2_combo = ttk.Combobox(width=3, values=list(vlt.keys()), state='readonly'); t2_combo.grid(row=4, column=0)
t2_combo.bind('<<ComboboxSelected>>', update_t2)
t2_label = ttk.Label(anchor='w'); t2_label.grid(row=4, column=1, padx=5, sticky='ew')
t2_info = Label(font='Arial 14 bold', justify='right'); t2_info.grid(row=4, column=2, sticky='e')

ttk.Button(text='РАСЧЕТ', command=set_exchange).grid(row=5, column=0, columnspan=3, sticky='ew')

ttk.Button(text='ИСТОРИЯ', command=history).grid(row=6, column=0, columnspan=3, sticky='ew')

ttk.Button(text='ОЧИСТИТЬ', command=clear).grid(row=7, column=0, columnspan=3, sticky='ew')
 
window.mainloop()
