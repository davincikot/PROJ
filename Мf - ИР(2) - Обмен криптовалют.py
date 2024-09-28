from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from datetime import datetime as dt
import requests

# Инициализируем переменные и рабочие словари крипто- и фиатных валют.
crypto_dict = {
    'tron' : 'TRX (Tron)',
    'bitcoin': 'BTC (Bitcoin)',
    'ethereum': 'ETH (Ethereum)'
}
currency_dict = {
    'rub': 'RUB (Рубль)',
    'usd': 'USD (Доллар)',
    'eur': 'EUR (Евро)'
}
first_num, second_num, result_num, coef, operation = 0, 0, 0, 0, ''
exchange_history = []


# Объявляем функции обновления меток и запуска главной функции конвертации 'на лету'.
def update_crypto(event):
    crypto_label.config(text=crypto_dict[crypto_combo.get()])
    exchange()


def update_target(event):
    if target_combo.get() in crypto_dict:
        target_label.config(text=crypto_dict[target_combo.get()])
    elif target_combo.get() in currency_dict:
        target_label.config(text=currency_dict[target_combo.get()])
    exchange()


# Объявляем главную функцию конвертации.
def exchange():
    crypto_code, target_code = crypto_combo.get(), target_combo.get()
    if coef != 0 and crypto_code != '' and target_code != '':
        try:
            # Выполняем попытку прямой конвертации.
            response = requests.get(
                f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_code}&vs_currencies={target_code}')
            response.raise_for_status()
            price = response.json().get(crypto_code, {}).get(target_code, 0)
            # Если прямой курс не найден, используем конвертацию через USD.
            if not price:
                response_usd = requests.get(
                    f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_code}&vs_currencies=usd')
                response_usd.raise_for_status()
                price_usd = response_usd.json().get(crypto_code, {}).get('usd', 0)

                response_target = requests.get(
                    f'https://api.coingecko.com/api/v3/simple/price?ids={target_code}&vs_currencies=usd')
                response_target.raise_for_status()
                target_usd = response_target.json().get(target_code, {}).get('usd', 0)

                if price_usd and target_usd:
                    price = price_usd / target_usd
            # Обновляем метки и историю.
            if price:
                result = coef * price
                if target_code in crypto_dict:
                    target_info.config(text=f'{result:.8f}')
                    exchange_history.append(
                        f"{dt.now().strftime('%d.%m.%Y %H:%M:%S')} обмен {coef:.8f} {crypto_code.upper()} на {result:.8f} {target_code.upper()}")
                else:
                    target_info.config(text=f'{result:.2f}')
                    exchange_history.append(
                        f"{dt.now().strftime('%d.%m.%Y %H:%M:%S')} обмен {coef:.8f} {crypto_code.upper()} на {result:.2f} {target_code.upper()}")
        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка: {e}')


# Объявляем функцию отправки суммы обмена на конвертацию.
def start_exchange():
    global coef
    try:
        crypto_info.config(text=f'{float(entry.get()):.8f}')
        coef = float(entry.get())
        win_set.destroy()
        exchange()
    except Exception:
        mb.showerror('Ошибка!', 'Поле ввода не может быть пустым!')
        entry.focus()


# Объявляем функцию для ввода (получения) суммы обмена и отрисовки дополнительного окна с калькулятором.
def set_exchange():
    global entry, win_set, crypto_code, target_code
    crypto_code, target_code = crypto_combo.get(), target_combo.get()
    if crypto_code and target_code:
        win_set = Toplevel()
        win_set.title('Введите сумму для обмена')
        w = win_set.winfo_screenwidth() // 2 - 192
        h = win_set.winfo_screenheight() // 2 - 115
        win_set.geometry(f'384x230+{w}+{h}')
        win_set.resizable(False, False)

        entry = ttk.Entry(win_set, justify='c')
        entry.grid(row=0, column=0, columnspan=4, sticky='ew')
        entry.bind('<KeyRelease>', lambda event: number_validate())
        entry.bind('<Return>', lambda eventr: start_exchange())
        entry.focus()

        ttk.Button(win_set, text='1',
                   command=lambda: [number('1'), entry.focus()]).grid(row=1, column=0)
        ttk.Button(win_set, text='2',
                   command=lambda: [number('2'), entry.focus()]).grid(row=1, column=1)
        ttk.Button(win_set, text='3',
                   command=lambda: [number('3'), entry.focus()]).grid(row=1, column=2)
        ttk.Button(win_set, text='4',
                   command=lambda: [number('4'), entry.focus()]).grid(row=2, column=0)
        ttk.Button(win_set, text='5',
                   command=lambda: [number('5'), entry.focus()]).grid(row=2, column=1)
        ttk.Button(win_set, text='6',
                   command=lambda: [number('6'), entry.focus()]).grid(row=2, column=2)
        ttk.Button(win_set, text='7',
                   command=lambda: [number('7'), entry.focus()]).grid(row=3, column=0)
        ttk.Button(win_set, text='8',
                   command=lambda: [number('8'), entry.focus()]).grid(row=3, column=1)
        ttk.Button(win_set, text='9',
                   command=lambda: [number('9'), entry.focus()]).grid(row=3, column=2)
        ttk.Button(win_set, text='0',
                   command=lambda: [number('0'), entry.focus()]).grid(row=4, column=0, columnspan=2, sticky='ew')
        ttk.Button(win_set, text='.',
                   command=lambda: [number('.'), number_validate(), entry.focus()]).grid(row=4, column=2)
        ttk.Button(win_set, text='+',
                   command=lambda: [calc_operation('+'), entry.focus()]).grid(row=1, column=3)
        ttk.Button(win_set, text='-',
                   command=lambda: [calc_operation('-'), entry.focus()]).grid(row=2, column=3)
        ttk.Button(win_set, text='*',
                   command=lambda: [calc_operation('*'), entry.focus()]).grid(row=3, column=3)
        ttk.Button(win_set, text='/',
                   command=lambda: [calc_operation('/'), entry.focus()]).grid(row=4, column=3)
        ttk.Button(win_set, text='C',
                   command=lambda: [entry.delete(0, END), entry.focus()]).grid(row=5, column=0)
        ttk.Button(win_set, text='AC',
                   command=lambda: [calc_clear(), entry.focus()]).grid(row=5, column=1)
        ttk.Button(win_set, text='=',
                   command=lambda: [calc(), entry.focus()]).grid(row=5, column=2, columnspan=2, sticky='ew')

        ttk.Button(win_set, text='КОНВЕРТИРОВАТЬ',
                   command=start_exchange).grid(row=6, column=0, columnspan=4, sticky='ew')

        Button(win_set, text='О КАЛЬКУЛЯТОРЕ', relief=FLAT, width=31, font='Arial 8',
               command=calc_about).grid(row=7, column=1, columnspan=2, sticky='ew', pady=5)
    else:
        mb.showwarning('Внимание!', 'Выберите все значения!')


# Объявляем функции для проверки корректности заполнения поля ввода суммы обмена для конвертации.
def number(num):
    entry.insert(END, num)


def number_validate():
    entry_number = entry.get()
    smb = "".join(i for i in entry_number if i in '1234567890.,')
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
    mb.showinfo('Логика работы',
'''После выполнения '+', '-', '*', '/'
и последующего ввода числа
необходимо выполнять '='

'C' - сброс числа
'AC' - сброс калькулятора''')
    entry.focus()


# Объявляем функции для работы с историей обменов и отрисовки интерфейса дополнительного окна.
def history():
    global win_his, exchange_history
    win_his = Toplevel()
    win_his.title('История обменов')
    w = win_his.winfo_screenwidth() // 2 - 294
    h = win_his.winfo_screenheight() // 2 - 200
    win_his.geometry(f'588x400+{w}+{h}')
    win_his.resizable(False, False)

    exchange_var = StringVar(value=exchange_history)
    txt_his = Listbox(win_his, listvariable=exchange_var, width=65, height=20)
    txt_his.grid(row=0, column=0)

    ttk.Button(win_his, text='ОЧИСТИТЬ',
               command=lambda: [exchange_history.clear(), win_his.destroy()]).grid(row=1, column=0, sticky='ew')

    ttk.Button(win_his, text='СОХРАНИТЬ',
               command=history_save).grid(row=2, column=0, sticky='ew')


def history_save():
    file = fd.asksaveasfile(filetypes=[('TXT Files', '*.txt')], defaultextension='.txt')
    if file is not None:
        file.write('\n'.join(exchange_history))
    win_his.focus()


# Объявляем сервисную функцию очистки всех данных и интерфейса главного окна.
def clear():
    global crypto_code, target_code, coef
    crypto_code, target_code, coef = '', '', 0
    crypto_combo.set('')
    crypto_label['text'] = ''
    crypto_info['text'] = ''
    target_combo.set('')
    target_label['text'] = ''
    target_info['text'] = ''


# Выполняем отрисовку интерфейса главного окна.
window = Tk()
window.title('Crypto Exchange Master')
w = window.winfo_screenwidth() // 2 - 200
h = window.winfo_screenheight() // 2 - 90
window.geometry(f'400x180+{w}+{h}')
window.resizable(True, True)
window.columnconfigure(index=2, weight=1)

Label(text='Выберите криптовалюту для продажи:',
      bg='gray', fg='white', font='Arial 14 bold', anchor='w').grid(row=0, column=0, columnspan=3, sticky='ew')

crypto_combo = ttk.Combobox(width=7, values=list(crypto_dict.keys()), state='readonly')
crypto_combo.grid(row=1, column=0)
crypto_combo.bind('<<ComboboxSelected>>', update_crypto)
crypto_label = ttk.Label(anchor='w')
crypto_label.grid(row=1, column=1, padx=5, sticky='w')
crypto_info = Label(font='Arial 14 bold', justify='right')
crypto_info.grid(row=1, column=2, sticky='e')

Label(text='Выберите валюту для покупки:',
      bg='gray', fg='white', font='Arial 14 bold', anchor='w').grid(row=2, column=0, columnspan=3, sticky='ew')

target_combo = ttk.Combobox(width=7, values=list(currency_dict.keys()) + list(crypto_dict.keys()), state='readonly')
target_combo.grid(row=3, column=0)
target_combo.bind('<<ComboboxSelected>>', update_target)
target_label = ttk.Label(anchor='w')
target_label.grid(row=3, column=1, padx=5, sticky='ew')
target_info = Label(font='Arial 14 bold', justify='right')
target_info.grid(row=3, column=2, sticky='e')

ttk.Button(text='РАСЧЕТ',
           command=set_exchange).grid(row=4, column=0, columnspan=3, sticky='ew')

ttk.Button(text='ИСТОРИЯ',
           command=history).grid(row=5, column=0, columnspan=3, sticky='ew')

ttk.Button(text='ОЧИСТИТЬ',
           command=clear).grid(row=6, column=0, columnspan=3, sticky='ew')

window.mainloop()
