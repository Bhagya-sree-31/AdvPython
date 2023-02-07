import pandas as pd
import numpy as np
df=pd.read_csv("C://Users/user789/Desktop/Data.csv")
print(df)
class Readcsv():
    def create_df(self,path):
        self.path=path
        self.df=pd.DataFrame(self.path)
        self.df['Total']=self.df['M1']+self.df['M2']+self.df['M3']+self.df['M4']+self.df['M5']+self.df['M6']
        print(self.df['Total'])
