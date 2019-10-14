import random

T = 10
J = 10
I = 20


f = open("exp2.py", "w")

f.write('# exp2.py\n\n')

#class Index
f.write('# index\n')
f.write('class index:\n')
f.write('\tT = '+ str(T) + "\n")
f.write('\tJ = '+ str(J) + "\n")
f.write('\tI = '+ str(I) + "\n")
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
f.write('\t)')


f.close()