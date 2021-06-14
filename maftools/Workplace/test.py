import os

fold1 = os.getcwd()+'/Num_maf'
fold2 = os.getcwd()+'/maf_result'
x = []
for i in os.listdir(fold1):
    if i not in os.listdir(fold2):
        x.append(i)
print(x)
print(len(x))
