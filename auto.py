#automatiza os comandos para cada cenario, fazendo com que cada linha referente a um cenario seja executada quantas vezes for desejada
# python3 auto.py parametro1.txt 50 -> irá executar o parametro1 (cenario1) 50 vezes.
  

import os
import sys
import time

ini = time.time()
print('Iniciando...')
print()
print('Comecou em',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print()

file =  sys.argv[1]
quantidade = sys.argv[2]
quantidade = int(quantidade)

modelo = file[-5]

comando = [line.rstrip() for line in open(file)]

folder = 'mkdir M'+str(modelo)
os.system(folder)


for i in range(0,quantidade):

    final = comando[0]+' >M'+str(modelo)+'/'+'Test'+str(i)+'.txt'

    os.system(final)
    print(f'Test{i} pronto.')

end = time.time()
print()
print('Terminou em',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print('-------------------------------------------------------------------')
print('O processo demorou',round(end-ini,3),'segundos.')
print()
print('O processo demorou',round((end-ini)/60,3),'minutos.')
print('-------------------------------------------------------------------')
