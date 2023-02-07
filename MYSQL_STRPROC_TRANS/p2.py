from openpyxl import Workbook
from pandas import read_excel
sheet=[]
file="C://Users/user789/Desktop/Dataclasses.xlsx"
i=1
for f in ["jan","feb","march"]:
    df=""
    name="HCL_SALES_"+f
    df= df + str(i)
    df=read_excel(file,name)
    i+=1
    sheet.append(df)
dataframe=pd.concat(sheet)
print(dataframe.reset_index())