a = 1
cnt = 0
while a:
    a = int(input('a= '))
if a > 0 and not a % 3:  # или if not a%3: если завершающий ноль тоже считать
    cnt += 1
print('Было введено', cnt, 'чисел кратных трем.')
