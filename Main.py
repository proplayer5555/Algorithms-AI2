import random
from GSAT import *
from GSATRW import *
from WALKSAT import *
from WKST_HEU import *




def CheckClause(r1):#checks if literal shows up twice in a clause or its negative
	good_Clause = True
	for i in range(3):
		checkSymbol = literals[r1][i]
		checkNeg = -checkSymbol
		for j in range(3):
			if ((literals[r1][j] == checkSymbol or literals[r1][j] == checkNeg) and (i!=j) ):
				good_Clause = False
	return good_Clause


def CheckProblem(): #checks for each clause if all of its literals show up in another clause
	good_Problem = True
	if (literals[0][0] == 0 ):
		good_Problem = False
	
	for p in range(P):
		checkClause = literals[p]

		for p2 in range(P):
			point=0
			compareClause = literals[p2]
			for i in range(3):
				if ((checkClause[0] == compareClause[i]) and (p!=p2) ):
					point += 1
			for i in range(3):
				if ((checkClause[1] == compareClause[i]) and (p!=p2) ):
					point += 1				
			for i in range(3):
				if ((checkClause[2] == compareClause[i]) and (p!=p2) ):
					point += 1
			if (point>=3): #3 points -> all three literals show up somewhere else
				good_Problem = False

	return good_Problem

def Printall():
	for r in range (P):		
		print( literals[r])


N1 = input("Insert Ν number of symbols: ")
N=int(N1)
# N=30 #number of symbols 30
P1 = input("Insert P number of clauses: ")
P=int(P1)
# P=220 #number of clauses 250
NegPercentage1 = input("Insert Percentage for negative literal:%")
NegPercentage=(float(NegPercentage1))/100
# NegPercentage = 0.3 #negative literal percentage 0.3
M1 = input("Insert M number of problems to solve: ")
M=int(M1)
# M = 1 #Number of problems to solve
maxtries1 = input("Insert acceptable number of tries: ")
maxtries=int(maxtries1)
# maxtries = 10
maxflips1 = input("Insert acceptable number of flips: ")
maxflips=int(maxflips1)
# maxflips = 40

#percentage 0.8
percentage1 = input("Insert percentage for random Random Walk for GSATRW(close to 100): ")
percentage=(float(percentage1))/100
#percentage walksat 0.3
percentage2 = input("Insert percentage for random WalkSat for WALKSAT(close to 0): ")
percentage_Walksat=(float(percentage2))/100

k1 = input("Insert amount of best actions to choose from for semi-heuristic: ")
k=int(k1)

for m in range(M):
	literals = [[0 for x in range(3)] for x in range(P)]
	truthtable = [[False for x in range(3)] for x in range(P)]

	#Problem initialization
	while(not CheckProblem()):
		literals = [[0 for x in range(3)] for x in range(P)]
		for r in range (P):
			while (not CheckClause(r)):
				for c in range(3):
					tempSymbol = random.randint(1,N)
					if (random.uniform(0,1) <= NegPercentage): #chance for negative
						tempSymbol = -tempSymbol
					literals[r][c] = tempSymbol

	Printall()

	print("Gsat:")
	gsat(literals,maxtries,maxflips,N)
	print("\nGsatrw:")
	gsatrw(literals,maxtries,maxflips,N,percentage)
	print("\nWalksat:")
	walksat(literals,maxtries,maxflips,N,percentage_Walksat)
	print("\nWalksat with truth table initialization:")
	wkst_heu(literals,maxtries,maxflips,N,percentage_Walksat,k)



    















        