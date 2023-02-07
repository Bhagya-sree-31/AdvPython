import pandas as pd
df=pd.read_csv('..//data/train.csv')
print(df.shape)
df.drop(['Cabin'],axis=1,inplace=True)
df.fillna(method='ffill',inplace=True)
#print(df['Embarked'])
print(pd.crosstab(index=df['Sex'],columns=df['Survived']))
#print(df.groupby(['Sex','Survived'])['Survived'].count())
t(pd.pivot_table(df,index=['Sex'],columns=def['Survived']))


