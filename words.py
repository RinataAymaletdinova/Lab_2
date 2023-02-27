N = input("Введите количество слов")
s = ''
for i in range(1, int(N)+1):
    word = input("Введите слово")
    s = s + word + ' '
print(s)