## Gera os arquivos txt que serão usados como imput de multipulses

M1 ='python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.7 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773'
M2 ='python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.8 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773'
M3 ='python multiple_pulses.py -m 0.1 0.8 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773'
M4 ='python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.4 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773'
M5 ='python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.4 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773'
M6 ='python multiple_pulses.py -m 0.1 0.4 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773'
M7 ='python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773'

lista = [M1,M2,M3,M4,M5,M6,M7]
caminhos = []

for i in range(1,8):
    caminh ='C:\\Users\\faria\\Desktop\parametro'+str(i)+'.txt'
    caminhos.append(caminh)

for a,b in zip(lista,caminhos):
    with open(b,'w') as txt:
        txt.write(a)
