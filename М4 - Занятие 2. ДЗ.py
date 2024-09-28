from tkinter import *
from tkinter import messagebox as mb

# Создаем функции для ичезающих подсказок по событиям в полях Entry.
def ent_enter(event):
    if event.widget == ent_num1 and ent_num1.get() == 'введите число':
        ent_num1.delete(0, END)
        ent_num1.config(fg='black')
    if event.widget == ent_num2 and ent_num2.get() == 'введите число':
        ent_num2.delete(0, END)
        ent_num2.config(fg='black')
    if event.widget == ent_num3 and ent_num3.get() == 'введите число':
        ent_num3.delete(0, END)
        ent_num3.config(fg='black')

def ent_leave(event):
    if event.widget == ent_num1 and ent_num1.get() == '':
        ent_num1.insert(0, 'введите число')
        ent_num1.config(fg='gray')
    if event.widget == ent_num2 and ent_num2.get() == '':
        ent_num2.insert(0, 'введите число')
        ent_num2.config(fg='gray')
    if event.widget == ent_num3 and ent_num3.get() == '':
        ent_num3.insert(0, 'введите число')
        ent_num3.config(fg='gray')

# Создаем функции для кнопок и выполняем проверку введенных значений на принадлежность к числам.
def n_int():
    ent_num1.delete(0, END)
    ent_num1.insert(0, 'введите число')
    ent_num1.config(fg='gray')

    ent_num2.delete(0, END)
    ent_num2.insert(0, 'введите число')
    ent_num2.config(fg='gray')

    ent_num3.delete(0, END)
    ent_num3.insert(0, 'введите число')
    ent_num3.config(fg='gray')

    lbl_rez['text'] = ''

    btn_summ['command'] = lambda: calc_int('summ_int')
    btn_mult['command'] = lambda: calc_int('mult_int')
    btn_degr['command'] = lambda: calc_int('degr_int')
    btn_divs['command'] = lambda: calc_int('divs_int')

    lbl_rez.focus_set()

def calc_int(operation):
    nums = [ent_num1.get(), ent_num2.get(), ent_num3.get()]

    for index, num in enumerate(nums):
        try:
            num = int(num)
        except:
            mb.showerror('Ошибка!', f'Ошибка ввода в поле №{index + 1}!')    
        continue

    # Считаем и выводим результат для 'ЦЕЛЫХ'.
    match operation:
        case 'summ_int':
            summa = int(nums[0]) + int(nums[1]) + int(nums[2])
            lbl_rez['text'] = f'{nums[0]} + {nums[1]} + {nums[2]} = {summa}'
        case 'mult_int':
            multiple = int(nums[0]) * int(nums[1]) * int(nums[2])
            lbl_rez['text'] = f'{nums[0]} * {nums[1]} * {nums[2]} = {multiple}'
        case 'degr_int':
            if int(ent_num1.get()) > 9 or int(ent_num2.get()) > 9 or int(ent_num3.get()) > 1:
                return mb.showerror('Ошибка!', 'Cлишком много вычислений!\nПервое поле должно быть < 10\nВторое поле должно быть < 10\nТретье поле должно быть <= 1')
            degrees = int(nums[0]) ** int(nums[1]) ** int(nums[2])
            lbl_rez['text'] = f'{nums[0]} ** {nums[1]} ** {nums[2]} = {degrees}'
        case 'divs_int':
            if int(ent_num2.get()) == 0 or int(ent_num3.get()) == 0:
                return mb.showerror('Ошибка!', 'Вы разгадали знак беконечность!\nНа ноль делить нельзя!')
            division = int(nums[0]) / int(nums[1]) / int(nums[2])
            lbl_rez['text'] = f'{nums[0]} / {nums[1]} / {nums[2]} = {division:.0f}'
        case _:
            lbl_rez['text'] = 'Непредвиденная ошибка!'

def n_float():
    ent_num1.delete(0, END)
    ent_num1.insert(0, 'введите число')
    ent_num1.config(fg='gray')

    ent_num2.delete(0, END)
    ent_num2.insert(0, 'введите число')
    ent_num2.config(fg='gray')

    ent_num3.delete(0, END)
    ent_num3.insert(0, 'введите число')
    ent_num3.config(fg='gray')

    lbl_rez['text'] = ''

    btn_summ['command'] = lambda: calc_float('summ_float')
    btn_mult['command'] = lambda: calc_float('mult_float')
    btn_degr['command'] = lambda: calc_float('degr_float')
    btn_divs['command'] = lambda: calc_float('divs_float')

    lbl_rez.focus_set()

def calc_float(operation):
    nums = [ent_num1.get(), ent_num2.get(), ent_num3.get()]

    for index, num in enumerate(nums):
        try:
            num = float(num)
        except:
            mb.showerror('Ошибка!', f'Ошибка ввода в поле №{index + 1}!')    
        continue

    # Считаем и выводим результат с округлением до десятых долей для 'ДРОБЕЙ'.
    match operation:
        case 'summ_float':
            summa = float(nums[0]) + float(nums[1]) + float(nums[2])
            lbl_rez['text'] = f'{float(nums[0]):.1f} + {float(nums[1]):.1f} + {float(nums[2]):.1f} = {summa:.1f}'
        case 'mult_float':
            multiple = float(nums[0]) * float(nums[1]) * float(nums[2])
            lbl_rez['text'] = f'{float(nums[0]):.1f} * {float(nums[1]):.1f} * {float(nums[2]):.1f} = {multiple:.1f}'
        case 'degr_float':
            if float(ent_num1.get()) > 9 or float(ent_num2.get()) > 9 or float(ent_num3.get()) > 1:
                return mb.showerror('Ошибка!', 'Cлишком много вычислений!\nПервое поле должно быть < 10\nВторое поле должно быть < 10\nТретье поле должно быть <= 1')
            degrees = float(nums[0]) ** float(nums[1]) ** float(nums[2])
            lbl_rez['text'] = f'{float(nums[0]):.1f} ** {float(nums[1]):.1f} ** {float(nums[2]):.1f} = {degrees:.1f}'
        case 'divs_float':
            if float(ent_num2.get()) == 0 or float(ent_num3.get()) == 0:
                return mb.showerror('Ошибка!', 'Вы разгадали знак беконечность!\nНа ноль делить нельзя!')
            division = float(nums[0]) / float(nums[1]) / float(nums[2])
            lbl_rez['text'] = f'{float(nums[0]):.1f} / {float(nums[1]):.1f} / {float(nums[2]):.1f} = {division:.1f}'
        case _:
            lbl_rez['text'] = 'Непредвиденная ошибка!'

def clear():
    ent_num1.delete(0, END)
    ent_num1.insert(0, 'введите число')
    ent_num1.config(fg='gray')

    ent_num2.delete(0, END)
    ent_num2.insert(0, 'введите число')
    ent_num2.config(fg='gray')

    ent_num3.delete(0, END)
    ent_num3.insert(0, 'введите число')
    ent_num3.config(fg='gray')

    lbl_rez['text'] = ''

    lbl_rez.focus_set()

# Создаем и центрируем окно.
window = Tk()
window.title('Калькулятор v.1.3')
w = window.winfo_screenwidth() // 2 - 110
h = window.winfo_screenheight() // 2 - 150
window.geometry(f'220x410+{w}+{h}')
window.resizable(False, False)

# Создаем метки и кнопки.
frm = Frame()
frm.pack()

lbl_manual1 = Label(frm, text='ВЫБЕРИТЕ ТИП ЧИСЕЛ', font='Arial 16 bold', bg='gray', fg='white')
lbl_manual1.pack()

var = IntVar()
var.set(0)
nums_int = Radiobutton(frm, text=' ЦЕЛЫЕ', variable = var, value = 1, command = n_int)
nums_int.pack(side=LEFT, padx=4)
lbl_manual2 = Label(frm, text='< И >', font='Arial 16 bold', bg='gray', fg='white')
lbl_manual2.pack(side=LEFT)
lbl_manual3 = Label(frm, text=' ДРОБИ')
lbl_manual3.pack(side=LEFT)
nums_float = Radiobutton(frm,variable = var, value = 2, command = n_float)
nums_float.pack(side=RIGHT)

lbl_manual4 = Label(text='ЗАПОЛНИТЕ ВСЕ ПОЛЯ', font='Arial 16 bold', bg='gray', fg='white')
lbl_manual4.pack()

ent_num1 = Entry(width=23, justify='center', font='Arial 14')
ent_num1.insert(0, 'введите число')
ent_num1.config(fg='gray')
ent_num1.bind('<FocusIn>', ent_enter)
ent_num1.bind('<FocusOut>', ent_leave)
ent_num1.pack()

ent_num2 = Entry(width=23, justify='center', font='Arial 14')
ent_num2.insert(0, 'введите число')
ent_num2.config(fg='gray')
ent_num2.bind('<FocusIn>', ent_enter)
ent_num2.bind('<FocusOut>', ent_leave)
ent_num2.pack()

ent_num3 = Entry(width=23, justify='center', font='Arial 14')
ent_num3.insert(0, 'введите число')
ent_num3.config(fg='gray')
ent_num3.bind('<FocusIn>', ent_enter)
ent_num3.bind('<FocusOut>', ent_leave)
ent_num3.pack()

btn_summ = Button(text='СУММИРОВАТЬ', width=26, font='Arial 10 bold')
btn_summ.pack(ipady=4)

btn_mult = Button(text='ПЕРЕМНОЖИТЬ', width=26, font='Arial 10 bold')
btn_mult.pack(ipady=4)

btn_degr = Button(text='ВОЗВЕСТИ В СТЕПЕНЬ', width=26, font='Arial 10 bold')
btn_degr.pack(ipady=4)

btn_divs = Button(text='ПОЛЕДОВАТЕЛЬНО РАЗДЕЛИТЬ', width=26, font='Arial 10 bold')
btn_divs.pack(ipady=4)

lbl_rez = Label(text='', width=26, justify='center', font='Arial 12 bold', bg='gray', fg='white')
lbl_rez.pack(ipady=10, pady=20)
lbl_rez.focus_set()

btn_copy = Button(text='КОПИРОВАТЬ РЕЗУЛЬТАТ В БУФЕР', width=26, font='Arial 10', command=lambda: window.clipboard_append(lbl_rez['text'][lbl_rez['text'].index("=")+1:]))
btn_copy.pack()

btn_clear = Button(text='ОЧИСТИТЬ ПОЛЯ ВВОДА ДАННЫХ', width=26, font='Arial 10', command=clear)
btn_clear.pack()

window.mainloop()
