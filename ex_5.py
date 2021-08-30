X, Y, Z = map(int, input("Введите количество покупок:").split())
Cx = 3
Cy = Cx + 2
Cz = Cy + 7
S = X * Cx + Cy * Y + Z * Cz
print("Сумма покупки:", S)
