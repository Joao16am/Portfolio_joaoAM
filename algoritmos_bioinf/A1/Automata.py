# -*- coding: utf-8 -*-


class Automata:

    def __init__(self, alphabet, pattern):
        self.numstates = len(pattern) + 1
        self.alphabet = alphabet
        self.transitionTable = {}
        self.buildTransitionTable(pattern)

    def buildTransitionTable(self, pattern):
        for q in range(self.numstates):
            for a in self.alphabet:
                prefix = pattern[:q] + a
                self.transitionTable[(q, a)] = overlap(prefix, pattern)

    def printAutomata(self):
        print("States: ", self.numstates)
        print("Alphabet: ", self.alphabet)
        print("Transition table:")
        for k in self.transitionTable.keys():
            print(k[0], ",", k[1], " -> ", self.transitionTable[k])

    def nextState(self, current, symbol):
        return self.transitionTable[(current, symbol)]

    def applySeq(self, seq):
        q = 0
        res = [q]
        for c in seq:
            q = self.nextState(q, c)
            res.append(q)
        return res

    def occurencesPattern(self, text):
        q = 0
        res = []
        for i in range(len(text)):
            q = self.nextState(q, text[i])
            if q == self.numstates - 1:
                res.append(i - self.numstates + 2)
        return res


def overlap(s1, s2):
    maxov = min(len(s1), len(s2))
    for i in range(maxov, 0, -1):
        print(s1[-i:], s2[:i])
        if s1[-i:] == s2[:i]:
            return i
    return 0


def test():
    auto = Automata("AC", "ACA")
    auto.printAutomata()
    print(auto.applySeq("CACAACAA"))
    print(auto.occurencesPattern("CACAACAA"))


def test2():
    auto2 = Automata('AGT', 'AGTGA')
    auto2.printAutomata()
    print(auto2.applySeq('ATGATGATAGAGAGTGGTATAGATAGATAGTAGAGTAGAGTAG'))
    print(auto2.occurencesPattern("ATAGTAGTGATGATAAGTAGTGAGAGTGGTATAGATAGATAGTGAGAGTAGAGTAG"))



#test2()

# States:  4
# Alphabet:  AC
# Transition table:
# 0 , A  ->  1
# 0 , C  ->  0
# 1 , A  ->  1
# 1 , C  ->  2
# 2 , A  ->  3
# 2 , C  ->  0
# 3 , A  ->  1
# 3 , C  ->  2
# [0, 0, 1, 2, 3, 1, 2, 3, 1]
# [1, 4]
