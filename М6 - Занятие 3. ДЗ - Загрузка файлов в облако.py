import json, os, requests, pyperclip
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb 
 
history_file = 'history.json'
 
 
def file_upload():
    global download_link
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files=files)
                response.raise_for_status()
                download_link = response.json().get('link')
                if download_link:
                    lbl_url['text'] = str(download_link)
                    history_save(filepath, download_link)
                else:
                    raise ValueError('Не удалось получить ссылку для скачивания!')
    except requests.RequestException as ne:
        mb.showerror('Ошибка!', f'Произошла ошибка: {ne}!')
    except ValueError as ve:
        mb.showerror('Ошибка!', f'Произошла ошибка: {str(ve)}!')
    except Exception as ex:
        mb.showerror('Ошибка!', f'Произошла ошибка: {ex}!')
 

def history_save(file_path, download_link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as file:
            history = json.load(file)
    
    history.append({'file_path': os.path.basename(file_path), 'download_link': download_link})
    
    with open(history_file, 'w') as file:
        json.dump(history, file, indent=4)


def history_show():
    global win_history, lst_history
    if not os.path.exists(history_file):
        mb.showwarning('Предупреждение!', 'История загрузок пуста!')
        return

    win_history = Toplevel(window)
    win_history.title('История загрузок')
    w = win_history.winfo_screenwidth() // 2 - 258
    h = win_history.winfo_screenheight() // 2 - 110
    win_history.geometry(f'516x220+{w}+{h}')
    win_history.resizable(False, False)
    
    lst_history = Listbox(win_history, width=55, height=10)
    lst_history.grid(row=0, column=0, padx=(10, 0), pady=10)
    
    btn_clear = ttk.Button(win_history, text='ОЧИСТИТЬ ИСТОРИЮ', command=history_clear)
    btn_clear.grid(row=1, column=0, padx=(10, 0), sticky='ew')

    with open(history_file, 'r') as file:
        history = json.load(file)
        for item in history:
            lst_history.insert(END, f"Файл '{item['file_path']}' загружен по адресу '{item['download_link']}'")


def history_clear():
    global lst_history
    lst_history.delete(0, END)
    os.remove(history_file)
    win_history.withdraw()


def copy_clipboard():
    try:
        if download_link:
            if download_link != '':
                pyperclip.copy(download_link)
                mb.showinfo('Успех!', 'Ссылка скопирована в буфер обмена!')
        else:
            mb.showerror('Ошибка!', 'Отсутвует ссылка для копирования!')
    except:
        mb.showerror('Ошибка!', 'Отсутвует ссылка для копирования!')


def clear():
    global download_link
    download_link = ''
    lbl_url['text'] = ''


window = Tk()
window.title('Files Cloud')
w = window.winfo_screenwidth() // 2 - 95
h = window.winfo_screenheight() // 2 - 53
window.geometry(f'190x132+{w}+{h}')
window.resizable(False, False)
 
lbl_url = Label(window, width=20, bg='gray', fg='white', font='Arial 12 bold', justify='right')
lbl_url.grid(row=0, column=0, sticky='ew')

btn_upload = ttk.Button(window, text='ЗАГРУЗИТЬ',
                        command=file_upload)
btn_upload.grid(row=1, column=0, sticky='ew')

btn_history = ttk.Button(window, text='ПОКАЗАТЬ ИСТОРИЮ',
                         command=history_show)
btn_history.grid(row=2, column=0, sticky='ew')

btn_clipboard = ttk.Button(window, text='КОПИРОВАТЬ В БУФЕР',
                           command=copy_clipboard)
btn_clipboard.grid(row=3, column=0, sticky='ew')

btn_clipboard = ttk.Button(window, text='ОЧИСТИТЬ',
                           command=clear)
btn_clipboard.grid(row=4, column=0, sticky='ew')


window.mainloop()
