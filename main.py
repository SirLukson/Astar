import numpy as np
import graphOpen
import math


def euklides(a1, b1, a2, b2):       #funkcja obliczająca odległość euklidesową
    return math.sqrt(math.pow(a2 - a1, 2) + math.pow(b2 - b1, 2))


def Neighbors(num):                 #funkcja definiująca sąsiadów dla danego wierzcholka
    mate = []
    for i in range(len(graphOpen.nmatrix)+1):
        if (graphOpen.neibh[num-1][i]) != 0:
            mate.append(i+1)
    return mate


def Route():                        #funcja podająca trasę punkt po punkcie
    global keys
    route = []
    routeStr = ''
    z = int(graphOpen.goal)
    values = [r for r in closeNodes.values()]
    keys = [r for r in closeNodes.keys()]
    if not (int(graphOpen.goal) in keys):
        routeStr = 'Nie znaleziono trasy'
    else:
        for i in keys:
            if z == int(graphOpen.start): break
            route.append(z)
            z = values[keys.index(z)]
        route.append(graphOpen.start)
        route.reverse()
        for item in route:
            routeStr = routeStr + str(item) + ' '
    print('Trasa: ')
    return print(routeStr)





def AStar():                        #funkcja implementująca algorytm A*
    global closeNodes
    heur = []
    h = 0

    name = input("Wprowadź nazwe pliku: ")  #wprowadzanie nazwy pliku np. 2.txt
    graphOpen.OpenTxt(name)                 #odwołanie do funkcji zajmujacej sie wczytaniem danych z pliku

    while (h < (len(graphOpen.a))):         #obliczanie heurystyki z uzyciem funkcji euklides
        heur.append(euklides(int(graphOpen.a[h]), int(graphOpen.b[h]), int(graphOpen.a[int(graphOpen.goal)-1]), int(graphOpen.b[int(graphOpen.goal)-1])))
        h += 1

    currentCost = {}               #aktualny koszt
    currentNode = graphOpen.start  #aktualnie rozpatrywany wierzcholek = start
    closeNodes = {}                #zmienna dict zawierajaca wierzcholki juz przejrzane
    openNode = [graphOpen.start]   #zmienna list zawierajaca wierzcholki rozpatrywane
    path = {}                      #droga g
    cost = {}                      #koszt trasy f
    path2 = 0                      #zmienna pomocnicza
    for i in range(len(graphOpen.a)):
        path[i + 1] = np.inf
        cost[i + 1] = np.inf
    path[graphOpen.start] = 0
    cost[graphOpen.start] = heur[graphOpen.start - 1]

    while openNode != []:
        for i in openNode:
            currentCost[i] = cost[i]
        CC_keys = list(currentCost.keys())          #lista kluczy z currentCost
        CC_values = list(currentCost.values())      #lista wartosci z currentCost
        minimal = min(currentCost.values())         #minimalna wartosc z currentCost.values
        currentNode = CC_keys[CC_values.index(minimal)]     #aktualny punkt = indeks przypisany do minimalnej wartosci
        currentCost = {}                                    #zmienna dict aktualnego kosztu
        openNode.remove(currentNode)                        #usunięcia z rozpatrywanych wierzcholków aktualnego wierzcholka
        if currentNode == int(graphOpen.goal):              #jeśli aktualny wierzcholek jest wierzcholkiem koncowym to zakoncz program i wyzeruj rozpatrywane
            openNode = []
            print(f'f: {cost[int(graphOpen.goal)]}')
            break
        else:                                               #jeśli program sie nie zakonczyl to sprawdz sasiadów punktu
            for i in Neighbors(currentNode):
                path2 = (path[currentNode]) + (graphOpen.neibh[currentNode - 1][i - 1])
                if path2 < path[i]:
                    path[i] = path2
                    closeNodes[i] = currentNode
                    cost[i] = path[i] + heur[i - 1]
                    if not i in openNode:
                        openNode.append(i)
    Route()
    return ()
AStar()
