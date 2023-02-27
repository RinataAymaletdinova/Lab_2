ticket = input("Введите номер места")
if int(ticket) < 37:
    if int(ticket) % 2 == 0:
        print("Купе, верхнее место")
    else:
            print("Купе, нижнее место")
else:
    if int(ticket) % 2 == 0:
        print("Боковое, верхнее место")
    else:
        print("Боковое, нижнее место")
