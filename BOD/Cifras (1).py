import sys

class cifras:

    def __init__(self, string):
        self.inp = string
        self.password, self.message = self.inpt()
        self.dict_password = self.codex_password()

    def get_info(self, strng):
        not_alph = list(set([na for na in strng if na.isalpha() is not True]))
        for na in not_alph: strng = strng.replace(na, '')
        return strng.upper()

    def inpt(self):
        parag_index = self.inp.index("\n")
        return self.get_info(self.inp[:parag_index]), self.get_info(self.inp[parag_index:])

    def codex_password(self):
        organised = sorted(self.password)
        dict_password = {}
        dict_password = {letter: (dict_password[letter]+[index] if letter in dict_password else [index]) for index, letter in enumerate(organised)}
        res = []
        res = [dict_password[let] for let in self.password if let not in res]
        return [l[0] for l in res]

    def coding(self):
        string = ''
        message = self.message
        missing = len(self.password) - len(message) % len(self.password)
        if missing > 0 and missing != len(self.password): msg = message + missing * ' '
        lst = [msg[ind:ind+len(self.password)] for ind in range(0, len(msg), len(self.password))]
        dic = {index: '' for index in range(len(self.password))}
        indexs = self.dict_password
        for lin in range(len(msg) // len(self.password)):
            for col in range(len(self.password)):
                dic[indexs[col]] = dic[indexs[col]] + lst[lin][col]
        for numb in set(sorted(indexs)): string += dic[numb]
        string = string.replace(' ', '')
        lst = [string[ind:ind + 5] for ind in range(0, len(string), 5)]
        res = ''
        for part in lst: res += part + ' '
        for n in range(0, len(res), 8*5+8):
            if n < len(res):
                res[n] = '\n'
        return res


if __name__ == '__main__':
    inputo = sys.stdin.readlines()
    cf = cifras([i.strip('\n') for i in inputo])
    print(cf.coding())
