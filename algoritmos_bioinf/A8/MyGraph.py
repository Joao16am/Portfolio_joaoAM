# -*- coding: utf-8 -*-

## Graph represented as adjacency list using a dictionary
## keys are vertices
## values of the dictionary represent the list of adjacent vertices of the key node

class MyGraph:
    
    def __init__(self, g = {}):
        ''' Constructor - takes dictionary to fill the graph as input; default is empty dictionary '''
        self.graph = g
        if g != {}: self.id = self.id_graph()
        self.mat_count()

    def print_graph(self):
        ''' Prints the content of the graph as adjacency list '''
        for v in self.graph.keys():
            print (v, " -> ", self.graph[v])


    ## get basic info

    def id_graph(self):
        for key in self.graph.keys():
            if type(self.graph[key][0]) is tuple: return 'grw'
            else: return 'gr'

    def mat_count(self):
        mat = [[0 for j in range(len(self.graph.keys()))] for i in range(len(self.graph.keys()))]
        for i in self.get_nodes():
            for j in self.graph[i]:
                n, p = j
                mat[self.get_nodes().index(i)][self.get_nodes().index(n)] = p
        return mat

    def get_nodes(self):
        ''' Returns list of nodes in the graph '''
        return list(self.graph.keys())
        
    def get_edges(self): 
        ''' Returns edges in the graph as a list of tuples (origin, destination) '''
        edges = []
        for v in self.graph.keys():
            for d in self.graph[v]:
                if type(d)==tuple:edges.append((v,d[0],d[1]))
                else: edges.append((v,d))
        return edges
      
    def size(self):
        ''' Returns size of the graph : number of nodes, number of edges '''
        return len(self.get_nodes()), len(self.get_edges())
      
    ## add nodes and edges    
    
    def add_vertex(self, v):
        ''' Add a vertex to the graph; tests if vertex exists not adding if it does '''
        if v not in self.graph.keys():
            self.graph[v] = []
        
    def add_edge(self, o, d, p = 'bin'):
        ''' Add edge to the graph; if vertices do not exist, they are added to the graph '''
        if o not in self.graph.keys():
            self.add_vertex(o)
        if d not in self.graph.keys():
            self.add_vertex(d)
        if d not in self.graph[o] and p == 'bin':
            self.graph[o].append(d)
        else: self.graph[o].append((d,p))

    ## successors, predecessors, adjacent nodes
        
    def get_successors(self, v):
        if self.id == 'gr': return list(self.graph[v])  # needed to avoid list being overwritten of result of the function is used
        else:
            res=[]
            for n in self.graph[v]:
                res.append(n[0])
            return res


    def get_predecessors(self, v):
        if self.id == 'gr':
            res = [i for i in self.graph.keys() if v in self.graph[i]]
        else:
            res = []
            for i in self.graph.keys():
                for j in self.graph[i]:
                    if v == j[0]:
                        res.append(i)
        return res

    def get_adjacents(self, v):
        suc = self.get_successors(v)
        pred = self.get_predecessors(v)
        res = pred
        for p in suc:
            if p not in res: res.append(p)
        return res

    ## degrees    
    
    def out_degree(self, v):
        return len(self.graph[v])

    def in_degree(self, v):
        return len(self.get_predecessors(v))

    def degree(self, v):
        return len(self.get_adjacents(v))

    ## BFS and DFS searches    
    
    def reachable_bfs(self, v):
        l = [v]
        res = []
        while len(l) > 0:
            node = l.pop(0)
            if node != v: res.append(node)
            for elem in self.graph[node]:
                if elem not in res and elem not in l and elem != node:
                    l.append(elem)  #Acrescenta sempre no fim!
        return res
        
    def reachable_dfs(self, v):
        l = [v]
        res = []
        while len(l) > 0:
            node = l.pop(0)
            if node != v: res.append(node)
            s = 0
            for elem in self.graph[node]:
                if elem not in res and elem not in l:
                    l.insert(s, elem)   # Ele acrescenta sempre no inicio
                    s += 1
        return res    
    
    def distance(self, s, d):
        if s == d: return 0
        if self.id == 'gr':
            l = [(s,0)]
            visited = [s]
            while len(l)>0:
                node, dist = l.pop(0)
                for elem in self.graph[node]:
                    if elem == d: return dist + 1
                    elif elem not in visited:
                        l.append((elem,dist+1))
                        visited.append(elem)
        else:
            l = [(s,0,0)]
            #visited = []
            res_t = []
            while len(l)>0:
                node, dist, price = l.pop(0)
                for elem in self.graph[node]:
                    node_t, price_t = elem
                    l.append((node_t, dist+1, price + price_t))
                if node == d:
                    res_t.append((node, dist, price))
            if len(res_t)==0: return None
            else:
                best = 'no'
                for coor in res_t:
                    pos, dist, price = coor
                    if best == 'no':
                        best = (dist, price)
                    else:
                        if best[1]>price:
                            best = (dist, price)
                return best
        
    def shortest_path(self, s, d):
        if s == d: return []
        if self.id == 'gr':
            l = [(s, [])]
            visited = [s]
            while len(l) > 0:
                node, preds = l.pop(0)
                for elem in self.graph[node]:
                    if elem == d:
                        return preds + [node, elem]
                    elif elem not in visited:
                        l.append((elem, preds + [node]))
                        visited.append(elem)
        else:
            l = [(s, 0, 0)]
            res_t = []
            while len(l) > 0:
                node, dist, price = l.pop(0)
                for elem in self.graph[node]:
                    node_t, price_t = elem
                    l.append((node_t, dist + 1, price + price_t))
                if node == d:
                    res_t.append((node, dist, price))

            if len(res_t) == 0:
                return None
            else:
                best = 'no'
                for coor in res_t:
                    pos, dist, price = coor
                    if best == 'no':
                        best = (dist, price)
                    else:
                        if best[0] > dist:
                            best = (dist, price)
                return best
        
    def reachable_with_dist(self, s):
        res = []
        l = [(s,0)]
        while len(l) > 0:
            node, dist = l.pop(0)
            if node != s: res.append((node,dist))
            for elem in self.graph[node]:
                if not is_in_tuple_list(l,elem) and not is_in_tuple_list(res,elem): 
                    l.append((elem,dist+1))
        return res

## cycles
    def node_has_cycle (self, v):
        l = [v]
        res = False
        visited = [v]
        while len(l) > 0:
            node = l.pop(0)
            for elem in self.graph[node]:
                if elem == v: return True
                elif elem not in visited:
                    l.append(elem)
                    visited.append(elem)
        return res

    def has_cycle(self):
        res = False
        for v in self.graph.keys():
            if self.node_has_cycle(v): return True
        return res


def is_in_tuple_list (tl, val):
    res = False
    for (x,y) in tl:
        if val == x: return True
    return res


def test1():
    gr = MyGraph( {1:[2], 2:[3], 3:[2,4], 4:[2]} )
    gr.print_graph()
    print (gr.get_nodes())
    print (gr.get_edges())
    

def test2():
    gr2 = MyGraph()
    gr2.add_vertex(1)
    gr2.add_vertex(2)
    gr2.add_vertex(3)
    gr2.add_vertex(4)
    
    gr2.add_edge(1,2)
    gr2.add_edge(2,3)
    gr2.add_edge(3,2)
    gr2.add_edge(3,4)
    gr2.add_edge(4,2)
    
    gr2.print_graph()
  
def test3():
    gr = MyGraph( {1:[2], 2:[3], 3:[2,4], 4:[2]} )
    gr.print_graph()

    print (gr.get_successors(2))
    print (gr.get_predecessors(2))
    print (gr.get_adjacents(2))
    print (gr.in_degree(2))
    print (gr.out_degree(2))
    print (gr.degree(2))

def test4():
    gr = MyGraph( {1:[2], 2:[3], 3:[2,4], 4:[2]} )
    
    print (gr.distance(1,4))
    print (gr.distance(4,3))

    print (gr.shortest_path(1,4))
    print (gr.shortest_path(4,3))

    print (gr.reachable_with_dist(1))
    print (gr.reachable_with_dist(3))

    gr2 = MyGraph( {1:[2,3], 2:[4], 3:[5], 4:[], 5:[]} )
    
    print (gr2.distance(2,1))
    print (gr2.distance(1,5))
    
    print (gr2.shortest_path(1,5))
    print (gr2.shortest_path(2,1))

    print (gr2.reachable_with_dist(1))
    print (gr2.reachable_with_dist(5))

def test5():
    gr = MyGraph( {1:[2], 2:[3], 3:[2,4], 4:[2]} )
    print (gr.node_has_cycle(2))
    print (gr. node_has_cycle(1))
    print (gr.has_cycle())

    gr2 = MyGraph( {1:[2,3], 2:[4], 3:[5], 4:[], 5:[]} )
    print (gr2. node_has_cycle(1))
    print (gr2.has_cycle())


#Testes para grafos pesados
def test6():
    grw = MyGraph({1:[(2,10)],2:[(3,20),(4,10)],3:[(5,30)],4:[(5,10)],5:[(6,10)],6:[]})
    grw.print_graph()
    print(grw.get_nodes())
    print(grw.get_edges())

def test7():
    grw = MyGraph()

    grw.add_vertex(1)
    grw.add_vertex(2)
    grw.add_vertex(3)
    grw.add_vertex(4)
    grw.add_vertex(5)
    grw.add_vertex(6)

    grw.add_edge(1, 2, 10)
    grw.add_edge(2, 3, 20)
    grw.add_edge(2, 4, 10)
    grw.add_edge(3, 5, 20)
    grw.add_edge(4, 5, 10)
    grw.add_edge(5, 6, 10)

    grw.print_graph()

    print(grw.get_nodes())
    print(grw.get_edges())

def test8():
    grw = MyGraph({1:[(2,10)],2:[(3,20),(4,10)],3:[(5,30)],4:[(5,10)],5:[(6,10)],6:[]})
    #grw.print_graph()

    print(grw.get_successors(5))
    print(grw.get_predecessors(5))
    print(grw.get_adjacents(5))
    print(grw.in_degree(5))
    print(grw.out_degree(5))
    print(grw.degree(5))

def test9():
    grw = MyGraph({1: [(2, 10)], 2: [(3, 20), (4, 10)], 3: [(5, 30)], 4: [(5, 10)], 5: [(6, 10)], 6: []})
    print(grw.distance(1,6))

    grw2 = MyGraph({1: [(2, 10)], 2: [(3, 10), (4, 5)], 3: [(6, 10)], 4: [(5, 5)], 5: [], 6: [(7,10)], 7:[]})
    print(grw2.distance(1,7))

    grw3 = MyGraph({1: [(2, 10)], 2: [(3, 10), (4, 5)], 3: [(6, 10)], 4: [(5, 5), (8, 1)], 5: [], 6: [(7, 10)], 7: [], 8: [(6, 1)]})
    print(grw3.distance(1, 7))
    print('Short: ', grw3.shortest_path(1,7))

    #grw4 = MyGraph({1:[(2,2)], 2:[(3,3)], 3:[(4,5),(6,4)], 4:[(5,6)], 5:[(1,7)], 6:[]})
    #print(grw4.distance(1, 5))
    #print('Short: ', grw4.shortest_path(1, 5))

if __name__ == "__main__":
    #test1()
    #test2()
    #test3()
    #test4()
    #test5()

#Grafos pesados
    #test6()
    #test7()
    #test8()
    test9()
    pass

