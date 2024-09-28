from tkinter import *
from tkinter import messagebox as mb

# Создаем рабочие функции для обработки заявок.
def book_seat(event=None):
    try:
        seat_name = seat_rez.get().upper()
        if seats[seat_name] == 'свободно':
            seats[seat_name] = 'забронировано'
            lbl_rez['text'] = f"Вы забронировали место '{seat_name}'."
            lbl_rez['bg'] = 'green'
            update_canvas()
        else:
            lbl_rez['text'] = f"Место '{seat_name}' уже забронировано."
            lbl_rez['bg'] = 'red'
    except KeyError:
        mb.showerror('Ошибка!', 'Место для бронирования не существует или не указано.')
    except Exception as e:
        mb.showerror('Ошибка!', f"Непредвиденная ошибка '{e}'!")

def del_seat(event=None):
    try:
        seat_name = seat_del.get().upper()
        if seats[seat_name] == 'забронировано':
            seats[seat_name] = 'свободно'
            lbl_rez['text'] = f"Вы отменили бронь на место '{seat_name}'."
            lbl_rez['bg'] = 'green'
            update_canvas()  
        else:
            lbl_rez['text'] = f"Место '{seat_name}' еще не забронировано."
            lbl_rez['bg'] = 'green'
    except KeyError:
        mb.showerror('Ошибка!', 'Место для отмены брони не существует или не указано.')
    except Exception as e:
        mb.showerror('Ошибка!', f"Непредвиденная ошибка '{e}'!")

# Создаем сервисную функцию для отрисовки графического фрейма статуса заявок.
def update_canvas():
    canvas.delete('all')
    for i, (seat, stat) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = 'green' if stat == 'свободно' else 'red'
        canvas.create_rectangle(x+5, y, x+35, y+30, fill=color)
        canvas.create_text(x+20, y+15, text=seat, font='Arial 18 bold', fill='white')
    canvas.create_rectangle(25, 100, 375, 60, fill="green")
    canvas.create_text(200, 80, text='Свободные места подсвечены зеленым цветом.', font='Arial 14', fill='white')
    canvas.create_rectangle(25, 150, 375, 110, fill="red")
    canvas.create_text(200, 130, text='Занятые места подсвечены красным цветом.', font='Arial 14', fill='white')

# Создаем сервисные функции для ичезающих подсказок по событиям в полях ввода данных.
def ent_enter(event):
    if event.widget == seat_rez and seat_rez.get() == 'введите номер места для бронирования':
        seat_rez.delete(0, END)
        seat_rez.config(fg='black')
        btn_rez['state'] = NORMAL
        btn_rez['fg'] = 'green'
    if event.widget == seat_del and seat_del.get() == 'введите номер места для отмены брони':
        seat_del.delete(0, END)
        seat_del.config(fg='black')
        btn_del['state'] = NORMAL
        btn_del['fg'] = 'red'

def ent_leave(event):
    if event.widget == seat_rez and seat_rez.get() == '':
        seat_rez.insert(0, 'введите номер места для бронирования')
        seat_rez.config(fg='gray')
        btn_rez['state'] = DISABLED
        lbl_rez.focus_set()
    if event.widget == seat_del and seat_del.get() == '':
        seat_del.insert(0, 'введите номер места для отмены брони')
        seat_del.config(fg='gray')
        btn_del['state'] = DISABLED
        lbl_rez.focus_set()

# Создааем сервисные функции для очистки полей ввода данных и информационного поля.
def clear_events():
    seat_rez.delete(0, END)
    seat_rez.insert(0, 'введите номер места для бронирования')
    seat_rez.config(fg='gray')
    seat_del.delete(0, END)
    seat_del.insert(0, 'введите номер места для отмены брони')
    seat_del.config(fg='gray')
    btn_rez['state'] = DISABLED
    btn_del['state'] = DISABLED
    lbl_rez['text'] = 'Здесь отобразится статус вашей брони.'
    lbl_rez['bg'] = 'gray'
    lbl_rez.focus_set()

def clear_reservations():
    seats.update({f'Б{i}': 'свободно' for i in range(1, 10)})
    clear_events()
    update_canvas()

# Создаем рабочий словарь - список мест для бронирования.
seats = {f'Б{i}': 'свободно' for i in range(1, 10)}

# Создаем и центрируем главное окно приложения.
window = Tk()
window.title('Бронировние мест v.1.1')
w = window.winfo_screenwidth() // 2 - 200
h = window.winfo_screenheight() // 2 - 150
window.geometry(f'400x430+{w}+{h}')
window.resizable(False, False)

# Создаем: холст для отрисовки ячеек с бронями; поля для ввода данных; кнопки; информационную метку.
canvas = Canvas(width=400, height=150)
canvas.pack()

seat_rez = Entry(width=35, justify='center', font='Arial 14')
seat_rez.config(fg='gray')
seat_rez.insert(0, 'введите номер места для бронирования')
seat_rez.bind('<FocusIn>', ent_enter)
seat_rez.bind('<FocusOut>', ent_leave)
seat_rez.bind('<Return>',book_seat)
seat_rez.pack()

btn_rez = Button(text='ЗАБРОНИРОВАТЬ', width=15, font='Arial 18 bold', state=DISABLED, command=book_seat)
btn_rez.pack(ipady=4, pady=5)

seat_del = Entry(width=35, justify='center', font='Arial 14')
seat_del.config(fg='gray')
seat_del.insert(0, 'введите номер места для отмены брони')
seat_del.bind('<FocusIn>', ent_enter)
seat_del.bind('<FocusOut>', ent_leave)
seat_del.bind('<Return>',del_seat)
seat_del.pack()

btn_del = Button(text='ОТМЕНИТЬ БРОНЬ', width=15, font='Arial 18 bold', state=DISABLED, command=del_seat)
btn_del.pack(ipady=4, pady=5)

lbl_rez = Label(text='Здесь отобразится статус вашей брони.', width=45, justify='center', font='Arial 14', bg='gray', fg='white')
lbl_rez.pack(ipady=10, pady=10)
lbl_rez.focus_set()

Button(text='ОЧИСТИТЬ ПОЛЯ ВВОДА ДАННЫХ', width=56, font='Arial 10 bold', command=clear_events).pack()

Button(text='ОТМЕНИТЬ ВСЕ БРОНИ', width=56, font='Arial 10 bold', command=clear_reservations).pack()

update_canvas()

window.mainloop()
