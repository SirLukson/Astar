
def OpenTxt(name):
    global a, b, start, goal, nodes, attributes, neibh, nmatrix
    attributes = []
    i = 0
    j = 1
    a = []
    b = []
    start = []
    goal = []
    #wczytanie pliku oraz obróbka znaków
    with open(name, 'r') as graf:
        for line in graf:
            line = line.strip()
            line = line.replace(",", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            attributes.append(list(line.split(",")))

    nodes = str(attributes[0])
    cond = str(attributes[1])
    cond = cond.replace(" ", "")
    cond = cond.replace("[", "")
    cond = cond.replace("]", "")
    cond = cond.replace("'", "")
    nodes = nodes.replace("['", "")
    nodes = nodes.replace("']", "")
    nodes = nodes.replace(" ", "")

    start = int(cond[0])            #wierzcholek start

    while i < (len(nodes)-1):       #pętla przypisująca do zmiennej a wspolrzedne x wierzcholków i do b współrzędne y wierzcholków
        a.append(nodes[i])
        b.append(nodes[i+1])
        i += 2

    while j < len(cond):            #pętla przypisująca zmiennaj goal wartosc mety
        goal.append(cond[j])
        j += 1

    goal = str(goal)
    goal = goal.replace("'", "")
    goal = goal.replace(",", "")
    goal = goal.replace(" ", "")
    goal = goal.replace("[", "")
    goal = goal.replace("]", "")

    print(f'start: {start}')
    print(f'goal: {goal}')
    print(f'wierzcholki a: {a}')
    print(f'wierzcholki b: {b}')

    nmatrix2 = []
    nmatrix = attributes[2:-1]

    for z in range(len(nmatrix)):
        nmatrix1 = str(nmatrix[z])
        nmatrix1 = nmatrix1.replace(" ", ",")
        nmatrix1 = nmatrix1.replace("[", "")
        nmatrix1 = nmatrix1.replace("]", "")
        nmatrix1 = nmatrix1.replace("'", "")
        nmatrix2.append(list(nmatrix1.split(",")))

    neibh = []
    for row in nmatrix2:                            #petla tworzaca macierz sasiedztwa
        neibh.append([float(i) for i in row])




