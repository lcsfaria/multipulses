# multipulses

# Cenários e Pulsos

O simulador trabalha com pulsos migracionais ao longo das geraçoes. Para este modelo, foi definida uma população do tipo trí-hibrida, ou seja, os tracts de ancestralidade tem origem em três grandes populações, nas quais foram chamadas de **P**, **Q** e **R**. Para isso, distribuimos essas populções coexitindo ao longo de 20 gerações, sendo a Geração 20 a **mais antiga** e Geração 1 a **mais recente**. Além disso, definmos a geração 21, denomida como **Fundadora**, pois apenas uma das populações existirá naquele momento, no caso, a Populção P será a fundadora.

Para esse modelo, teremos três pulsos migracionais, no qual cada pulso migracional acontecerá durante três gerações. As gerações escolhidas foram: 4, 5 e 6 (Pulso Recente); 10, 11 e 12 (Pulso Intermediário); 18, 19 e 12 (Pulso Antigo). 

Os cenários foram divido

![imagem_pulso](https://github.com/lcsfaria/Imagens/blob/9553f288ad1f7d03ececa93b9c5eca9bcecda7b0/figura_pulsos.png)

## Para executar o Cenário I usamos o seguinte comando:

> python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.8 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773

No qual os parâmetros(flags) são:
````
-m probabilidade de migração de uma população, o seu peso de contribuição
-s populaçoes
-T gerações em que os pulsos ocorrem
-q quantidade de simualçoes (por se tratar de um modelo diploide, 2000 gerarão 1000 cromossomos simulados
-c número do cromossomo
-N tamanho da população
-r tamanho do cromossomo referência (cM)
````
Para entender melhor o funcionamento deveremos enxergar o código da seguinte maneira:
````
python multiple_pulses.py 
-m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.8 0.1 1 
-s P Q R P Q R P Q R P 
-T 4 5 6 11 12 13 18 19 20 21 
-q 2000 
-c 1 
-N 10000 
-r 2.84249773
````

As  flags -m,-s e -T estão correlacionadas da seguinte maneira: o primeiro valor de -m (0.1) está relacionado com o primeiro valor de -s (P) e com o primeiro valor de -T (4). O mesmo acontece para os outros valores.

![tabela_flags](https://github.com/lcsfaria/Imagens/blob/8f1520f4c6e3fc40f30d0786e9470bd28b27e6b5/tabela_flags.png)

Para os demais cenários teremos as seguintes linhas de comandos:

### Cenário II
> python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.8 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
### Cenário III
>python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.8 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
### Cenário IV
> python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.4 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
### Cenário V
> python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.4 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
### Cenário VI
> python multiple_pulses.py -m 0.1 0.4 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
### Cenário VII
>python multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
