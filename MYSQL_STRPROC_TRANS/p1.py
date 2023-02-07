from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass()
class People():
    name:str
    no:int
    age:int
    #age:int
#p=People("bhagi",1,21)
p=[People("bhagi",1,21),People("sravya",2,20),People("shruthi",3,22)]
data=[[p.name,p.no,p.age] for p in p]
data=[["name","no","age"]]+data
for d in data:
    sheet.append(d)
wb.save("C://Users/user789/Desktop/Dataclasses.xlsx")
