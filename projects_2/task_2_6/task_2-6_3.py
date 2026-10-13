donor = input("Введите группу крови донора: ").upper()
recipient = input("Введите группу крови пациента: ").upper()

if donor == "O" or donor == recipient:
    print("Переливание возможно")
elif donor != "O" and donor != recipient:
    print("Переливание невозможно")
else:
    print("Некорректные данные")
