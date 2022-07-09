# roda paramentro a parametro

import os
    

for i in range(1,8):
	n = str(i)
	comando = 'python3 auto.py parametro'+n+'.txt 2'
	os.system(comando)
