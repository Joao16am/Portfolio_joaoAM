# -*- coding: utf-8 -*-

class SuffixTree:
    def __init__(self):
        self.nodes = {0: (-1, {})}  # root node
        self.num = 0

    def print_tree(self):
        for k in self.nodes.keys():
            if self.nodes[k][0] < 0:
                print(k, "->", self.nodes[k][1])
            else:
                print(k, ":", self.nodes[k][0])

    def add_node(self, origin, symbol, leafnum=-1):
        self.num += 1
        self.nodes[origin][1][symbol] = self.num
        self.nodes[self.num] = (leafnum, {})

    def add_suffix(self, p, sufnum):
        pos = 0
        node = 0
        while pos < len(p):
            if p[pos] not in self.nodes[node][1].keys():
                if pos == len(p) - 1:
                    self.add_node(node, p[pos], sufnum)
                else:
                    self.add_node(node, p[pos])
            node = self.nodes[node][1][p[pos]]
            pos += 1

    def suffix_tree_from_seq(self, text):
        t = text + "$"
        for i in range(len(t)):
            self.add_suffix(t[i:], i)

    def find_pattern(self, pattern):
        pos = 0
        node = 0
        for pos in range(len(pattern)):
            if pattern[pos] in self.nodes[node][1].keys():
                node = self.nodes[node][1][pattern[pos]]
            else:
                return None
        return self.get_leafes_below(node)

    def get_leafes_below(self, node):
        res = []
        if self.nodes[node][0] >= 0:
            res.append(self.nodes[node][0])
        else:
            for k in self.nodes[node][1].keys():
                newnode = self.nodes[node][1][k]
                leafes = self.get_leafes_below(newnode)
                res.extend(leafes)
        return res

    # 1.A) Conjunto_1
    def nodes_below(self, node):
        res, c_res = [node], []  # c_res => é uma lista para confirmar quais os nós já lidos
        while len(res) != len(c_res):
            if len(self.nodes[node][1].keys()) != 0:  # Aqui é para meter os nós
                for nuc in self.nodes[node][1].keys():
                    id2 = self.nodes[node][1][nuc]  # para qual leva o tuplo do nuc
                    if nuc != '$' and list(self.nodes[id2][1].keys()) != ['$']:
                        res.append(self.nodes[node][1][nuc])
            for i in reversed(res):
                if i not in c_res:  # é para alterar de Nó em Nó !
                    c_res.append(i)
                    node = i
                    break
            res = list(dict.fromkeys(res))
            c_res = list(dict.fromkeys(c_res))
        res.remove(res[0])  # Remover o nó inicial
        if len(res) != 0:
            return sorted(res)
        else:
            return -1

    # 1.B) Conjunto_1
    def matches_prefix(self, prefix):
        res = []
        if not self.find_pattern(prefix):
            return -1  # Ver se o padrão existe na arvore, caso não, dá -1
        else:
            res.append(prefix)
            id = self.nodes[0][1][prefix[0]]
            c = 1
            while c != len(prefix):  # Determinar a posição da ultima letra do padrão
                for i in self.nodes[id][1].keys():
                    if c != len(prefix) and i == prefix[c]:
                        c += 1
                        id = self.nodes[id][1][i]

            str = prefix
            for no in self.nodes_below(id):  # Associar a uma lista resultado todos as sequências possíveis com o prefixo dado
                aux_list = list(self.nodes[no - 1][1].keys())
                str += aux_list[0]
                res.append(str)
            return sorted(list(set(res)))

    # 2) Conjunto_1

class DoubleTree(SuffixTree):

    def __init__(self):
        self.nodes = {0: (-1, {})}  # root node
        self.num = 0

    def print_tree(self):
        for k in self.nodes.keys():
            if self.nodes[k][0] < 0:
                print(k, "->", self.nodes[k][1])
            else:
                print(k, ":", self.nodes[k][0])

    def add_node(self, origin, symbol, leafnum=-1):
        self.num += 1
        self.nodes[origin][1][symbol] = self.num
        self.nodes[self.num] = (leafnum, {})

    def add_suffix(self, p, sufnum):
        pos = 0
        node = 0
        while pos < len(p):
            if p[pos] not in self.nodes[node][1].keys():
                if pos == len(p) - 1:
                    self.add_node(node, p[pos], sufnum)
                else:
                    self.add_node(node, p[pos])
            node = self.nodes[node][1][p[pos]]
            pos += 1

    def suffix_tree_from_seqs(self, text1, text2):
        t1 = text1 + "$"
        t2 = text2 + "#"
        for seq in [t1, t2]:
            for i in range(len(seq)):
                self.add_suffix(seq[i:], i)

    def nodes_below(self, node):
        res, c_res = [node], []  # c_res => é uma lista para confirmar quais os nós já lidos
        while len(res) != len(c_res):
            if len(self.nodes[node][1].keys()) != 0:  # Aqui é para meter os nós
                for nuc in self.nodes[node][1].keys():
                    id2 = self.nodes[node][1][nuc]  # para qual leva o tuplo do nuc
                    if nuc != '$' and nuc != '#' and list(self.nodes[id2][1].keys()) != ['#'] and list(self.nodes[id2][1].keys()) != ['$']:
                        res.append(self.nodes[node][1][nuc])
            for i in reversed(res):
                if i not in c_res:  # é para alterar de Nó em Nó !
                    c_res.append(i)
                    node = i
                    break
            res = list(dict.fromkeys(res))
            c_res = list(dict.fromkeys(c_res))
        res.remove(res[0])  # Remover o nó inicial
        if len(res) != 0:
            return sorted(res)
        else:
            return -1

    def find_pattern(self, pattern):
        pos = 0
        node = 0
        for pos in range(len(pattern)):
            if pattern[pos] in self.nodes[node][1].keys():
                node = self.nodes[node][1][pattern[pos]]
            else:
                return None
        return self.get_leafes_below(node)

    def get_leafes_below(self, node):
        res = []
        if self.nodes[node][0] >= 0:
            res.append(self.nodes[node][0])
        else:
            for k in self.nodes[node][1].keys():
                newnode = self.nodes[node][1][k]
                leafes = self.get_leafes_below(newnode)
                res.extend(leafes)
        return res

    def largestCommonSubstring(self):
        check, node = [[], []], 0
        while node != len(self.nodes):
            for i in self.nodes[node][1].keys():
                if i == '$':
                    check[0].append(node)
                elif i == '#':
                    check[1].append(node)
            node += 1
        print(check)


def test():
    seq = "TACTA"
    st = SuffixTree()
    st.suffix_tree_from_seq(seq)
    st.print_tree()
    # print (st.find_pattern("TA"))
    # print (st.find_pattern("ACG"))
    print(st.nodes_below(1))
    print(st.matches_prefix('TA'))


def test2():
    seq = "TACTA"
    st = SuffixTree()
    # st.suffix_tree_from_seq(seq)
    # print(st.find_pattern("TA"))
    # print(st.repeats(2,2))


def test3():
    seq1 = "TACTA"
    seq2 = "AGTAC"
    DT = DoubleTree()
    DT.suffix_tree_from_seqs(seq1, seq2)
    DT.print_tree()
    #print(DT.nodes_below(1))
    print(DT.largestCommonSubstring())
    # print(DT.find_pattern('ACT'))
    #print(DT.get_leafes_below(0))


#test()
# test2()
test3()
