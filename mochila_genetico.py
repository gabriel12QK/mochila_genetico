import random
import copy
import math
from matplotlib import pyplot as plt
import numpy as np
def one_point_cross_over(padres, mut_fact):
    # Nodos = list(N.get_nodes())
    #Se elige un punto de corte aleatorio:
    pc = random.sample( range(math.floor(len(padres[0])/2)),1)[0]
    hijo1=padres[0][:pc] + padres[1][pc:] 
    hijo2=padres[1][:pc] + padres[0][pc:] 
    #return [mutacion_extrema(hijo1,mut_fact),mutacion_extrema(hijo2,mut_fact)]
    #return [mutacion_extrema(hijo1,mut_fact),mutacion_extrema(hijo2,mut_fact)]
    #print([mutacion_extrema(hijo1,mut_fact), mutacion_extrema(hijo2,mut_fact)])
    return [mutacion_extrema(hijo1,mut_fact), mutacion_extrema(hijo2,mut_fact)]
    
def cross_over_1(poblacion,mut_fact):
    #Definimos en una variable la copia de la población para ir eliminando los padres seleccionados
    poblacion_copia = copy.deepcopy(poblacion)

    #Definimos en una variable la copia de la población para ir añadiendo los hijos creados
    poblacion_final = copy.deepcopy(poblacion)
    while len(poblacion_copia) > 1:  #Iteramos mientras haya padres disponibles
        #Seleccionamos dos padres al azar
        padre1,padre2 = random.sample(poblacion_copia   ,2)
        hijo1,hijo2 = one_point_cross_over([padre1,padre2],mut_fact)
        #print(,"numhijo",hijo1,hijo2)
        if (hijo1 not in poblacion_final and  hijo2 not in poblacion_final):
            poblacion_copia.remove(padre1)
            poblacion_copia.remove(padre2)
            poblacion_final.extend([hijo1,hijo2])
    #print(poblacion_final)
    return poblacion_final

def cross_over_3(poblacion,mut_fact):
    #Definimos en una variable la copia de la población para ir eliminando los padres seleccionados
    poblacion_copia = copy.deepcopy(poblacion)

    #Definimos en una variable la copia de la población para ir añadiendo los hijos creados
    poblacion_final = copy.deepcopy(poblacion)

    while len(poblacion_copia) > 1:  #Iteramos mientras haya padres disponibles
        #Seleccionamos dos padres
        padre1,padre2 = random.sample(poblacion_copia   ,2)
        hijo1,hijo2 = three_point_cross_over([padre1,padre2],mut_fact)
        if (hijo1 not in poblacion_final and  hijo2 not in poblacion_final):
            poblacion_copia.remove(padre1)
            poblacion_copia.remove(padre2)
            poblacion_final.extend([hijo1,hijo2])
    return poblacion_final

def three_point_cross_over(padres, mut_fact, k=3):
    # Nodos = list(problem.get_nodes())
    #Se elige un punto de corte aleatorio:
    while True:
        pc = sorted(random.sample(range(3,len(poblacion[0])-3),k))
        if(pc[2]-pc[1]) > 7 and (pc[1]-pc[0]) > 7:
            break                                    
    hijo1 =  padres[0][:pc[0]] + padres[1][pc[0]:pc[1]] + padres[0][pc[1]:pc[2]] + padres[1][pc[2]:] 
    hijo2 =  padres[1][:pc[0]] + padres[0][pc[0]:pc[1]] + padres[1][pc[1]:pc[2]] + padres[0][pc[2]:] 
    return [mutacion_extrema(hijo1,mut_fact), mutacion_extrema(hijo2,mut_fact)]
    #return [local_search_2_opt(mutacion(hijo1,mut_fact),problem),local_s

def cross_over_4(poblacion,mut_fact):
    #Definimos en una variable la copia de la población para ir eliminando los padres seleccionados
    # poblacion_copia = copy.deepcopy(poblacion)

    #Definimos en una variable la copia de la población para ir añadiendo los hijos creados
    poblacion_final = copy.deepcopy(poblacion)

    for i in range(round(len(poblacion)/2)):  #Iteramos mientras haya padres disponibles
        #Seleccionamos dos padres al azar
        # padre1,padre2 = random.sample(poblacion_copia, 2)
        #Seleccion por torneo
        padre1 = seleccionTorneo(poblacion, 20)
        while True:
          padre2 = seleccionTorneo(poblacion, 10)
          if padre1!=padre2:
            break
        #hijo1,hijo2 = k_point_cross_over([padre1,padre2],problem,mut_fact)
        hijo1,hijo2 = four_point_cross_over([padre1,padre2],mut_fact)
        if (hijo1 not in poblacion_final and  hijo2 not in poblacion_final):
            # poblacion_copia.remove(padre1)
            # poblacion_copia.remove(padre2)
            poblacion_final.extend([hijo1,hijo2])
    return poblacion_final

def four_point_cross_over(padres, mut_fact, k=4):
    
    #Se elige un punto de corte aleatorio:
    while True:
        pc = sorted(random.sample(range(3,len(poblacion[0])-3),k))
        if (pc[3]-pc[2]) > 4 and (pc[2]-pc[1]) > 4 and (pc[1]-pc[0]) > 4:
            break                                    
    hijo1 =  padres[0][:pc[0]] + padres[1][pc[0]:pc[1]] + padres[0][pc[1]:pc[2]] + padres[1][pc[2]:pc[3]] + padres[0][pc[3]:] 
    hijo2 =  padres[1][:pc[0]] + padres[0][pc[0]:pc[1]] + padres[1][pc[1]:pc[2]] + padres[0][pc[2]:pc[3]] + padres[1][pc[3]:] 
    #return [mutacion_extrema(hijo1,mut_fact), mutacion_extrema(hijo2,mut_fact)]
    return [mutacion_extrema(hijo1,mut_fact), mutacion_extrema(hijo2,mut_fact)]



def cross_over_5(poblacion,mut_fact):
    #Definimos en una variable la copia de la población para ir eliminando los padres seleccionados
    poblacion_copia = copy.deepcopy(poblacion)

    #Definimos en una variable la copia de la población para ir añadiendo los hijos creados
    poblacion_final = []
    cont=0
    while cont <= len(poblacion)/2:  #Iteramos mientras haya padres disponibles
        cont+=1
        #Seleccionamos dos padres
        # padre1,padre2 = random.sample(poblacion_copia   ,2)
        # padre1 = seleccionTorneo(poblacion_copia, 5)
        # padre2 = seleccionTorneo(poblacion_copia, 5)
        while True:
          padre1,padre2 = random.sample(poblacion_copia   ,2)
          if padre1!=padre2:
            break
        hijo1,hijo2 = five_point_cross_over([padre1,padre2],mut_fact)
        poblacion_final.extend([hijo1,hijo2])
        # if (hijo1 not in poblacion_final and  hijo2 not in poblacion_final):
        #     poblacion_copia.remove(padre1)
        #     poblacion_copia.remove(padre2)
        #     poblacion_final.extend([hijo1,hijo2])
    return poblacion_final

def five_point_cross_over(padres, mut_fact, k=5):
    #Se elige un punto de corte aleatorio:
    while True:
        pc = sorted(random.sample(range(3,len(poblacion[0])-3),k))
        if (pc[4]+pc[3]) > 4 and (pc[3]+pc[2]) > 4 and (pc[2]+pc[1]) > 4 and (pc[1]+pc[0]) > 4:
            break                                    
    hijo1 =  padres[0][:pc[0]] + padres[1][pc[0]:pc[1]] + padres[0][pc[1]:pc[2]] + padres[1][pc[2]:pc[3]] + padres[0][pc[3]:pc[4]] + padres[1][pc[4]:]
    hijo2 =  padres[1][:pc[0]] + padres[0][pc[0]:pc[1]] + padres[1][pc[1]:pc[2]] + padres[0][pc[2]:pc[3]] + padres[1][pc[3]:pc[4]] + padres[0][pc[4]:]
    #return [mutacion_extrema(hijo1,mut_fact), mutacion_extrema(hijo2,mut_fact)]
    return [mutacion_extrema(hijo1,mut_fact), mutacion_extrema(hijo2,mut_fact)]



##Seleccion por Torneo

def seleccionTorneo(poblacionInicial, porcentaje):
    nTorneo = round((len(poblacionInicial) * porcentaje)/100)
    size_poblacion = len(poblacionInicial)
    parents = np.random.choice(size_poblacion, nTorneo)
    fo = 0
    index = 0
    for i in parents:
      _fo = funcionDeCalidad(poblacionInicial[i], pesos,valores,peso_maximo)
      if _fo < fo:
        fo = _fo
        index = i
    return poblacionInicial[index]

##Mutaciones


def mutacion(hijo, mut_fact):
    if random.random() <= mut_fact:
        gen1,gen2 = sorted(random.sample(range(len(hijo)),2))
        aux = hijo[gen1]
        hijo[gen1] = hijo[gen2]
        hijo[gen2] = aux
        return hijo
    else:
        return hijo[::] 
    
def mutacion_extrema(hijo, mut_fact):
    for i in range(len(hijo)):
        if random.random() <= mut_fact:
            gen = random.choice(list(set(range(len(hijo)))-{i}))
            aux = hijo[i]
            hijo[i] = hijo[gen]
            hijo[gen] = aux
    return hijo 

##Funcion de calidad

def funcionDeCalidad(_individuo,pesos,valores,peso_maximo):
  tamaño = len(_individuo)
  #print(valores)
  peso=0
  valor=0
  i=0
  for indice in _individuo:
      if indice==1:
         peso +=pesos[i] #sumamos el total de peso de la solucion
         valor +=valores[i]
      i+=1
  if peso > peso_maximo:
     return-1
  else:
      #print(valor)
      return valor

##Remplazo

def reemplazo(poblacion, fact_elit,pesos,valores,peso_maximo, n_de_items):
  #Se ordena la población según el fitness(tamaño del recorrido) en una lista de elementos [distancia, solucion]
  poblacion_ordenada = sorted([ [funcionDeCalidad(_individuo,pesos,valores,peso_maximo), _individuo] for _individuo in poblacion ], key= lambda x:x[0], reverse=True )

  #Devolvemos elitismo% y el resto se eligen aleatoriamente
  return [x[1] for x in poblacion_ordenada][:int(n_de_items*fact_elit)]  + \
  random.sample([x[1] for x in poblacion_ordenada][int(n_de_items*fact_elit):] , int(n_de_items*(1-fact_elit))  ) 

##Poblacion inicial

def poblacionInicial(n_de_individuos, n_de_itens):
    """"Crear la población"""
    return [ individuo(n_de_itens) for x in range(n_de_individuos) ]

def individuo(n_de_itens):
    """Crear un miembro de la población"""
    return [ random.getrandbits(1) for x in range(n_de_itens) ]#genera distintas soluciones

##Calcula la media de peso de la mochila

def media_fitness(poblacion, peso_maximo, pesos,valores): #solo tiene en cuenta los elementos que respetan el peso máximo de la mochila
    """Encuentra el valor medio de la poblacion"""
    if((funcionDeCalidad(x, pesos,valores,peso_maximo) for x in poblacion if funcionDeCalidad(x,pesos,valores,peso_maximo) > 0)):
      summed = sum(funcionDeCalidad(x, pesos,valores,peso_maximo) for x in poblacion if funcionDeCalidad(x,pesos,valores,peso_maximo) > 0)
    return summed / (len(poblacion) * 1.0)

##Funcion para calcular el fitnnes de las soluciones


def fitness(poblacion, peso_maximo, pesos, valores):
    #print(individuo)
    """Evaluar al individuo"""
    peso_total, valor_total = 0, 0
    solucion=[]
    for indice in poblacion:#recorremos nuestras soluciones
        peso = sum([pesos[i] for i in range(len(indice)) if indice[i] == 1])#sumamos el total de peso de la solucion
        valor = sum([valores[i] for i in range(len(indice)) if indice[i] == 1])#sumamos el total de valor de nuestra solucion
        if peso < peso_maximo:#evaluamos que no exeda nuestra restriccion
           if valor > valor_total:#verificamos el mayor valor de las soluciones validas
              valor_total=valor
              peso_total=peso
              solucion=indice
    return valor_total,peso_total,solucion
    # if (peso_maximo > peso_total) :
    #     return valor_total # devuelve -1 en caso que exceda el peso
    # print("Solucion:", individuo,"Peso:", peso_total, "Valor:", valor_total)
     #si es un individuo válido, devuelve su valor

#pesos_e_valores = [[4, 30], [8, 10], [8, 30], [25, 75], [2, 10], [50, 100], [6, 300], [20, 70],[100, 400], [100, 250],[4, 30], [8, 10], [8, 30], [25, 75], [2, 10], [120, 120], [6, 300], [12, 50],[100, 200], [8, 300]]
pesos =   [485,	94,	326,	506,	248,	416,	421,	992,	322,	649,	795,	237,	43,	457,	845,	815,	955,	446,	252,	422,	9,	791,	901,	359,	122,	667,	94,	598,	738,	7,	574,	544,	715,	334,	882,	766,	367,	994,	984,	893,	299,	633,	433,	131,	682,	428,	72,	700,	874,	617,	138,	874,	856,	720,	145,	419,	995,	794,	529,	196,	199,	997,	277, 116, 97,	908, 719, 539, 242, 707, 107, 569, 122, 537, 70,	931, 98, 726, 600, 487, 645, 772, 267, 513, 972, 81,	895, 943, 213, 58, 748, 303, 487, 764, 923, 536, 29, 724, 674, 789]
valores = [585,	194,	426,	606,	348,	516,	521,	1092,	422,	749,	895,	337,	143,	557,	945,	915,	1055,	546,	352,	522,	109,	891,	1001,	459,	222,	767,	194,	698,	838,	107,	674,	644,	815,	434,	982,	866,	467,	1094,	1084,	993,	399,	733,	533,	231,	782,	528,	172,	800,	974,	717,	238,	974,	956,	820,	245,	519,	1095,	894,	629,	296,	299,	1097,	377,	216,	197,	1008,	819,	639,	342,	807,	207,	669,	222,	637,	170,	1031,	198,	826,	700,	587,	745,	872,	367,	613,	1072,	181,	995,	1043,	313,	158,	848,	403,	587,	864,	1023,	636,	129,	824,	774,	889]
peso_maximo = 40000
numero_poblacion = 150
generaciones = 1000
mut_fact=.08
fact_elit=1
historico_de_fitness=[]
aux=[]

n_de_items = len(pesos) #Analogo aos pesos e valores
poblacion = poblacionInicial(numero_poblacion, n_de_items)#creo mi poblacion inicial
historico_de_fitness=[media_fitness(poblacion, peso_maximo, pesos,valores)]
(valorInicial,pesoInicial,mejorSolucion)=fitness(poblacion, peso_maximo, pesos, valores)#evaluo la mejor solucion de mi poblacion inicial
print("Mejor solucion incial:",mejorSolucion,"\nValor:",valorInicial,"Peso;",pesoInicial)

for i in range(generaciones):
    poblacion = cross_over_3(poblacion , mut_fact)
   
    poblacion = reemplazo(poblacion, fact_elit,pesos,valores,peso_maximo,n_de_items)
    historico_de_fitness.append(media_fitness(poblacion, peso_maximo, pesos,valores))
    (mejor_val,mejor_peso,mejorsol)=fitness(poblacion, peso_maximo, pesos, valores)
    print("Generacion",i,"Mejor solucion:",mejorsol,"\nValor:",mejor_val,"Peso;",mejor_peso)
    aux.append(mejorsol)
print("\n\n\nMejor Resultado dentro de las ",generaciones," generaciones")  
(valor,peso,solucion)=fitness(aux, peso_maximo, pesos, valores)
print("Mejor solucion encontrada:",solucion,"\nValor:",valor,"Peso:",peso)
for indice,dados in enumerate(historico_de_fitness):
   print ("Generacion: ", indice," | Media de valorn en la mochila: ", dados)

plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema de la mochila")
plt.xlabel("Generacion")
plt.ylabel("valor medio de la mochila")
plt.show()
   