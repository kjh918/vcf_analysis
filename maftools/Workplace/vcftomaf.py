import os
import shutil

f = os.getcwd()

folder_1 = f+'/Cancer_Type'
folder_2 = f+'/Sample'

folder_list = os.listdir(folder_1)

for i in folder_list:
    a = os.listdir(folder_1+'/'+i)
    for j in os.listdir(folder_2):
        if j.endswith('maf') == True:
            b = j.split('-')[1]
            if b in a:
                shutil.move(folder_2+'/'+j,folder_1+'/'+i+'/'+j)
    print(i)

