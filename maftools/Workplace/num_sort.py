import os
import subprocess

pwd = os.getcwd()
folder_list = pwd+'/Num_sorted'

for i in os.listdir(folder_list):
    print(i)
    os.chdir(folder_list+'/'+i+'/maf')
    os.system('cat *.maf >> {0}.maf'.format(i))
    os.system('mv {0}.maf ~/kjh/Num_maf'.format(i))
os.chdir(pwd+'/Num_maf')

