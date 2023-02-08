#Punto 1
def coeficientes(q: np.array)->np.array:
    rta = np.empty((0,0), float)
    #Revisa si Q es cuadrada
    if len(q) != len(q[0]):
        return ('No es nxn, por lo que no es posible determinar los coeficientes de su forma cuadrática')
    else:
        #Recorre las filas
        for i in range(len(q)):
            #Para las posiciones i,i se agregan los coeficientes al arreglo final
            rta = np.append(rta,q[i,i]) 
        for i in range(len(q)):
            #Recorre las columnas
            for j in range(len(q[0])):
                #Si la columna es mayor, se suman las dos posiciones (fila, columna + columna,fila) para encontrar el coeficiente
                if j>i:
                    rta = np.append(rta,(q[i,j]+q[j,i]))
    return rta
# Punto 2
# Revisar si la matriz es simetrica
def es_simetrica(q: np.array)->bool:
    a = np.transpose(q)
    if np.array_equal(a,q) == True:
        return True
    else:
        return False
#Encontrar la forma simétrica
def forma_simetrica(q:np.array)->np.array:
    rta = np.empty((0,0), float)
    if es_simetrica(q)==True:
        rta = q
    else:
        rta = 0.5*(q.dot(np.transpose(q)))
    return rta