import pandas as pd
#load dataset
df=pd.read_csv('IPL_data.csv')

#display first rows
#print(df.head())

#check data information
#print(df.info())

#check missing values
#print(df.isnull().sum())

#fill missing values
df['city']=df['city'].fillna('Unknown')
df['winner']=df['winner'].fillna("No result")

#remove duplicate rows
df=df.drop_duplicates()

#standardize team names
df['winner']=df['winner'].replace({
    'Delhi Daredevils':'Delhi Capitals'
})

#convert data type season into int
df['season']=df['season'].astype(int)

#save cleaned dataset
df.to_csv("cleaned_ipl_dataset.csv")

print("IPL dataset cleaned successfully")

print(df['winner'].value_counts().head())