import openpyxl
wb=openpyxl.load_workbook("C://Users/user789/Desktop/Data1.xlsx")
sheet=wb.active
data=sheet['A3'].value
data3=sheet.cell(row=2,column=3).value
data1=sheet['A1:A10']
print(data)
print(data1)
print(sheet)
