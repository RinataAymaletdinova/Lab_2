year = input("Введите год")
if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
    print("Год", year, "- високосный")
else:
    print("Этот год не високосный")