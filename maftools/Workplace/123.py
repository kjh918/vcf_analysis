import os, sys
import pandas as pd 

pwd = os.getcwd()+'/Num_maf'

file_list = os.listdir(pwd)

for i in file_list[:1]:
    a = i.split('.')[0]
    print(a)
    x = []
    with open(pwd+'/'+i,'r') as handle:
        for line in handle:
            if line.startswith('#') == False:
                line = line.replace('\n','')
                x.append(line.split('\t'))
    sample = pd.DataFrame(x)
    sample.columns = list(sample.loc[0])
    sample = sample[1:]
    sample['Tumor_Sample_Barcode'] = sample.Tumor_Sample_Barcode.apply(lambda x: x.lstrip('Japan '))
    sample['a'] = sample.Tumor_Sample_Barcode.str.split('-').str[0]
    sample['b'] = sample.Tumor_Sample_Barcode.str.split('-').str[2]
    sample['a'] = sample.a.apply(lambda x:x.lower())
    #sample['b'] = sample['a'].str.replace('4w','mid')
    #sample['b'] = sample.b.apply(lambda x:x.lower())
    blood = sample[sample.a=='blood']
    cfdna = sample[sample.a=='cf']
    ctc = sample[sample.a=='ctc']
    x = list(set(list(blood.b)))
    for i in x:
        if i in ['pro','Pro']:
            cfdna_pro = cfdna[cfdna.b==i]
            ctc_pro = ctc[ctc.b==i]
            for j in list(blood[blood.b==i]['HGVSc']):
                cfdna_pro.drop(cfdna_pro.loc[cfdna_pro['HGVSc']==j].index,inplace=True)
                ctc_pro.drop(ctc_pro.loc[ctc_pro['HGVSc']==j].index,inplace=True)
            df_1 = pd.concat([ctc_pro,cfdna_pro])
            df_1['a'] = df_1.a.apply(lambda x:x+'_'+i)
            print(df_1)
        elif i in ['pre','Pre']:
            cfdna_pre = cfdna[cfdna.b==i]
            ctc_pre = ctc[ctc.b==i]
            for j in list(blood[blood.b==i]['HGVSc']):
                cfdna_pre.drop(cfdna_pre.loc[cfdna_pre['HGVSc']==j].index,inplace=True)
                ctc_pre.drop(ctc_pre.loc[ctc_pre['HGVSc']==j].index,inplace=True)
            df_2 = pd.concat([ctc_pre,cfdna_pre])
            df_2['a'] = df_2.a.apply(lambda x:x+'_'+i)
        else:
            cfdna_4w = cfdna[cfdna.b==i]
            ctc_4w = ctc[ctc.b==i]
            for j in list(blood[blood.b==i]['HGVSc']):
                cfdna_4w.drop(cfdna_4w.loc[cfdna_4w['HGVSc']==j].index,inplace=True)
                ctc_4w.drop(ctc_4w.loc[ctc_4w['HGVSc']==j].index,inplace=True)
            df_3 = pd.concat([ctc_4w,cfdna_4w])
            df_3['a'] = df_3.a.apply(lambda x:x+'_'+i)

    df = pd.concat([df_1,df_2,df_3])
    df.index = range(0,len(df.index))
    print(df)
    #df.to_csv(os.getcwd()+'/somatic/'+a+'_filtering.maf')
    #df.to_excel(os.getcwd()+'/filter_folder/'+a+'_SNV_filtering.xlsx')

