volume = float(input("Введите нужный объем раствора (мл): "))

salt_mass = volume * 0.009
water_volume = volume

report = (
    "ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n"
    + "-" * 23 + "\n"
    + f"Общий объем: {volume} мл\n"
    + f"Масса соли:  {salt_mass:.2f} г\n"
    + f"Объем воды:  {water_volume} мл\n"
)

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Файл recipe.txt успешно сформирован!")
