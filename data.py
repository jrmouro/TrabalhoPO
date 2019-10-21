import random

T = 30
J = 6
I = 10
S = 0
F = 30



f = open("exp2.py", "w")

f.write('# exp2.py\n\n')

#class Index
f.write('# index\n')
f.write('class index:\n')
f.write('\tT = '+ str(T) + "\n")
f.write('\tJ = '+ str(J) + "\n")
f.write('\tI = '+ str(I) + "\n")
f.write('\tS = '+ str(S) + "\n")
f.write('\tF = '+ str(F) + "\n")
f.write('\n')


#class Data
f.write('# data\n')
f.write('class data:\n')


#DL
f.write('\n\t# deadline da tarefa i')
s = '\n\tDL = ('
for i in range(I):
    s += str(random.randint(int(T/2),T)) + ', '
f.write(s + ')\n')


#OC
f.write('\n\t# ociosidade da maquina j')
s = '\n\tOC = ('
for j in range(J):
    s += str(random.randint(0,int(T/3))) + ', '

f.write(s + ')\n')

#DU
f.write('\n\t#duracao da tarefa i na maquina j')
f.write('\n\tDU = (')
for i in range(I):
    s = '\t('
    for j in range(J):
        s += str(random.randint(1,int(T/3))) + ', '
    f.write(s + '),\n')
f.write('\t)\n')


#PO
f.write('\n\t#se a tarefa i pode ser executada na maquina j')
f.write('\n\tPO = (')
for i in range(I):
    s = '\t('
    for j in range(J):
        s += str(random.randint(0,1)) + ', '
    f.write(s + '),\n')
f.write('\t)\n')


#DS
f.write('\n\t#disponivilidade a maquina j no tempo t')
f.write('\n\tDS = (')
for j in range(J):
    s = '\t('
    for t in range(S, F):
        a = random.randint(0,6)
        if a > 5:
            s += str(1) + ', '
        else:
            s += str(0) + ', '
    f.write(s + '),\n')
f.write('\t)\n')

#DE
f.write('\n\t#dependencia temporal da tarefa i\' da tarefa i\"')
f.write('\n\tDE = (')
for i in range(I):
    s = '\t('
    for ii in range(I):
        a = random.randint(0,6)
        if a > 5 and ii > i:
            s += str(1) + ', '
        else:
            s += str(0) + ', '
    f.write(s + '),\n')
f.write('\t)')


f.close()