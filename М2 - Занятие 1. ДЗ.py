# 1 вариант.
T = float(input("Введите температуру первого озера: "))
if T <= 0: print("Озеро замерзло")
elif 0 < T < 10: print("Ледяная вода")
elif 10 <= T < 15: print("Жуть как холодно")
elif 15 <= T < 18: print("Прохладно, но можно искупаться")
elif 18 <= T < 24: print("Кайф")
elif 24 <= T < 30: print("Полный кайф")
elif 30 <= T <= 36: print("Горячая")
else: print("Кипяток")

# 2 вариант.
[print("Озеро замерзло" if t <= 0 else "Ледяная вода" if t < 10 else
      "Жуть как холодно" if t < 15 else "Прохладно, но можно искупаться" if t < 18 else
      "Кайф" if t < 24 else "Полный кайф" if t < 30  else "Горячая" if t <= 36 else "Кипяток") for t in [int(input())]]

# 3 вариант.
num = float(input("Введите температуру первого озера: "))
match num:
  case num if num <= 0:
        print("Озеро замерзло")
  case num if num < 10:
        print("Ледяная вода")
  case num if num < 15:
        print("Жуть как холодно")
  case num if num < 18:
        print("Прохладно, но можно искупаться")
  case num if num < 24:
        print("Кайф")
  case num if num < 30:
        print("Полный кайф")
  case num if num < 36:
        print("Горячая")
  case  _:
        print("Кипяток")
