# exp2.py

# index
class index:
	T = 30
	J = 6
	I = 10
	S = 0
	F = 30

# data
class data:

	# deadline da tarefa i
	DL = (18, 24, 24, 29, 15, 15, 29, 22, 29, 28, )

	# ociosidade da maquina j
	OC = (9, 5, 5, 5, 2, 4, )

	#duracao da tarefa i na maquina j
	DU = (	(3, 3, 2, 5, 7, 7, ),
	(2, 1, 4, 5, 2, 9, ),
	(3, 1, 5, 7, 2, 2, ),
	(4, 8, 8, 3, 5, 4, ),
	(1, 2, 2, 3, 7, 1, ),
	(9, 6, 8, 8, 8, 9, ),
	(6, 7, 7, 4, 3, 7, ),
	(8, 7, 9, 4, 9, 10, ),
	(4, 8, 10, 1, 5, 5, ),
	(1, 2, 7, 7, 5, 6, ),
	)

	#se a tarefa i pode ser executada na maquina j
	PO = (	(1, 0, 1, 0, 0, 0, ),
	(0, 1, 0, 1, 1, 0, ),
	(0, 0, 0, 1, 1, 0, ),
	(1, 1, 1, 1, 1, 0, ),
	(1, 1, 1, 1, 1, 1, ),
	(0, 1, 0, 1, 1, 0, ),
	(0, 1, 1, 1, 0, 0, ),
	(1, 0, 1, 0, 1, 0, ),
	(0, 0, 1, 0, 1, 0, ),
	(0, 1, 1, 0, 1, 0, ),
	)

	#disponivilidade a maquina j no tempo t
	DS = (	(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, ),
	(0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, ),
	)

	#dependencia da tarefa i' da tarefa i"
	DE = (	(0, 0, 0, 0, 0, 0, 0, 1, 1, 1, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ),
	)