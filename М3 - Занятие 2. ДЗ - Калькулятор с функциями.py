def add(a, b):
    return a + b

def substruct(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка! На ноль делить нельзя."
    else:
        return a/b

print("Выберите операцию: ")
print('1.Сложение')
print('2.Вычитание')
print('3.Умножение')
print('3.Деление')

choice=input("Введите номер операции(1/2/3/4): ")

n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))

if choice == "1":
    print(f"Результат: {n1} + {n2} = {add(n1,n2)}")
elif choice == "2":
    print(f"Результат: {n1} - {n2} = {substruct(n1,n2)}")
elif choice == "3":
    print(f"Результат: {n1} * {n2} = {multiply(n1,n2)}")
elif choice == "4":
    print(f"Результат: {n1} / {n2} = {divide(n1,n2)}")
else:
    print("Вы выбрали неправильную операцию")
