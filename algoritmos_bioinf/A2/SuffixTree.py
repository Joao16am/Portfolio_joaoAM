# -*- coding: utf-8 -*-

class SuffixTree:
    
    def __init__(self):
        self.nodes = { 0:(-1,{}) } # root node
        self.num = 0
    
    def print_tree(self):
        for k in self.nodes.keys():
            if self.nodes[k][0] < 0:
                print (k, "->", self.nodes[k][1]) 
            else:
                print (k, ":", self.nodes[k][0])
                
    def add_node(self, origin, symbol, leafnum = -1):
        self.num += 1
        self.nodes[origin][1][symbol] = self.num
        self.nodes[self.num] = (leafnum,{})
        
    def add_suffix(self, p, sufnum):
        pos = 0
        node = 0
        while pos < len(p):
            if p[pos] not in self.nodes[node][1].keys():
                if pos == len(p)-1:
                    self.add_node(node, p[pos], sufnum)
                else:
                    self.add_node(node, p[pos])
            node = self.nodes[node][1][p[pos]]
            pos += 1
    
    def suffix_tree_from_seq(self, text):
        t = text+"$"
        for i in range(len(t)):
            self.add_suffix(t[i:], i)
            
    def find_pattern(self, pattern):
        pos = 0
        node = 0
        for pos in range(len(pattern)):
            if pattern[pos] in self.nodes[node][1].keys():
                node = self.nodes[node][1][pattern[pos]]
            else: return None
        return self.get_leafes_below(node)
        

    def get_leafes_below(self, node):
        res = []
        if self.nodes[node][0] >=0: 
            res.append(self.nodes[node][0])            
        else:
            for k in self.nodes[node][1].keys():
                newnode = self.nodes[node][1][k]
                leafes = self.get_leafes_below(newnode)
                res.extend(leafes)
        return res

    #1.A) Conjunto_1
    def nodes_below(self, node):
        res = []
        for nucleotido in list(self.nodes[node][1].keys()):
            check = False
            B1 = False
            while B1 != True:  # Primeira Barreira => Determinar se o nó principal já acabou
                if nucleotido != '$' and check == False:
                    id = self.nodes[node][1][nucleotido]
                    res.append(id)
                    B2 = False
                    while B2 == False:  # Segunda Barreira => Serve para saltar de nó em nó
                        for inner_check in self.nodes[id][1].keys():
                            if inner_check != '$':
                                res.append(self.nodes[id][1][inner_check])
                                id = res[-1]
                            else:
                                if '$' in self.nodes[id][1].keys():
                                    check = True
                                    B2 = True
                B1 =True
        return res

    #1.B) Conjunto_1
    def matches_prefix(self, prefix):
        res = []
        if not self.find_pattern(prefix): return -1        #Ver se o padrão existe na arvore, caso não, dá -1
        else:
            res.append(prefix)
            id = self.nodes[0][1][prefix[0]]
            c = 1
            while c!=len(prefix):                           #Determinar a posição da ultima letra do padrão
                for i in self.nodes[id][1].keys():
                    if c != len(prefix) and i == prefix[c]:
                        c+=1
                        id = self.nodes[id][1][i]

            str = prefix
            for no in self.nodes_below(id):                 #Associar a uma lista resultado todos as sequências possíveis com o prefixo dado
                aux_list = list(self.nodes[no-1][1].keys())
                str += aux_list[0]
                res.append(str)
            return sorted(list(set(res)))

    #2) Conjunto_1
    def largestCommonSubstring(self):










def test():
    seq = "TACTA"
    st = SuffixTree()
    st.suffix_tree_from_seq(seq)
    st.print_tree()
    print (st.find_pattern("TA"))
    #print (st.find_pattern("ACG"))
    print(st.nodes_below(1))
    print(st.matches_prefix('TA'))

def test2():
    seq = "TACTA"
    st = SuffixTree()
    #st.suffix_tree_from_seq(seq)
    #print(st.find_pattern("TA"))
    #print(st.repeats(2,2))

test()
#test2()