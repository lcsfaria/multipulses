import pandas as pd

hg17 = pd.read_csv('D:\\Meu\\ambiente\\script\\genetic_map_hg38_withX.txt', sep = ' ')

for i in range(1,23):
    ch = hg17.loc[hg17['chr']==i]
    maxi = max(ch['Genetic_Map(cM)'])
    print(f'chr {i} = {maxi/100}')
