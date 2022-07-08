# Como é executado o simulador

## Cenários e Pulsos


O simulador trabalha com pulsos migracionais ao longo do tempo. Para este modelo, utilizamos três populações(**P**, **Q** e **R**) que coexistem e interagem entre si ao longo de 20 gerações, sendo a geração 20 a **mais antiga** e geração 1 a **mais recente**. Teremos três pulsos migracionais, no qual cada um deles acontecerá durante três gerações. As gerações escolhidas foram: 4, 5 e 6 (Pulso Recente); 10, 11 e 12 (Pulso Intermediário); 18, 19 e 20 (Pulso Antigo). Dessa maneira é possível indicar em qual das gerações acontecerá um maior fluxo migracional e quanto cada uma das três populações irá contribuir. 

![imagem_pulso](https://github.com/lcsfaria/Imagens/blob/9553f288ad1f7d03ececa93b9c5eca9bcecda7b0/figura_pulsos.png)

Nos exemplos, foi escolhida a População Q para ser aquela que terá a sua contribuição variada ao longo dos pulsos. Além disso, definimos a geração 21, denomida como **Fundadora**, pois apenas uma das populações existirá naquele momento, no caso, a Populção P será a fundadora. Assim, criamos sete cenários nos quais a variações de Q vão ocorrendo ao longo do tempo e com pesos diferentes.

![tabela_cenarios](https://github.com/lcsfaria/Imagens/blob/210bd44e56a8b57f7629c5221a39214f6e481a48/tabelas_cenarios.png)

Cenário I, a população Q terá um fluxo migracional de 0.8 durantes as Gerações 18, 19 e 20. Em contrapartida, temos o Cenário VI, com a população Q contribuindo com um peso de 0.4 nas gerações 4, 5 e 6. Ou seja, um fluxo antigo e um fluxo recente, respectivamentes. O Cenário VII é onde todos as populações contribuirão com os mesmos pesos. 




## Para executar o Cenário I usamos o seguinte comando:

> python3 multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.8 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773

No qual os parâmetros(flags) são:
````
-m: probabilidade de migração ou peso de contribuição de cada população
-s: identificação da população de origem da migração
-T: gerações em que ocorrem os pulsos
-q: quantidade de cromossomos 
-c: número do cromossomo. Vemos o cromossomo 1 no exemplo
-N: número efetivo de indivíduos diplóides na população
-r: distância de recombinação em morgans
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

As  flags -m,-s e -T estão correlacionadas da seguinte maneira: o primeiro valor de -m (0.1) está relacionado com o primeiro valor de -s (P) e com o primeiro valor de -T (4). O mesmo acontece para os outros valores. É importante observar que a Geração 21 deve ser passada nos parâmetros sendo referente a populaçao P e com peso 1.0.

![tabela_flags](https://github.com/lcsfaria/Imagens/blob/main/cenarioa_1.png)

Para os demais cenários teremos as seguintes linhas de comandos:

### Cenário II
> python3 multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.8 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
![cenario_2](https://github.com/lcsfaria/Imagens/blob/main/cenario_2.png)

### Cenário III
>python3 multiple_pulses.py -m 0.1 0.8 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
![cenario_3](https://github.com/lcsfaria/Imagens/blob/main/cenario_3.png)

### Cenário IV
> python3 multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.4 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
![cenario_4](https://github.com/lcsfaria/Imagens/blob/main/cenario_4.png)

### Cenário V
> python3 multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.4 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
![cenario_5](https://github.com/lcsfaria/Imagens/blob/main/cenario_5.png)

### Cenário VI
> python3 multiple_pulses.py -m 0.1 0.4 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
![cenario_6](https://github.com/lcsfaria/Imagens/blob/main/cenario_6.png)

### Cenário VII 
>python3 multiple_pulses.py -m 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1 -s P Q R P Q R P Q R P -T 4 5 6 11 12 13 18 19 20 21 -q 2000 -c 1 -N 10000 -r 2.84249773
![cenario_7](https://github.com/lcsfaria/Imagens/blob/main/cenarssio_7.png)


# Referências

KEHDY, Fernanda S. G. et al. Origin and dynamics of admixture in Brazilians and its effect on the pattern of deleterious mutations. Proceedings Of The National Academy Of Sciences, v. 112, n. 28, p. 8696-8701, 2015.

LIANG, M.; NIELSEN, R. The Lengths of Admixture Tracts. Genetics, v. 197, n. 3, p. 953-967, 2014.
