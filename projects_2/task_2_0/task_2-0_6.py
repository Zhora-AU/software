info = "Фамилия: Тишура\nИмя: Егор\nГруппа: 202.1\nГод поступления: 2025"
file_path = "C:/Users/Егор/output.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(info)

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print("Файл успешно создан! Вот его содержимое:")
    print("-" * 20)
    print(content)
    print("-" * 20)
