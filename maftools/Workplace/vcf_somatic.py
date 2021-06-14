import os
import pandas as pd 

inp = '/BiO/Research/maftools/0.Rawdata/'
out = '/BiO/Research/maftools/1.Somatic/'


file_list = os.listdir(inp)


for num in range(55):
    for j in file_list:
        if j.startswith(str(num)):
