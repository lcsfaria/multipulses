# le todos os .txt de uma pasta e os junta de um arquivo só

import pandas as pd
import glob

read_files = glob.glob("C:\\Users\\faria\\Desktop\\M1\\*.txt")

with open("C:\\Users\\faria\\Desktop\\result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

            
data = pd.read_csv("C:\\Users\\faria\\Desktop\\result.txt", sep='\t',names=['Pop', 'Len.Tract','id','Chr'])

dataQ= data.loc[data['Pop']=='Q']


dataQ['Len.Tract'].mean()
dataQ['Len.Tract'].max()
dataQ['Len.Tract'].min()

## Para cada arquivo na pasta, ele le o seu conteudo 

import pandas as pd
import glob

read_files = glob.glob("C:\\Users\\faria\\Desktop\\M1\\*.txt")

for i in read_files:
    print(i)
    data = pd.read_csv(i,sep = '\t', names=['Pop', 'Len.Tract','id','Chr'])
    mini = data.loc[data['Len.Tract']==0]
    print(mini)
    print()

 
