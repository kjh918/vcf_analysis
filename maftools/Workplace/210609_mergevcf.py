import os
import pandas as pd 

input_file = '/BiO/Research/maftools/1_merge_pre.vcf.gz'


CHR=[]
POS=[]
GT=[]
with open(input_file, 'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        if line.startswith('#'):
            continue
        if line.split('\t')[-1].split(':')[0] !='0/0':
            CHR.append(line.split('\t')[0])
            POS.append(line.split('\t')[1])
            GT.append(line.split('\t')[-1].split(':')[0])
df = pd.DataFrame([CHR,POS,GT]).T
df.columns = ['CHR','POS','GT']
print(df)
