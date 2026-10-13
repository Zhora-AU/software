dna = input("Введите последовательность ДНК: ")
dna = dna.upper()

print("\n=== Анализ последовательности ДНК ===\n")
print(f"Последовательность в верхнем регистре: {dna}\n")

count_a = dna.count("A")
count_t = dna.count("T")
count_g = dna.count("G")
count_c = dna.count("C")
total = len(dna)

print("Подсчёт нуклеотидов:")
print(f"A: {count_a}")
print(f"T: {count_t}")
print(f"G: {count_g}")
print(f"C: {count_c}\n")

print(f"Общая длина: {total} нуклеотидов\n")

print("Процентное содержание:")
print(f"A: {count_a / total * 100:.2f}%")
print(f"T: {count_t / total * 100:.2f}%")
print(f"G: {count_g / total * 100:.2f}%")
print(f"C: {count_c / total * 100:.2f}%")
