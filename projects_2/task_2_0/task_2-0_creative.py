import os

info = "Фамилия: Тишура\nИмя: Егор\nГруппа: 202.1\nГод поступления: 2025"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "output.txt")

with open(file_path, "w", encoding="utf-8") as file:
    file.write(info)

with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())
