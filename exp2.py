# exp2.py

# index
class index:
	T = 10
	J = 10
	I = 20

# data
class data:

	# deadline da tarefa i
	DL = (9, 5, 7, 5, 5, 7, 9, 6, 6, 6, 10, 5, 6, 8, 7, 10, 6, 8, 8, 5, )

	# ociosidade da maquina j
	OC = (2, 1, 1, 1, 1, 3, 2, 3, 3, 3, )

	#duracao da tarefa i na maquina j
	DU = (	(3, 3, 2, 3, 2, 2, 2, 2, 3, 2, ),
	(2, 2, 3, 3, 1, 1, 1, 2, 2, 1, ),
	(2, 1, 2, 2, 3, 3, 2, 1, 2, 1, ),
	(2, 2, 2, 2, 2, 1, 2, 2, 3, 2, ),
	(2, 1, 3, 2, 2, 2, 2, 2, 1, 1, ),
	(2, 3, 2, 3, 1, 3, 3, 1, 3, 3, ),
	(2, 2, 3, 1, 2, 2, 3, 3, 1, 2, ),
	(2, 2, 3, 3, 1, 2, 2, 2, 2, 3, ),
	(3, 2, 3, 3, 3, 3, 3, 1, 2, 3, ),
	(2, 3, 2, 3, 1, 3, 3, 2, 2, 3, ),
	(1, 1, 1, 2, 3, 3, 1, 1, 2, 3, ),
	(3, 1, 2, 2, 2, 2, 3, 1, 3, 1, ),
	(3, 3, 3, 2, 3, 1, 1, 1, 3, 3, ),
	(1, 3, 3, 1, 3, 3, 2, 2, 3, 1, ),
	(3, 3, 3, 1, 1, 1, 2, 3, 1, 2, ),
	(2, 3, 2, 2, 2, 2, 3, 3, 2, 1, ),
	(2, 3, 2, 2, 1, 3, 2, 1, 3, 2, ),
	(2, 1, 3, 2, 1, 2, 2, 2, 2, 1, ),
	(2, 1, 1, 1, 1, 3, 3, 2, 2, 2, ),
	(1, 1, 2, 3, 3, 3, 3, 2, 3, 1, ),
	)

	#se a tarefa i pode ser executada na maquina j
	PO = (	(1, 1, 1, 0, 0, 0, 1, 0, 1, 1, ),
	(0, 1, 0, 0, 0, 0, 0, 0, 1, 1, ),
	(1, 0, 0, 0, 0, 1, 0, 0, 1, 1, ),
	(1, 1, 0, 0, 1, 1, 0, 0, 0, 0, ),
	(1, 0, 0, 0, 1, 0, 1, 0, 0, 0, ),
	(0, 0, 0, 1, 0, 0, 1, 0, 1, 0, ),
	(1, 0, 0, 0, 0, 1, 0, 1, 0, 1, ),
	(0, 1, 1, 0, 0, 1, 1, 0, 0, 1, ),
	(1, 1, 1, 0, 0, 0, 0, 1, 0, 0, ),
	(0, 0, 0, 1, 1, 0, 1, 0, 1, 0, ),
	(1, 0, 1, 0, 1, 0, 0, 1, 1, 0, ),
	(1, 0, 0, 1, 0, 1, 0, 0, 1, 0, ),
	(1, 1, 1, 1, 0, 0, 0, 0, 1, 0, ),
	(1, 0, 1, 1, 1, 0, 0, 0, 0, 0, ),
	(1, 0, 0, 0, 0, 0, 1, 0, 0, 1, ),
	(0, 0, 0, 1, 1, 1, 1, 0, 0, 1, ),
	(1, 1, 1, 0, 1, 0, 1, 0, 0, 1, ),
	(1, 1, 0, 0, 1, 0, 0, 0, 1, 1, ),
	(0, 0, 1, 0, 0, 1, 1, 0, 0, 1, ),
	(0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ),
	)