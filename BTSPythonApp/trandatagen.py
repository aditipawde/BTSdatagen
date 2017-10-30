#%%
# import packages
import pandas as pd
import random
import numpy as np
#%%
# Variable initialization
c_dataframe = pd.read_csv(r'G:\Study\2017-2018\Internship work\Coding\BTSPythonApp\BTSPythonApp\companyMetadata.csv')
c_dataframe.set_index('comp_id')
sample_size = 20000
N = len(c_dataframe)
b_low, b_high = 5, 600
s_low, s_high = 601, 1000
r_low, r_high = 1001, 10000
tran_mode = ['CASH', 'CHEQUE','TRANSFER']


# Distributions
# Normal distributioons for amounts
mu1, sigma1 = 5000, 1000; N1 = np.random.normal(mu1, sigma1, sample_size)
mu2, sigma2 = 50000, 10000; N2 = np.random.normal(mu2, sigma2, sample_size)
mu3, sigma3 = 500000, 100000; N3 = np.random.normal(mu3, sigma3, sample_size)
mu4, sigma4 = 5000000, 1000000; N4 = np.random.normal(mu4, sigma4, sample_size)
mu5, sigma5 = 50000000, 10000000; N5 = np.random.normal(mu5, sigma5, sample_size)

# Mixtures
mix34 = np.round(np.concatenate((N3,N4), axis=0), 2)
mix123 = np.round(np.concatenate((N1,N2,N3), axis=0), 2)

#%%
# Generate account details
c_id = acc_no = range(N)
acc_type = np.random.choice(['C', 'S'], N, p=[0.99, 0.01])
cust_type = ['C'] * N
balance = np.random.choice(mix34, N)
clist = list(zip(acc_no, acc_type, cust_type, c_id, balance))
comp_df = pd.DataFrame(clist, columns=['acc_no', 'acc_type', 'cust_type',  'comp_id', 'balance'])

c_acc_no = np.random.randint(N, 2*N, N)
c_acc_type = np.random.choice(['C', 'S'], N, p=[0.01, 0.99])
c_cust_type = ['I']*N
c_compid = ['']*N
c_bal = np.random.choice(mix123, N)
c_list = list(zip(c_acc_no, c_acc_type, c_cust_type, c_compid, c_bal))
cust_df = pd.DataFrame(c_list, columns=['acc_no', 'acc_type', 'cust_type','comp_id',  'balance'])

c_dataframe.insert(loc=len(c_dataframe.columns), column='expenses', value=np.zeros_like(N))
c_dataframe.expenses = c_dataframe.annual_revenue - c_dataframe.net_revenue

acc_df = pd.concat([comp_df, cust_df],axis=0, ignore_index=False)
acc_df.set_index('acc_no')


tran_df = pd.DataFrame(columns=['id', 'from_acc', 'to_acc', 'amount','mode', 'date'])
tran_df.set_index('id')
#%%

# Generate annual revenue for companies
comp_id = 0
acc_no, category, ann_rev = acc_df.acc_no[acc_df['comp_id'] == comp_id], c_dataframe.loc[comp_id, 'industry_category'], c_dataframe.loc[comp_id, 'annual_revenue']
id = 0
n_customers = random.randint(10, 60)
# 75% customers who are companies within same bank
cust_list = list(np.concatenate([np.random.choice(comp_df.acc_no, int(0.75*n_customers)), np.random.choice(cust_df.acc_no, (n_customers - len(cust_within_bank)))]))
rev_temp = 0
while (ann_rev > rev_temp):
    c = random.choice(cust_list)
    c_balance = acc_df.loc[c].balance
    c_expenses = c_dataframe.loc[c].expenses
    if (c_balance > 0):
        amt = np.random.choice(mix34)
        if (c_expenses > amt):
            rev_temp = rev_temp + amt
            tran_df.loc[id]=[id, c, comp_id, amt, np.random.choice(tran_mode,p=[0.25, 0.5, 0.25]),np.nan]
            id=id+1
#%%
# Generate expenses for companies