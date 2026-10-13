sample_name = input("Введите название образца: ")
sample_volume = input("Введите объём образца (мл): ")

sample_date = "2026-10-13"  # фиксированная дата

with open("sample_log.txt", "w", encoding="utf-8") as file:
    file.write(f"Дата взятия образца: {sample_date}\n")
    file.write(f"Название образца: {sample_name}\n")
    file.write(f"Объём: {sample_volume} мл\n")

print("Данные сохранены в sample_log.txt")
