import sys

# a map is a tuple of matrix and a dict with neighbor info
def readmap(inputfile,alignment):
	f = open(inputfile, "r")
	mat = []
	for line in f:
		mat.append(line.splitlines()[0].split(','))
	f.close()
	nbs = {}
	for row in range(0,len(mat)):
		for col in range(0,len(mat[row])):
			nbs[(row,col)] = []
			odd = row % 2
			odd = odd ^ alignment #invert what is odd and what is even depending on map alignment
			if odd == 1: #odd rows
				if row > 0:
					nbs[(row,col)].append((row-1,col)) # odd rows always grab up 
					nbs[(row,col)].append((row-1,col+1))
				if row < 8:
					nbs[(row,col)].append((row+1,col))# odd rows always grab bottom
					nbs[(row,col)].append((row+1,col+1))
			else: #even rows 
				if row > 0:
					if col > 0:
						nbs[(row,col)].append((row-1,col-1))
					if col < (len(mat[row])-1):
						nbs[(row,col)].append((row-1,col))
				if row < 8:
					if col > 0:
						nbs[(row,col)].append((row+1,col-1))
					if col < (len(mat[row])-1):
						nbs[(row,col)].append((row+1,col))
			if col > 0:
				nbs[(row,col)].append((row,col-1))
			if (col < (len(mat[row])-1)):
				nbs[(row,col)].append((row,col+1))
	return mat,nbs

def f1(tm_map):
	mat = tm_map[0]
	nbs = tm_map[1]
	tot = 0
	for row in range(0,len(mat)): #for each row
		pr = []
		for col in range(0,len(mat[row])): #for each col in that row
			if mat[row][col] != 'I': #if hex is not a river
				occ = 0
				for r,c in nbs[(row,col)]: #for each neighbor of the hex
					if mat[row][col] == mat[r][c]: #if it's the same color
						occ += 1	# increase req1 infractions
				if occ > 0:
					tot+=occ
					pr.append(1)
				else:
					pr.append(0)
			else:
				pr.append(0)
		print(pr)
	return tot

def f2(tm_map):
	mat = tm_map[0]
	nbs = tm_map[1]
	tot = 0
	for row in range(0,len(mat)): #for each row
		pr = []
		for col in range(0,len(mat[row])): # for each col in that row
			if mat[row][col] == 'I': # if this is a river hex
				occ = 0
				for r,c in nbs[(row,col)]: #for each neighbor
					if mat[r][c] == 'I': # if the neighbor is also a river
						occ += 1
				if occ < 1 or occ > 3: #req2 as written "between 1 and 3 neighbor river hexes to avoid formation of lakes", their mathematical formula does not express this
					tot+=1
					pr.append(1)
				else:
					pr.append(0)
			else:
				pr.append(0)
		print(pr)
	return tot

def f3(tm_map):
	mat = tm_map[0]
	nbs = tm_map[1]
	visited  = [] #set()
	initr = 0
	initc = 0
	tot = 0
	while True:
		found = False
		for row in range(0,len(mat)):
			for col in range(0, len(mat[row])):
				if mat[row][col] == 'I' and (row,col) not in visited:	# river hex which we have not visited yet
					initr = row
					initc = col
					found = True
					break
			if found == True:
				break
		if found == False:
			return tot
		print("starting new disjoint river with hex " + str(initr) + "," + str(initc))
		S = [(initr,initc)] #initialize stack
		visited.append((initr,initc))
		while S != []:
			rs,cs = S.pop() #pop stack to do DFS
			for nr,nc in nbs[(rs,cs)]:
				if mat[nr][nc] == 'I' and (nr,nc) not in visited:
					S.append((nr,nc))
					#visited.add((nr,nc))
					visited.append((nr,nc))
		tot+=1
	return tot			

def f4(tm_map):
	mat = tm_map[0]
	nbs = tm_map[1]
	tot = 0
	isOneSpade = {}
	isOneSpade['R'] = {'S','Y'}
	isOneSpade['S'] = {'R','G'}
	isOneSpade['G'] = {'S','B'}
	isOneSpade['B'] = {'G','K'}
	isOneSpade['K'] = {'B','U'}
	isOneSpade['U'] = {'K','Y'}
	isOneSpade['Y'] = {'U','R'}
	for row in range(0,len(mat)):
		pr = []
		for col in range(0,len(mat[row])):
			if mat[row][col] != 'I': # if this is not a river
				occ = False	# default: no neighbor with 1-spade distance
				for r,c in nbs[(row,col)]: # for each neighbor
					if mat[r][c] in isOneSpade[mat[row][col]]: #if neighbor is 1-spade away from hex
						occ = True	# found one
						break
				if not occ:
					tot+=1
					pr.append(1)
				else:
					pr.append(0)
			else:
				pr.append(0)
		print(pr)
	return tot

def f5(tm_map): #peninsula
	mat = tm_map[0]
	nbs = tm_map[1]
	tot = 0
	for row in range(0,len(mat)): #for each row
		pr = []
		for col in range(0,len(mat[row])): #for each col in that row
			if mat[row][col] != 'I': #if hex is not a river
				occ = 0
				for r,c in nbs[(row,col)]: #for each neighbor of the hex
					if mat[r][c] != 'I': #if neighbor is not a river
						occ += 1	# increase req1 infractions
				if occ < 2:
					tot+=1
					pr.append(1)
				else:
					pr.append(0)
			else:
				pr.append(0)
		print(pr)
	return tot

if __name__ == '__main__':
	infile = sys.argv[1]
	a = 0
	if len(sys.argv) > 2:
		if sys.argv[2] == "skewed":
			a = 1
		else:
			print("we only accept 'skewed' as a parameter so far...")
			sys.exit()

	tm_map = readmap(infile,a)
	print("f1 analysis")
	print(str(f1(tm_map)) + " infractions")
	print("f2 analysis")
	print(str(f2(tm_map)) + " infractions")
	print("f3 analysis")
	print(str(f3(tm_map)) + " disjoint rivers")
	print("f4 analysis") 
	print(str(f4(tm_map)) + " infractions")
	print(str(f5(tm_map)) + " isolated peninsulas")
