import sys

def quadrados(inputo):
	M, res = [], 0
	for i in inputo: M.append(list(map(int, i)))
	for i in range(len(M)):
		for j in range(len(M[i])):
			if M[i][j] == 1:
				s, tmh, x = 1, 1, 1
				while s != 0 and i + x < len(M) and j + x < len(M[0]):
					for tx in range(i, i + x + 1):
						if M[tx][j + x] != 1: s = 0
					for ty in range(j, j + x + 1):
						if M[i + x][ty] != 1: s = 0
					if s == 0: break
					else: x, tmh = x+1, tmh+1
				if tmh > res: res = tmh
	return res

inputo = sys.stdin.readlines()
print(quadrados(inputo))