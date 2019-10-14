import exp2 as exp



from gurobipy import *
try:
    # Create a new model
    m = Model("task scheduler")

    # Se a tarefa i inicia no tempo t na máquina j
    x = m.addVars(exp.index.J, exp.index.I, exp.index.T, vtype=GRB.BINARY, name="x")

    # Set objective
    #go = (x[j,i,t]*(exp.data.DL[i] - t - exp.data.DU[i][j]) 
    go = (x[j,i,t]*(exp.data.DL[i] - t - exp.data.DU[i][j])
    for j in range(exp.index.J) 
    for i in range(exp.index.I) 
    for t in range(exp.index.T))
    
    m.setObjective(sum(go), GRB.MAXIMIZE)

    

    #Add constraints
    # Se a tatefa i pode ser executada na máquina j
    for t in range(exp.index.T):

        g = (exp.data.PO[i][j] - x[j,i,t] >= 0
        for j in range(exp.index.J) 
        for i in range(exp.index.I))
        
        m.addConstrs(g, "c0." + str(t))

    # A tarefa i só pode iniciar no tempo t se não há outra tareja em andamento na maquina j naquele momento
    for j in range(exp.index.J):
        for t in range(exp.index.T):
            g1 = (x[j,i,t] for i in range(exp.index.I))
            g2 = (x[j,i,tt] for i in range(exp.index.I) for tt in range(exp.index.T ) if tt < t if tt + exp.data.DU[i][j] > t)
                        
                        
            m.addConstr(sum(g1) + sum(g2) <= 1, "c1")
        

        

                

    # a tarefa i deve começar no tempo t > que a ociosidade da máquina j
    for t in range(exp.index.T):

        g = (x[j,i,t]*(t - exp.data.OC[j]) >= 0
        for j in range(exp.index.J) 
        for i in range(exp.index.I))
        
        m.addConstrs(g, "c2." + str(t))

    # a tarefa i deve ser executada uma única vez
    for i in range(exp.index.I):

        g = (x[j,i,t]
        for j in range(exp.index.J) 
        for t in range(exp.index.T))
        
        m.addConstr(sum(g) == 1, "c3." + str(i))

    

    m.optimize()

    print("\n")

    print("Tar\tMaq\tIni\tFim\tDur\tDea\tSum")

    for i in range(exp.index.I):
        aj = 0
        at = 0
        du = 0
        for j in range(exp.index.J):
            for t in range(exp.index.T):
                if x[j,i,t].x > 0:
                    aj = j
                    at = t
                    du = exp.data.DU[i][j]

        print(str(i) + "\t" 
        + str(aj) + "\t" 
        + str(at) + "\t" 
        + str(at + du) + "\t" 
        + str(du) + "\t" 
        + str(exp.data.DL[i]) + "\t" 
        + str(exp.data.DL[i]-at - du))



    
    #m.write("saida.lp")

    print('Obj: ' , m.objVal)

except GurobiError:
    print('Error reported')


