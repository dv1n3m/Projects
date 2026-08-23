#Hi, this is my first project that i store in github :)


import numpy as np
import pandas as pd

#Make the data
Bank_df_1 = pd.DataFrame({
    'Client Name Complete':['Pedro Pascal','Rocio Campos','Maria Bustamante','Joel Mendoza','Lucia de las Fuentes'],
    'Client ID':[1,2,3,4,5]},
    index=[0,1,2,3,4])



Bank_df_2 = pd.DataFrame({
    'Client Name Complete':['Mauricio Vasquez','Anna Merino','Juan Fajardo','Luis de las Casas','Sabrina Montenegro'],
    'Client ID':[6,7,8,9,10]},
    index=[5,6,7,8,9])

list_salary = np.random.randint(10000,80000,10)
Salary = pd.DataFrame({'Annual Salary [$]':list_salary,
                       'Client ID':[1,2,3,4,5,6,7,8,9,10]})

#Modify and create new data
Bank_df = pd.concat((Bank_df_1,Bank_df_2),axis=0)

Bank_df = pd.merge(Bank_df,Salary,on='Client ID')

#Create a new client
raw_data = {
    'Client ID':[11],
    'Client Name Complete':['Jose Riveros'],
    'Annual Salary [$/year]':[32512]}
new_client = pd.DataFrame(
    raw_data,
    columns=['Client Name Complete','Client ID','Annual Salary [$/year]'],
    index=[10])

pd.concat((Bank_df,new_client),axis=0)
