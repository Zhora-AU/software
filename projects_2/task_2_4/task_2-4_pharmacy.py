total_capsules = int(input("Введите общее количество произведенных капсул: "))
per_package = int(input("Введите количество капсул в одной упаковке: "))

full_packages = total_capsules // per_package
remainder = total_capsules % per_package

print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packages}")
print(f"Остаток капсул:\t\t{remainder}")
print("=" * 98)
