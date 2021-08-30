a, b = map(int, input("Введите рубли/копейки:").split())
n = int(input("Введите количество пирожков:"))
cost = n * (100 * a + b)
print(cost // 100, cost % 100)
