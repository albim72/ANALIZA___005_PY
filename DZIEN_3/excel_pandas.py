import pandas as pd
import xlsxwriter

df = pd.DataFrame({'Data':[10,13,14,56,86,36,78,90,446,35,67,2,578,9]})

writer = pd.ExcelWriter('pandas_dane.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='ramka')
writer._save()
