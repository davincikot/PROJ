from tkinter import *
from tkinter import messagebox as mb
from datetime import datetime as dt

# Создаем рабочие функции для обработки заявок.
def book_seat(event=None):
    try:
        seat_name = seat.get().upper()
        if seats[seat_name] == 'свободно':
            seats[seat_name] = 'забронировано'
            lbl_rez['text'] = f"Вы забронировали место '{seat_name}'."
            lbl_rez['bg'] = 'green'
            lbl_rez['text'] = f"Вы забронировали место '{seat_name}'."
            seats_history.insert(0, f"Место '{seat_name}' забронировано {dt.now().strftime('%d.%m.%Y')} в {dt.now().strftime('%H:%M:%S')}.")
            if len(seats_history) > 20:
                seats_history.pop()
            lbl_inf['text'] = f"Количество свободных мест: {list(seats.values()).count('свободно')}."
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
        seat_name = seat.get().upper()
        if seats[seat_name] == 'забронировано':
            seats[seat_name] = 'свободно'
            lbl_rez['text'] = f"Вы отменили бронь на место '{seat_name}'."
            lbl_rez['bg'] = 'green'
            seats_history.insert(0, f"Бронь на место '{seat_name}' анулирована {dt.now().strftime('%d.%m.%Y')} в {dt.now().strftime('%H:%M:%S')}.")
            if len(seats_history) > 20:
                seats_history.pop()
            lbl_inf['text'] = f"Количество свободных мест: {list(seats.values()).count('свободно')}."
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
        if i < 10:
            x = i * 40 + 20
            y = 20
            color = 'green' if stat == 'свободно' else 'red'
            canvas.create_rectangle(x+5, y, x+35, y+30, fill=color)
            canvas.create_text(x+21, y+15, text=seat, font='Arial 15 bold', fill='white')
        if i >= 10:
            x = (i - 10) * 40 + 20
            y = 60
            color = 'green' if stat == 'свободно' else 'red'
            canvas.create_rectangle(x+5, y, x+35, y+30, fill=color)
            canvas.create_text(x+21, y+15, text=seat, font='Arial 15 bold', fill='white')   
    canvas.create_rectangle(25, 100, 415, 130, fill="green")
    canvas.create_text(220, 115, text='Свободные места подсвечены зеленым цветом.', font='Arial 14', fill='white')
    canvas.create_rectangle(25, 140, 415, 170, fill="red")
    canvas.create_text(220, 155, text='Занятые места подсвечены красным цветом.', font='Arial 14', fill='white')

# Создаем сервисные функции для ичезающих подсказок по событиям в полях ввода данных.
def ent_enter(event):
    if event.widget == seat and seat.get() == 'введите номер места':
        seat.delete(0, END)
        seat.config(fg='black')
        btn_rez['state'] = NORMAL
        btn_rez['fg'] = 'green'
        btn_del['state'] = NORMAL
        btn_del['fg'] = 'red'

def ent_leave(event):
    if event.widget == seat and seat.get() == '':
        seat.insert(0, 'введите номер места')
        seat.config(fg='gray')
        btn_rez['state'] = DISABLED
        btn_del['state'] = DISABLED
        lbl_inf.focus_set()

# Создаем сервисную функцию для истории заявок.
def history():
    global lbl_his
    win = Toplevel()
    win.title('История бронирования')
    win.geometry(f'440x480+{w}+{h}')
    win.resizable(False, False)
    lbl_his = Label(win, text=f'{'\n'.join(seats_history)}', width=54, height=28, justify='center', font='Arial 14', bg='gray', fg='white')
    lbl_his.pack()
    Button(win, text='ОЧИСТИТЬ ИСТОРИЮ', width=68, font='Arial 10 bold', command=history_clear).pack()

def history_clear():
    seats_history.clear()
    lbl_his.config(text = "")

# Создааем сервисные функции для очистки поля ввода данных и информационного поля.
def clear_events():
    seat.delete(0, END)
    seat.insert(0, 'введите номер места')
    seat.config(fg='gray')
    btn_rez['state'] = DISABLED
    btn_del['state'] = DISABLED
    lbl_rez['text'] = 'Здесь отобразится статус вашей брони.'
    lbl_rez['text'] = 'Здесь отобразится статус вашей брони.'
    lbl_rez['bg'] = 'gray'
    lbl_inf['text'] = 'Здесь отобразится количество свободных мест.'
    lbl_inf.focus_set()

def clear_reservations():
    seats.update({f'Б{i}': 'свободно' for i in range(1, 21)})
    clear_events()
    update_canvas()

# Создаем рабочий словарь мест для бронирования и пустой список свободных мест.
seats = {f'Б{i}': 'свободно' for i in range(1, 21)}
seats_history = []

# Создаем и центрируем главное окно приложения.
window = Tk()
window.title('Бронировние мест v.1.2')
w = window.winfo_screenwidth() // 2 - 220
h = window.winfo_screenheight() // 2 - 150
window.geometry(f'440x480+{w}+{h}')
window.resizable(False, False)

# Создаем: холст для отрисовки ячеек с бронями; поля для ввода данных; кнопки; информационную метку.
canvas = Canvas(width=450, height=180)
canvas.pack()

seat = Entry(width=24, justify='center', font='Arial 14')
seat.config(fg='gray')
seat.insert(0, 'введите номер места')
seat.bind('<FocusIn>', ent_enter)
seat.bind('<FocusOut>', ent_leave)
seat.bind('<Return>', book_seat)
seat.pack()

btn_rez = Button(text='ЗАБРОНИРОВАТЬ', width=15, font='Arial 18 bold', state=DISABLED, command=book_seat)
btn_rez.pack(ipady=4, pady=5)

btn_del = Button(text='ОТМЕНИТЬ БРОНЬ', width=15, font='Arial 18 bold', state=DISABLED, command=del_seat)
btn_del.pack(ipady=4, pady=5)

lbl_rez = Label(text='Здесь отобразится статус вашей брони.', width=45, justify='center', font='Arial 14', bg='gray', fg='white')
lbl_rez.pack(ipady=5, pady=5)

lbl_inf = Label(text='Здесь отобразится количество свободных мест.', width=45, justify='center', font='Arial 14', bg='gray', fg='white')
lbl_inf.pack(ipady=5, pady=5)
lbl_inf.focus_set()

Button(text='ОЧИСТИТЬ ПОЛЕ ВВОДА', width=56, font='Arial 10 bold', command=clear_events).pack()

Button(text='ОТМЕНИТЬ ВСЕ БРОНИ', width=56, font='Arial 10 bold', command=clear_reservations).pack()

Button(text='ИСТОРИЯ БРОНИРОВАНИЯ', width=56, font='Arial 10 bold', command=history).pack()

update_canvas()

window.mainloop()
