import os

reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество (целое число): "))

report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."
print(report)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "inventory.txt")

with open(file_path, "w", encoding="utf-8") as file:
    file.write(report)
