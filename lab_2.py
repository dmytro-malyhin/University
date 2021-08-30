# lab2
import math
import csv
from openpyxl import Workbook

NomerLopati = [1, 2, 3]
NomerDoslid = [1, 2, 3]
Nvt1 = [18.3, 18.5, 19.0]
Nvt2 = [18.6, 19.9, 22.5]
Nvt3 = [19.8, 21.8, 25.1]
Nobhv = [327, 572, 815]
Ncek = [(Nobhv[0] / 60), (Nobhv[1] / 60), (Nobhv[2] / 60)]
p = 880
u = 0.098
e = 2.71
R = [0.0165, 0.024, 0.037]
d = [0.054, 0.0883, 0.127]
print(
    f'Витрата потужності до першої лопаті,першого досліду:{Nvt1[0]},другого досліду:{Nvt1[1]},третего досліду:{Nvt1[2]}')
print(
    f'Витрата потужності до другої лопаті,першого досліду:{Nvt2[0]},другого досліду:{Nvt2[1]},третего досліду:{Nvt2[2]}')
print(
    f'Витрата потужності до другої лопаті,першого досліду:{Nvt3[0]},другого досліду:{Nvt3[1]},третего досліду:{Nvt3[2]}')
print(f'Діаметр лопаті для першого експеременту:{d[0]},другого досліду:{d[1]},третего досліду:{d[2]}')
print(
    f'Висота змінних лопастей для першого експеременту:{R[0]},лругого досліду {R[1]},третего досліду:{R[2]}')  # возможно не высота?
print(f'Частота обертання для перша:{Ncek[0]},друга:{Ncek[1]},третя:{Ncek[2]}')
Eum11 = (Nvt1[0]) / (u * (Ncek[0] ** 2) * (d[0] ** 3))
Eum12 = (Nvt1[1]) / (u * (Ncek[1] ** 2) * (d[0] ** 3))
Eum13 = (Nvt1[2]) / (u * (Ncek[2] ** 2) * (d[0] ** 3))
Eum21 = (Nvt2[0]) / (u * (Ncek[0] ** 2) * (d[1] ** 3))
Eum22 = (Nvt2[1]) / (u * (Ncek[1] ** 2) * (d[1] ** 3))
Eum23 = (Nvt2[2]) / (u * (Ncek[2] ** 2) * (d[1] ** 3))
Eum31 = (Nvt3[0]) / (u * (Ncek[0] ** 2) * (d[2] ** 3))
Eum32 = (Nvt3[1]) / (u * (Ncek[1] ** 2) * (d[2] ** 3))
Eum33 = (Nvt3[2]) / (u * (Ncek[2] ** 2) * (d[2] ** 3))
print(f'Критерій Ейлера для першого досліду першої лопаті:{Eum11},другого:{Eum12},третего:{Eum13}')
print(f'Критерій Ейлера для першого досліду другої лопаті:{Eum21},другого:{Eum22},третего:{Eum23}')
print(f'Критерій Ейлера для першого досліду третьої лопаті:{Eum31},другого:{Eum32},третего:{Eum33}')
Re11 = (p * Ncek[0] * d[0] ** 2) / u
Re12 = (p * Ncek[1] * d[0] ** 2) / u
Re13 = (p * Ncek[2] * d[0] ** 2) / u
Re21 = (p * Ncek[0] * d[1] ** 2) / u
Re22 = (p * Ncek[1] * d[1] ** 2) / u
Re23 = (p * Ncek[2] * d[1] ** 2) / u
Re31 = (p * Ncek[0] * d[2] ** 2) / u
Re32 = (p * Ncek[1] * d[2] ** 2) / u
Re33 = (p * Ncek[2] * d[2] ** 2) / u
print(f'Критерій Рейнольдса для першого досліду першої лопаті:{Re11},другого:{Re12},третего:{Re13}')
print(f'Критерій Рейнольдса для першого досліду другої лопаті:{Re21},другого:{Re22},третего:{Re23}')
print(f'Критерій Рейнольдса для першого досліду третьої лопаті:{Re31},другого:{Re32},третего:{Re33}')
EumLog11 = math.log1p(Eum11)
EumLog12 = math.log1p(Eum12)
EumLog13 = math.log1p(Eum13)
EumLog21 = math.log1p(Eum21)
EumLog22 = math.log1p(Eum22)
EumLog23 = math.log1p(Eum23)
EumLog31 = math.log1p(Eum31)
EumLog32 = math.log1p(Eum32)
EumLog33 = math.log1p(Eum33)
print(f'Логарифм числа Ейлера до першої лопаті першого експеременту:{EumLog11},другого:{EumLog12},третего:{EumLog13}')
print(f'Логарифм числа Ейлера до другої лопаті першого експеременту:{EumLog21},другого:{EumLog22},третего:{EumLog23}')
print(f'Логарифм числа Ейлера до третьої лопаті першого експеременту:{EumLog31},другого:{EumLog32},третего:{EumLog33}')
ReLog11 = math.log1p(Re11)
ReLog12 = math.log1p(Re12)
ReLog13 = math.log1p(Re13)
ReLog21 = math.log1p(Re21)
ReLog22 = math.log1p(Re22)
ReLog23 = math.log1p(Re23)
ReLog31 = math.log1p(Re31)
ReLog32 = math.log1p(Re32)
ReLog33 = math.log1p(Re33)
print(f'Логарифм числа Рейнольдса до першої лопаті першого експеременту:{ReLog11},другого:{ReLog12},третего:{ReLog13}')
print(f'Логарифм числа Рейнольдса до другої лопаті першого експеременту:{ReLog21},другого:{ReLog22},третего:{ReLog23}')
print(f'Логарифм числа Рейнольдса до третьої лопаті першого експеременту:{ReLog31},другого:{ReLog32},третего:{ReLog33}')
workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Номер лопаті"
sheet["A2"] = NomerDoslid[0]
sheet["A3"] = NomerDoslid[1]
sheet["A4"] = NomerDoslid[2]
sheet["A5"] = NomerDoslid[0]
sheet["A6"] = NomerDoslid[1]
sheet["A7"] = NomerDoslid[2]
sheet["A8"] = NomerDoslid[0]
sheet["A9"] = NomerDoslid[1]
sheet["A10"] = NomerDoslid[2]
sheet["A12"] = "p"
sheet["B12"] = p
sheet["A13"] = "u"
sheet["B13"] = u
sheet["B1"] = 'N,ВТ'
sheet["B2"] = Nvt1[0]
sheet["B3"] = Nvt1[1]
sheet["B4"] = Nvt1[2]
sheet["B5"] = Nvt2[0]
sheet["B6"] = Nvt2[1]
sheet["B7"] = Nvt2[2]
sheet["B8"] = Nvt3[0]
sheet["B9"] = Nvt3[1]
sheet["B10"] = Nvt3[2]
sheet["C1"] = 'n,об/хв'
sheet["C2"] = Nobhv[0]
sheet["C3"] = Nobhv[1]
sheet["C4"] = Nobhv[2]
sheet["C5"] = Nobhv[0]
sheet["C6"] = Nobhv[1]
sheet["C7"] = Nobhv[2]
sheet["C8"] = Nobhv[0]
sheet["C9"] = Nobhv[1]
sheet["C10"] = Nobhv[2]
sheet["D1"] = 'n,c^-1'
sheet["D2"] = Ncek[0]
sheet["D3"] = Ncek[1]
sheet["D4"] = Ncek[2]
sheet["D5"] = Ncek[0]
sheet["D6"] = Ncek[1]
sheet["D7"] = Ncek[2]
sheet["D8"] = Ncek[0]
sheet["D9"] = Ncek[1]
sheet["D10"] = Ncek[2]
sheet["E1"] = 'R,m'
sheet["E2"] = R[0]
sheet["E3"] = R[1]
sheet["E4"] = R[2]
sheet["E5"] = R[0]
sheet["E6"] = R[1]
sheet["E7"] = R[2]
sheet["E8"] = R[0]
sheet["E9"] = R[1]
sheet["E10"] = R[2]
sheet["F1"] = 'd,m'
sheet["F2"] = d[0]
sheet["F3"] = d[1]
sheet["F4"] = d[2]
sheet["F5"] = d[0]
sheet["F6"] = d[1]
sheet["F7"] = d[2]
sheet["F8"] = d[0]
sheet["F9"] = d[1]
sheet["F10"] = d[2]
sheet["H1"] = 'Rem'
sheet["H2"] = Re11
sheet["H3"] = Re12
sheet["H4"] = Re13
sheet["H5"] = Re21
sheet["H6"] = Re22
sheet["H7"] = Re23
sheet["H8"] = Re31
sheet["H9"] = Re32
sheet["H10"] = Re33
sheet["I1"] = 'Eum'
sheet["I2"] = Eum11
sheet["I3"] = Eum12
sheet["I4"] = Eum13
sheet["I5"] = Eum21
sheet["I6"] = Eum22
sheet["I7"] = Eum23
sheet["I8"] = Eum31
sheet["I9"] = Eum32
sheet["I10"] = Eum33
sheet["J1"] = 'Логарифм числа Рейнольдса з основою e'
sheet["J2"] = ReLog11
sheet["J3"] = ReLog12
sheet["J4"] = ReLog13
sheet["J5"] = ReLog21
sheet["J6"] = ReLog22
sheet["J7"] = ReLog23
sheet["J8"] = ReLog31
sheet["J9"] = ReLog32
sheet["J10"] = ReLog33
sheet["M1"] = 'Логарифм числа Ейлера з основою e'
sheet["M2"] = EumLog11
sheet["M3"] = EumLog12
sheet["M4"] = EumLog13
sheet["M5"] = EumLog21
sheet["M6"] = EumLog22
sheet["M7"] = EumLog23
sheet["M8"] = EumLog31
sheet["M9"] = EumLog32
sheet["M10"] = EumLog33
workbook.save(filename='D:\\lAB2.xlsx')
