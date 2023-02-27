pas = input("Введите пароль")
if len(pas) > 6:
    pas2 = input("Введите пароль повторно")
    if pas == pas2:
        print("Пароль принят")
    else:
        print("Пароль не принят")
else:
    print("Ненадежный пароль")
