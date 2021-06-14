import os
import pandas as pd

pwd = os.getcwd()
folder_list = os.listdir(pwd + '/maf_result')

for i in folder_list:
    a = pd.read_csv(pwd+'/maf_result/'+i+'/_summary.txt',sep='\t')
    a.index = list(a['ID'])
    b = a['summary']
    if i == folder_list[0]:
        c = pd.DataFrame(b)
    else:
        c = pd.merge(c,pd.DataFrame(b),left_index=True,right_index=True,how='outer')

c.columns = [int(i.split('.')[0]) for i in folder_list]
df = c.T
df = df.sort_index(ascending=True)
c = df.T
c = c.fillna(0)
print(c)
dff = c.drop(['Center','NCBI_Build','Samples','nGenes','total'])
# c.to_excel(pwd+'/num_summary.xlsx',header=True)
print(dff)
