import random
import sys
from collections import defaultdict
from timeit import default_timer as timer
from datetime import timedelta

class Graph_M():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]


    def topologicalSortPomoc(self, i, stack, visited):

        visited[i] = True

        for z in range(self.V):
            if self.graph[i][z] == 1:
                if visited[z] == False:
                    self.topologicalSortPomoc(z, stack, visited)

        stack.insert(0, i)


    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortPomoc(i, stack, visited)
        # print(stack)


    def printMST(self, parent):
        print("Edge \tWeight")
        weight = 0
        for i in range(1, self.V):
            weight += self.graph[i][parent[i]]
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
        print(weight)


    def minKey(self, key, mstSet):

        min = 1001

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index


    def primMST(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


    def value_DAG_matrix_generator(self, saturation):  # saturation - value from 0.0-1.0
        for w in range(self.V):
            for c in range(w + 1, self.V):
                value = random.randint(0 - (100 - saturation), saturation)

                if value > 0:
                    value = random.randint(0, 1000)
                    self.graph[w][c] = value
                    self.graph[c][w] = value

        #for i in range(self.V):
            #print(self.graph[i])


    def connect_DAG_matrix_generator(self, saturation):

        for w in range(self.V):
            for c in range(w + 1, self.V):
                value = random.randint(0 - (100 - saturation), saturation)
                up = random.randint(0, 1)  # 1- gorny trojkat w macierzy, 0- dolny trojkat macierzy
                if value > 0 and up == 1:
                    self.graph[w][c] = 1
                elif value > 0 and up == 0:
                    self.graph[c][w] = 1
                    
                    
    def euler_matrix_generator(self, saturation):

        odd = []
        for w in range(self.V):
            for c in range(w + 1, self.V):
                value = random.randint(0 - (100 - saturation), saturation)
                if value > 0:
                    self.graph[w][c] = 1
                    self.graph[c][w] = 1
            if sum(self.graph[w]) % 2 == 1:
                odd.append(w)

        while odd:

            if len(odd)>=2:
                check = False
                for i in range(1,len(odd)):
                    if not self.graph[odd[0]][odd[i]]:
                        self.graph[odd[0]][odd[i]] = 1
                        self.graph[odd[i]][odd[0]] = 1
                        odd.pop(0)
                        odd.pop(i-1)
                        check = True
                        break
                if not check:
                    newV = random.randint(0, self.V-1)
                    while (newV in odd) or newV == odd[0] or self.graph[odd[0]][newV]:
                        newV = random.randint(0, self.V-1)
                    self.graph[odd[0]][newV] = 1
                    self.graph[newV][odd[0]] = 1
                    odd.pop(0)
                    odd.append(newV)
        for w in self.graph:
            print(w, sum(w))     
                    
                    
    def euler_finder_help(self, graf, vert, u, s):
        for i in range(vert):
            if graf[u][i] == 1:
                graf[u][i] = None
                graf[i][u] = None
                self.euler_finder_help(graf, vert, i, s)
        s.append(u)

    def euler_finder(self):
        vert = self.V
        stack = []
        graf = self.graph.copy()
        self.euler_finder_help(graf, vert, 0, stack)
        print(stack)

    def hamilton_finder_help(self, s, u):
        s.append(u)
        for i in range(self.V):
            if self.graph[u][i] == 1 and i not in s:
                self.hamilton_finder_help(s, i)
        if len(s) == self.V:
            if self.graph[u][s[0]] == 1:
                s.append(s[0])
        else:
            s.pop(len(s) - 1)

    def hamilton_finder(self):
        s = []
        for i in range(self.V):
            if len(s) == self.V + 1:
                break
            else:
                self.hamilton_finder_help(s, i)
        s.append(s[0])
        print(s)

    def hamilton_finder_all_help(self, s, u):
        temp = s.copy()
        temp.append(u)
        for i in range(self.V):
            if self.graph[u][i] == 1 and i not in temp:
                self.hamilton_finder_all_help(temp, i)

        if len(temp) == self.V:
            if self.graph[u][temp[0]] == 1:
                temp.append(temp[0])
                print(temp)

        else:
            temp.pop(len(s) - 1)

    def hamilton_finder_all(self):
        s = []
        for i in range(self.V):
            if len(s) == self.V + 1:
                break
            else:
                self.hamilton_finder_all_help(s, i)

class Graph_L:
    def __init__(self, wierzcholki):
        self.graph = defaultdict()
        self.V = wierzcholki

    def topologicalSortPomoc(self, v, visited, stack):

        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortPomoc(i, visited, stack)
        stack.insert(0, v)


    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortPomoc(i, visited, stack)
        # print(stack)


    def minKey(self, key, mstSet):

        min = 1001

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index


    def printMST(self, parent):
        print("Edge \tWeight")
        weight = 0
        for i in range(1, self.V):
            weight += self.graph[i][parent[i]]
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
        print(weight)


    def primMST(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in self.graph[u].keys():
                if mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


    def connect_DAG_list_generator(self, nasycenie):
        slownik = {}
        poziomy = 0
        for i in range(self.V):
            if 2 ** i >= self.V:
                poziomy = i

        tabelka = []
        for i in range(poziomy):
            tabelka.append([])
        pomoc = []
        for i in range(self.V):
            pomoc.append(i)
        for i in range(self.V):
            losowa = random.randrange(0, self.V - i)
            slownik[pomoc[losowa]] = []
            pomoc.pop(losowa)
        i = 0
        for klucz in slownik:
            if len(tabelka[i]) == 2 ** i:
                i += 1
            tabelka[i].append(klucz)
        los_wierz = random.randrange(0, self.V)
        los_kraw = random.randrange(0, self.V)
        krawedzie = 0
        while (((self.V * (self.V - 1)) / 2) * (nasycenie / 100)) > krawedzie:
            cykl = False
            idenks_kraw = 1
            indeks_wierz = 0
            for i in range(poziomy):
                if los_wierz in tabelka[i]:
                    indeks_wierz = i
            for i in range(poziomy):
                if los_kraw in tabelka[i]:
                    indeks_kraw = i
            if indeks_kraw <= indeks_wierz:
                cykl = True
            if cykl == False and (los_kraw != los_wierz) and (los_kraw not in slownik[los_wierz]) and los_wierz not in \
                    slownik[los_kraw]:
                slownik[los_wierz].append(los_kraw)
                krawedzie += 1
            los_wierz = random.randrange(0, self.V)
            los_kraw = random.randrange(0, self.V)
        for i in range(self.V):
            self.graph[i] = slownik[i]

    def value_DAG_list_generator(self, nasycenie):

        for i in range(self.V):
            self.graph[i] = []
        krawedzie = 0
        los_wierz = random.randrange(0, self.V)
        los_kraw = random.randrange(0, self.V)
        waga = random.randrange(0, 1000)
        i = 0
        while i < self.V:

            warunek = True
            if los_kraw == i:
                warunek = False
            for j in self.graph[i]:
                if j[0] == i or i == los_kraw:
                    warunek == False
            if warunek == True:
                for j in self.graph[los_kraw]:
                    if j[0] == i or j[0] == los_kraw:
                        warunek = False

            if warunek == True:
                self.graph[i].append((los_kraw, waga))
                self.graph[los_kraw].append((i, waga))
                i += 1
                krawedzie += 1
            los_kraw = random.randrange(0, self.V)
            waga = random.randrange(0, 1000)
        while (((self.V * (self.V - 1)) / 2) * (nasycenie / 100)) >= krawedzie:
            warunek = True
            if los_kraw == los_wierz:
                warunek = False

            if warunek == True:
                for j in self.graph[los_wierz]:
                    if j[0] == i or i == los_kraw:
                        warunek == False
            if warunek == True:
                for j in self.graph[los_kraw]:
                    if j[0] == los_wierz or j[0] == los_kraw:
                        warunek = False

            if warunek == True:
                self.graph[los_wierz].append((los_kraw, waga))
                self.graph[los_kraw].append((los_wierz, waga))
                i += 1
                krawedzie += 1
            los_kraw = random.randrange(0, self.V)
            waga = random.randrange(0, 1000)
            los_wierz = random.randrange(0, self.V)


def cut_to_seconds(timestring):
    return (str(timestring))[-9:-1]


def matrix_to_list(matrix):
    graph = defaultdict()
    for w in range(len(matrix)):
        graph[w] = {}
        for c in range(len(matrix)):
            if matrix[w][c]:
                graph[w][c] = matrix[w][c]
    # for k in graph.keys():
    #     print(graph[k])
    return graph


def graph_sorting():
    print('Matrix sorting')
    for i in range(1,16):

        g = Graph_M(i*50)
        g.connect_DAG_matrix_generator(60)

        start = timer()
        g.topologicalSort()
        stop = timer()
        print(timedelta(seconds=stop - start))

    print('List sorting')
    for i in range(1,16):

        g = Graph_L(i*50)
        g.generate(60)

        start = timer()
        g.topologicalSort()
        stop = timer()
        print(timedelta(seconds=stop - start))

def graph_MST():
    for i in range(1, 2):

        gm = Graph_M(i * 1000)
        gm.value_DAG_matrix_generator(90) #Remember about set the saturation in %, 30% = 30

        start = timer()
        gm.primMST()
        stop = timer()
        print(cut_to_seconds(timedelta(seconds=stop - start)), end = ' ')

        gl = Graph_L(i * 1000)
        gl.graph = matrix_to_list(gm.graph)

        start = timer()
        gl.primMST()
        stop = timer()
        print(cut_to_seconds(timedelta(seconds=stop - start)))

def menu():
    option = True
    while option:
        print("============MENU============ \n"
              "1. Import and sort \n"
              "2. Generate and sort \n"
              "3. Import and find MST \n"
              "4. Generate and find MST \n"
              "0. Exit \n ========================== \n"
              "Select: ")

        option = int(input())

        if option == 1:
            tmp = []
            plik = open("topol.txt")

            for line in plik:
                tmp.append(list(line.split()))

            v = int(tmp[0][0])
            matrix = [[0]]*v
            dict = defaultdict()
            gl = Graph_L(v)
            gm = Graph_M(v)

            for i in range(1,v + 1):
                temporary = []
                tempdict = []
                for j in range(v):
                    temporary.append(int(tmp[i][j]))
                    if int(tmp[i][j]):
                        tempdict.append(j)
                dict[i - 1] = tempdict
                matrix[i - 1] = temporary
            gl.graph = dict
            gm.graph = matrix

            start = timer()
            gl.topologicalSort()
            stop = timer()
            print("Lista: ",cut_to_seconds(timedelta(seconds=stop - start)))

            start = timer()
            gm.topologicalSort()
            stop = timer()
            print("Macierz: ",cut_to_seconds(timedelta(seconds=stop - start)))


        if option == 2:
            v = int(input("V: "))
            saturation = int(input("%: "))
            gl = Graph_L(v)
            gm = Graph_M(v)
            gl.connect_DAG_list_generator(saturation)
            gm.connect_DAG_matrix_generator(saturation)

            start = timer()
            gl.topologicalSort()
            stop = timer()
            print("Lista: ", cut_to_seconds(timedelta(seconds=stop - start)))

            start = timer()
            gm.topologicalSort()
            stop = timer()
            print("Macierz: ", cut_to_seconds(timedelta(seconds=stop - start)))


        if option == 3:
            tmp = []
            plik = open("mst.txt")

            for line in plik:
                tmp.append(list(line.split()))

            v = int(tmp[0][0])
            matrix = [[0]]*v
            dict = defaultdict()
            gl = Graph_L(v)
            gm = Graph_M(v)

            for i in range(1,v+1):
                temporary = []
                tempdict = defaultdict()
                for j in range(v):
                    temporary.append(int(tmp[i][j]))
                    if int(tmp[i][j]):
                        tempdict[j] = int(tmp[i][j])
                dict[i-1] = tempdict
                matrix[i - 1] = temporary
            gl.graph = dict
            gm.graph = matrix

            start = timer()
            gl.primMST()
            stop = timer()
            print("Lista: ",cut_to_seconds(timedelta(seconds=stop - start)))

            start = timer()
            gm.primMST()
            stop = timer()
            print("Macierz: ",cut_to_seconds(timedelta(seconds=stop - start)))


        if option == 4:
            v = int(input("V: "))
            saturation = int(input("%: "))
            gl = Graph_L(v)
            gm = Graph_M(v)
            gm.value_DAG_matrix_generator(saturation)
            gl.graph = matrix_to_list(gm.graph)

            start = timer()
            gl.primMST()
            stop = timer()
            print("Lista: ", cut_to_seconds(timedelta(seconds=stop - start)))

            start = timer()
            gm.primMST()
            stop = timer()
            print("Macierz: ", cut_to_seconds(timedelta(seconds=stop - start)))
        next = input()
