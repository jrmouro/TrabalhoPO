# exp2.py

# index
class index:
	T = 3
	J = 2
	I = 3
	S = 0
	F = 3

# data
class data:

	# deadline da tarefa i
	DL = (2, 2, 2, )

	# ociosidade da maquina j
	OC = (0, 0, )

	#duracao da tarefa i na maquina j
	DU = (	(1, 1, ),
	(1, 1, ),
	(1, 1, ),
	)

	#se a tarefa i pode ser executada na maquina j
	PO = (	(1, 1, ),
	(1, 1, ),
	(1, 1, ),
	)

	#disponivilidade a maquina j no tempo t
	DS = (	(0, 0, 0, ),
	(0, 0, 0, ),
	)

	#dependencia temporal da tarefa i' da tarefa i"
	DE = (	(0, 1, 2, ),
	(0, 0, 0, ),
	(0, 0, 0, ),
	)