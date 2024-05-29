import pandas as pd
import xlsxwriter


workbook = xlsxwriter.Workbook("wydatki.xlsx")
worksheet = workbook.add_worksheet("moje_wydatki")

#deklaracja formatu komórek
bold = workbook.add_format({'bold':True})
money = workbook.add_format({'num_format':'#.## 0zł'})
worksheet.write('A1','id',bold)
worksheet.write('B1','rodzaj wydatku',bold)
worksheet.write('C1','kwota',bold)

wydatki = (
    ['1','żywność',2500],
    ['2','czynsz',1200],
    ['3','gaz',880],
    ['4','prąd',620],
    ['5','woda',312],
    ['6','samochód',1100],
    ['7','edukacja',500],
    ['8','hobby',350],
    ['9','ubrania i inne',700]
)

row = 1
col = 0

for id,rodzaj,koszt in (wydatki):
    worksheet.write(row,col,id)
    worksheet.write(row,col+1,rodzaj)
    worksheet.write(row,col+2,koszt,money)
    row+=1

worksheet.write(row,0,'Koszt całkowity',bold)
worksheet.write(row,2,'=SUM(c2:c10)',bold)
workbook.close()
