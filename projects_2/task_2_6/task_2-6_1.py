ph = float(input("Введите значение pH: "))

if ph < 0 or ph > 14:
    print("Некорректное значение pH (допустимо от 0 до 14)")
elif ph < 7:
    print("Кислая среда")
elif ph == 7:
    print("Нейтральная среда")
else:
    print("Щелочная среда")
