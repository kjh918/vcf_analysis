import os
import pandas as pd 

path1 = '/BiO/Research/maftools/0.Rawdata/'
path2 = '/BiO/Research/martools/1.Somatic/'

ind = list(set([int(i.split('_')[0]) for i in os.listdir(path1)]))
ind.sort()
sample = ['blood','ctcdna','cfdna']
step = ['pre.vcf','4w.vcf','pro.vcf']

header = []
for i in ind[:1]:
    for st in step:
        blood = str(i)+'_'+sample[0]+'_'+st
        ctc = str(i)+'_'+sample[1]+'_'+st
        cf = str(i)+'_'+sample[2]+'_'+st
        if blood in os.listdir(path1):
            germ_summary = []
            with open(path1+blood,'r') as handle:
                for line in handle:
                    line = line.replace('\n','')
                    germ_data = []
                    if line.startswith('##'):
                        continue
                    if line.startswith('#'):
                        header = line.split('\t')
                    else:
                        if (int(line.split('\t')[-1].split(':')[2])) < 500:
                            pass
                        elif (float(line.split('\t')[-1].split(':')[8].split(',')[0]) < 0.01):
                            pass
                        elif line.split('\t')[-1].split(':')[0] not in ['0/0','./.']:
                            raw_data = line.split('\t')
                            germ_data.append(raw_data[0])
                            germ_data.append(raw_data[1])
                            GT = line.split('\t')[-1].split(':')[0].split('/')
                            REF = [line.split('\t')[3]]
                            ALT = line.split('\t')[4].split(',')
                            for z in ALT:
                                REF.append(z)
                            germ_data.append(str(REF[int(GT[0])])+'/'+str(REF[int(GT[1])]))
                            germ_summary.append(germ_data)
            
        else:
            pass
        if ctc in os.listdir(path1):
            ctc_summary = []
            with open(path1+ctc,'r') as handle:
                for line in handle:
                    line = line.replace('\n','')
                    ctc_data = []
                    if line.startswith('##')|line.startswith('#'):
                        continue
                    else:
                        if (int(line.split('\t')[-1].split(':')[2])) < 500:
                            pass
                        elif (float(line.split('\t')[-1].split(':')[8].split(',')[0]) < 0.01):
                            pass
                        elif line.split('\t')[-1].split(':')[0] not in ['0/0','./.']:
                            raw_data = line.split('\t')
                            ctc_data.append(raw_data[0])
                            ctc_data.append(raw_data[1])
                            GT = line.split('\t')[-1].split(':')[0].split('/')
                            REF = [line.split('\t')[3]]
                            ALT = line.split('\t')[4].split(',')
                            for z in ALT:
                                REF.append(z)
                            ctc_data.append(str(REF[int(GT[0])])+'/'+str(REF[int(GT[1])]))
                            ctc_summary.append(ctc_data)
            
        if cf in os.listdir(path1):
            cf_summary = []
            with open(path1+cf,'r') as handle:
                for line in handle:
                    line = line.replace('\n','')
                    cf_data = [] 
                    if line.startswith('##')|line.startswith('#'):
                        continue
                    else:
                        if (int(line.split('\t')[-1].split(':')[2])) < 500:
                            pass
                        elif (float(line.split('\t')[-1].split(':')[8].split(',')[0]) < 0.01):
                            pass
                        elif line.split('\t')[-1].split(':')[0] not in ['0/0','./.']:
                            raw_data = line.split('\t')
                            cf_data.append(raw_data[0])
                            cf_data.append(raw_data[1])
                            GT = line.split('\t')[-1].split(':')[0].split('/')
                            REF = [line.split('\t')[3]]
                            ALT = line.split('\t')[4].split(',')
                            for z in ALT:
                                REF.append(z)
                            cf_data.append(str(REF[int(GT[0])])+'/'+str(REF[int(GT[1])]))
                            cf_summary.append(cf_data)
germ_df = pd.DataFrame(germ_summary)
ctc_df = pd.DataFrame(ctc_summary)
cf_df = pd.DataFrame(cf_summary)
print(germ_df)
print(ctc_df)
print(cf_df)
#germ_df.columns = header
#ctc_df.columns = header
#cf_df.columns = header

#ctc = pd.merge(ctc_df,germ_df,how='left',on=['#CHROM','POS'])
#ctc.to_excel('1.xlsx')
'''
for i in os.listdir(path1)[:1]:
    meta = []
    header = []
    data = []
    description = []
    with open(path1+i,'r') as handle:
        for line in handle:
            line = line.replace('\n','')
            if line.startswith('##'):
                meta.append(line)
            elif line.startswith('#'):
                header.append(line)
            else:
                data.append(line)
    #print(header)
    for j in range(len(data)):
        POS = data[j].split('\t')[1]
        GT = data[j].split('\t')[-1].split(':')[0]
    print(POS)
    print(GT)
'''         

