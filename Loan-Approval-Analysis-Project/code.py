# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)





# code ends here


# --------------
# code starts here

banks = bank.drop(columns='Loan_ID')
print(banks.isnull().sum())
bank_mode = banks.mode()
banks.fillna(bank_mode.iloc[0],inplace=True)
banks.isna()
   

#code ends here


# --------------
# Code starts here
avg_loan_amount = banks.pivot_table(index = ['Gender','Married','Self_Employed'],
values ='LoanAmount',aggfunc = 'mean')



# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].shape[0]
loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].shape[0]
Loan_Status = 614
percentage_se = loan_approved_se/Loan_Status*100
percentage_nse = loan_approved_nse/Loan_Status*100





# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)
print(loan_term)
big_loan_term = loan_term.loc[lambda x : x>= 25].count()
print(big_loan_term)



# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()




# code ends here


