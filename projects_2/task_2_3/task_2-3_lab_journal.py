researcher = input("Введите ФИО исследователя: ")
date = input("Введите дату: ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

line = "+" + "-" * 50 + "+"

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(line + "\n")
    file.write(f"| {'Электронный лабораторный журнал':<48} |\n")
    file.write(line + "\n")
    file.write(f"| {'ФИО исследователя':<17}: {researcher:<28} |\n")
    file.write(f"| {'Дата':<17}: {date:<28} |\n")
    file.write(f"| {'Эксперимент':<17}: {experiment:<28} |\n")
    file.write(line + "\n")
    file.write(f"| {'Вывод:':<48} |\n")
    for word_line in conclusion.split("\n"):
        file.write(f"| {word_line:<48} |\n")
    file.write(line + "\n")

print("Журнал сохранён в journal.txt")
