#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


#%%
c_dataframe = pd.read_csv(r'G:\Study\2017-2018\Internship work\Coding\BTSPythonApp\BTSPythonApp\companyMetadata.csv')

#%%
style.use('ggplot')
fig1 = plt.figure(1)
fig1.suptitle('Distribution of number of employees', fontsize=16, fontweight='bold')
#%%
size = 'VERY SMALL'

series = c_dataframe.loc[c_dataframe.loc[:, 'emp_base'] == size].loc[:, 'num_employees']

ax1 = fig1.add_subplot(321)

ax1.hist(series, bins=10)
ax1.set_title('Employee base category - VERY SMALL', fontsize=10)
ax1.set_xlabel('Number of employees', fontsize=8)
ax1.set_ylabel('Frequency', fontsize=8)


#%%
size = 'SMALL'

series = c_dataframe.loc[c_dataframe.loc[:, 'emp_base'] == size].loc[:, 'num_employees']
#print(series)
#style.use('ggplot')
ax2 = fig1.add_subplot(322)
ax2.hist(series, bins=11)
ax2.set_title('Employee base category - SMALL', fontsize=10)
ax2.set_xlabel('Number of employees', fontsize=8)
ax2.set_ylabel('Frequency', fontsize=8)

#%%
size = 'MEDIUM'

series = c_dataframe.loc[c_dataframe.loc[:, 'emp_base'] == size].loc[:, 'num_employees']

ax3 = fig1.add_subplot(323)
ax3.hist(series, bins=11)
ax3.set_title('Employee base category - MEDIUM', fontsize=10)
ax3.set_xlabel('Number of employees', fontsize=8)
ax3.set_ylabel('Frequency', fontsize=8)

#%%

size = 'LARGE'

series = c_dataframe.loc[c_dataframe.loc[:, 'emp_base'] == size].loc[:, 'num_employees']
#print(series)
#style.use('ggplot')
ax4 = fig1.add_subplot(324)
ax4.hist(series, bins=11)
ax4.set_title('Employee base category - LARGE', fontsize=10)
ax4.set_xlabel('Number of employees', fontsize=8)
ax4.set_ylabel('Frequency', fontsize=8)

#%%
size = 'VERY LARGE'

series = c_dataframe.loc[c_dataframe.loc[:, 'emp_base'] == size].loc[:, 'num_employees']
#style.use('ggplot')
ax5 = fig1.add_subplot(325)
ax5.hist(series, bins=11)
ax5.set_title('Employee base category - VERY LARGE', fontsize=10)
ax5.set_xlabel('Number of employees', fontsize=8)
ax5.set_ylabel('Frequency', fontsize=8)

#%%
size = 'EXTRA LARGE'

series = c_dataframe.loc[c_dataframe.loc[:, 'emp_base'] == size].loc[:, 'num_employees']
#style.use('ggplot')
ax6 = fig1.add_subplot(326)
ax6.hist(series, bins=11)
ax6.set_title('Employee base category - EXTRA LARGE', fontsize=10)
ax6.set_xlabel('Number of employees', fontsize=8)
ax6.set_ylabel('Frequency', fontsize=8)

fig1.savefig('NoOfEMployeesDistribution.png')
plt.show()

#%%
fig2 = plt.figure(2)
fig2.suptitle('Distributions of companies', fontsize=12, fontweight='bold')
ns = 10
industry_sectors = np.arange(ns)
industry_sector_names = ['Comp.s/w', 'Hotels-resorts', 'Clth manu.', 'Construc.', 'Elex comp. M','Chem.M.', 'Insurance A.', 'Jewelers','Medi.N.','Pharma']
#%%
cnt_per_sector = []
for sector in industry_sectors:
    cnt_per_sector.append(len(c_dataframe.loc[c_dataframe.loc[:, 'industry_sector'] == sector]))
    
ax1 = fig2.add_subplot(221)
ax1.bar(industry_sectors, cnt_per_sector, label='Number of companies per sector')
ax1.set_xticks(industry_sectors)
ax1.set_xticklabels(industry_sector_names, rotation=45)
ax1.set_title('No. of companies per sector', fontsize=10)
ax1.set_xlabel('Industry sector', fontsize=8)
ax1.set_ylabel('No. of companies', fontsize=8)

#%%
number_of_emp = c_dataframe.loc[:, 'num_employees']
bins = 11
ax2 = fig2.add_subplot(222)
ax2.hist(number_of_emp, bins)
ax2.set_xlabel('Number of employees', fontsize=8)
ax2.set_ylabel ('Frequency', fontsize=8)
ax2.set_title('Distribution of number of employees', fontsize=10)
ax2.set_yscale('log')

#%%
annual_rev = c_dataframe.loc[:, 'annual_revenue']
bins = 11
ax3 = fig2.add_subplot(223)
ax3.hist(annual_rev, bins)
ax3.set_xlabel('Annual revenue', fontsize=8)
ax3.set_ylabel('Number of companies', fontsize=8)
ax3.set_title('Distribution of annual revenue', fontsize=10)
ax3.set_yscale('log')

#%%

net_rev = c_dataframe.loc[:, 'net_revenue']
bins = 9
ax4 = fig2.add_subplot(224)
ax4.hist(net_rev, bins)
ax4.set_xlabel('Net revenue', fontsize=8)
ax4.set_ylabel('Number of companies', fontsize=8)
ax4.set_title('Distribution of net revenue', fontsize=10)
ax4.set_yscale('log')

fig2.savefig('AllDistributions.png')
plt.show()

#%%

fig3 = plt.figure(3)
fig3.suptitle('Distribution of annual revenue for various categories of rev./employee/month', fontsize=12, fontweight='bold')
#%%
size = 'VERY LOW'

R = (c_dataframe.loc[c_dataframe.loc[:, 'rev_per_emp_month_size'] == size]).loc[:, 'annual_revenue']
bins = 11
ax1 = fig3.add_subplot(321)
ax1.hist(R, bins)
ax1.set_xlabel('Annual revenue', fontsize=8)
ax1.set_ylabel('Number of companies', fontsize=8)
ax1.set_title('Rev./month/employee category - VERY LOW', fontsize=10)
ax1.set_yscale('log')
print('Median: ', np.median(R), 'Min: ', np.min(R), 'Max: ', np.max(R))

#%%
size = 'LOW'

R = (c_dataframe.loc[c_dataframe.loc[:, 'rev_per_emp_month_size'] == size]).loc[:, 'annual_revenue']

ax2 = fig3.add_subplot(322)
ax2.hist(R, bins)
ax2.set_xlabel('Annual revenue', fontsize=8)
ax2.set_ylabel('Number of companies', fontsize=8)
ax2.set_title('Rev./month/employee category - LOW', fontsize=10)
ax2.set_yscale('log')

print('Median: ', np.median(R), 'Min: ', np.min(R), 'Max: ', np.max(R))
#%%

#%%
size = 'MEDIUM'

R = (c_dataframe.loc[c_dataframe.loc[:, 'rev_per_emp_month_size'] == size]).loc[:, 'annual_revenue']
ax3 = fig3.add_subplot(323)
ax3.hist(R, bins)
ax3.set_xlabel('Annual revenue', fontsize=8)
ax3.set_ylabel('Number of companies', fontsize=8)
ax3.set_title('Rev./month/employee category - MEDIUM', fontsize=10)
ax3.set_yscale('log')

print('Median: ', np.median(R), 'Min: ', np.min(R), 'Max: ', np.max(R))
#%%

#%%
size = 'HIGH'

R = (c_dataframe.loc[c_dataframe.loc[:, 'rev_per_emp_month_size'] == size]).loc[:, 'annual_revenue']
ax4 = fig3.add_subplot(324)
ax4.hist(R, bins)
ax4.set_xlabel('Annual revenue', fontsize=8)
ax4.set_ylabel('Number of companies', fontsize=8)
ax4.set_title('Rev./month/employee category - HIGH', fontsize=10)
ax4.set_yscale('log')

print('Median: ', np.median(R), 'Min: ', np.min(R), 'Max: ', np.max(R))
#%%
size = 'VERY HIGH'

R = (c_dataframe.loc[c_dataframe.loc[:, 'rev_per_emp_month_size'] == size]).loc[:, 'annual_revenue']
ax5 = fig3.add_subplot(325)
ax5.hist(R, bins)
ax5.set_xlabel('Annual revenue', fontsize=8)
ax5.set_ylabel('Number of companies', fontsize=8)
ax5.set_title('Rev./month/employee category - VERY HIGH', fontsize=10)
ax5.set_yscale('log')

print('Median: ', np.median(R), 'Min: ', np.min(R), 'Max: ', np.max(R))
#%%

#%%
size = 'EXTRA HIGH'

R = (c_dataframe.loc[c_dataframe.loc[:, 'rev_per_emp_month_size'] == size]).loc[:, 'annual_revenue']
ax6 = fig3.add_subplot(326)
ax6.hist(R, bins)
ax6.set_xlabel('Annual revenue', fontsize=8)
ax6.set_ylabel('Number of companies', fontsize=8)
ax6.set_title('Rev./month/employee category - EXTRA HIGH', fontsize=10)
ax6.set_yscale('log')

fig3.savefig('AnnualRevenue.png')
plt.show()
print('Median: ', np.median(R), 'Min: ', np.min(R), 'Max: ', np.max(R))
#%%

fig4, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
fig4.suptitle('Sector wise distribution of annual revenue', fontsize=12, fontweight='bold')
c_dataframe.boxplot(column='annual_revenue', by='industry_sector', ax=ax[0], showmeans=True)
c_dataframe.boxplot(column='annual_revenue', by='industry_sector', ax=ax[1], showmeans=True)
#ax[0].set_xticks(industry_sectors)
#ax[0].set_xticklabels(industry_sector_names, rotation=40)
ax[0].set_title('On linear scale', fontsize=10)
ax[1].set_title('On log scale', fontsize=10)
ax[1].set_xticks(industry_sectors)
ax[1].set_xticklabels(industry_sector_names, rotation=30)
ax[1].set_yscale('log')
fig4.savefig('SectorwiseAnnualRevenue.png')
plt.show()
#%%

fig5, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
fig4.suptitle('Sector wise distribution of annual revenue', fontsize=12, fontweight='bold')
c_dataframe.boxplot(column='net_revenue', by='industry_sector', ax=ax[0], showmeans=True)
c_dataframe.boxplot(column='net_revenue', by='industry_sector', ax=ax[1], showmeans=True)
#ax[0].set_xticks(industry_sectors)
#ax[0].set_xticklabels(industry_sector_names, rotation=40)
ax[0].set_title('On linear scale', fontsize=10)
ax[1].set_title('On log scale', fontsize=10)
ax[1].set_xticks(industry_sectors)
ax[1].set_xticklabels(industry_sector_names, rotation=30)
ax[1].set_yscale('log')
fig4.savefig('SectorwiseNetRevenue.png')
plt.show()
#%%
