import random

def walksat(a,maxTries,maxFlips,N,propability):
    P=len(a)#Number of problems
    finished = False
    flipcounter =0
    trycounter = 1 
    truthtable = [False for x in range(N)]
    scoreperflip = [0 for x in range (N)]
    currentscore = 0
    lowscore = 0
    sidestep = [] #variables whose flip results in side step
    for i in range(maxTries):
        if(finished):
            break;
        for n in range (N): #initialize variables
            truthtable[n] = random.choice([True, False])
            #print((n+1),":",truthtable[n])
        for j in range(maxFlips):
            currentscore = return_score(a,P,truthtable)
            if(currentscore == 0):
                finished = True
                break;
            else:
                index = heuristic(a,P,truthtable,propability,currentscore) #heuristic return index
                truthtable[index] = not truthtable[index] #flip
                flipcounter+=1
        print("try #",trycounter," variables flipped: ",flipcounter,"Total cost: ",currentscore)
        trycounter+=1
        flipcounter = 0
                    
    if(finished):
        print("Model found:\n",truthtable,"\n Total cost: ",currentscore)
    else:
        print("No model found!!! \n")

                   
def heuristic(a,P,truthtable,propability,currentscore):
    #randomly choose false clause. From its variables:
    #if a variable lowers score then flip it,
    #else (either flip random variable or flip variable with the least negative impact) according to p

    indexes2 = []
    scoreperflip2 = [0 for x in range (3)]

    #get random clause that is false
    clause = random.randint(0,P-1)
    while(falseClause(clause,a,truthtable)):
          clause = random.randint(0,P-1)    

    #appends variables from false clause to list
    for c in range(3):
        if (a[clause][c]<0):
            indexes2.append(-(a[clause][c])) #flip index if it's negative
        else:
            indexes2.append(a[clause][c])
            
    #test score for each variable flipped in list
    for x in range(3):
        truthtable[(indexes2[x])-1] = not truthtable[(indexes2[x])-1]
        scoreperflip2[x] = return_score(a,P,truthtable)
        truthtable[(indexes2[x])-1] = not truthtable[(indexes2[x])-1]

    #calculate total score
    lowscore = scoreperflip2[0]
    tempx = 0
    for x in range(3):
        if (scoreperflip2[x] < lowscore):
            lowscore = scoreperflip2[x]
            tempx = x
    if (lowscore < currentscore):
        return ((indexes2[tempx])-1)

    #No better flip found:
    else:
        if (random.uniform(0,1) <= propability): # propability p 
            return ((indexes2[random.randint(0,2)])-1) #choose a random variable in c 
        else:
            return ((indexes2[tempx])-1) #return variable with the least negative impact 




def falseClause(r,a,truthtable): #returns if clause is true or false
    trueclause = False #make the trueclause False for the next literal
    for c in range(3):
        slot1 = a[r][c] #slot -> -1 1 6 ktlp   # r is the random c that the algorith will take

        if (slot1 > 0):
            if (truthtable[(a[r][c])-1] == True):
                trueclause = True
        else:
            if (truthtable[((-a[r][c]))-1] == False):
                trueclause = True
    return trueclause   # return true or false if the whole clause is true or false
                

def return_score(a,P,truthtable):
    score = 0
    trueclause = False
    for r in range(P):
        trueclause = False #make the trueclause False for the next literal
        for c in range(3):
            slot1 = a[r][c] #slot -> -1 1 6 ktlp

            if (slot1 > 0):
                if (truthtable[(a[r][c])-1] == True):
                    trueclause = True
            else:
                if (truthtable[((-a[r][c]))-1] == False):
                    trueclause = True
        if( trueclause == False):
            score+=1 #count score of the line in the table

    return score
        

    


    
