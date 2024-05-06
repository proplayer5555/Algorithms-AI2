import random
from classes import*
import copy

def wkst_heu(a,maxTries,maxFlips,N,propability,k):
    P=len(a)
    finished = False
    flipcounter =0
    trycounter = 1 
    scoreperflip = [0 for x in range (N)]
    currentscore = 0
    lowscore = 0
    sidestep = []
    for i in range(maxTries):
        if(finished):
            break;
        truthtable = InitVariables(a,P,N,k) #initialized truth table
        #for n in range(N):
            #print((n+1),":",truthtable[n])      # print besttruthtable
        for j in range(maxFlips):
            currentscore = return_score(a,P,truthtable)
            if(currentscore == 0):
                finished = True
                break;
            else:
                index = heuristic(a,P,truthtable,propability,N,currentscore)#heuristic return index
                truthtable[index] = not truthtable[index]#flip
                flipcounter+=1
        print("try #",trycounter," variables flipped: ",flipcounter,"Total cost: ",currentscore)
        trycounter+=1
        flipcounter = 0
                    
    if(finished):
        print("Model found:\n",truthtable,"\n Total cost: ",currentscore)
    else:
        print("No model found!!! \n")

                   
def heuristic(a,P,truthtable,propability,N,currentscore):
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
        



def InitVariables(a,P,N,k):
    #calculate the score for each action (ex. 1->true , 5-> false)
    #and perform one action of the (N * 0.5) best until all actions depleted

    truthtable = [False for x in range(N)] #starting position = all zeros
    choices = [] #Initialize choices table 
    atemp = copy.deepcopy(a) # copy the full table with the problems

    #create all actions/choices
    for i in range(N):
        l1 = literal() #create positive literal
        l1.symbol = (i+1)
        choices.append(l1)
        l2 = literal() #create negative literal 
        l2.symbol = -(i+1)
        choices.append(l2)

    while(choices):
        for i in range(len(choices)): #calculate score for each
            choices[i].score = literal_score(atemp,choices[i].symbol)

        min_Score = choices[0].score   
        for x in range(len(choices)):   #find best score from choices
            if (choices[x].score < min_Score):
                min_Score = choices[x].score

        #setup choices in RCL "priority queue" with k size
        counter = 0
        Best_choices  = []
        for increase in range(P):
            if(counter == k):
                   break
            for x in range(len(choices)):
                if(choices[x].score == (min_Score + increase)):
                    Best_choices.append(choices[x])
                    counter+=1
                if(counter == k):
                    break

        chosen = random.randint(0,(len(Best_choices))-1) #choose random choice from VIP LIST
        if (Best_choices[chosen].symbol < 0):
            index = -(Best_choices[chosen].symbol)
            truthtable[index-1] = False   #Make the flip if negative 
        else:
            index = Best_choices[chosen].symbol #Make the flip if positive
            truthtable[index-1] = True
    
        #remove choice (and its negative) from choices list
        for i in range(len(choices)):
            if (Best_choices[chosen].symbol == choices[i].symbol):
                if (Best_choices[chosen].symbol < 0):
                    choices.pop(i) #remove negative literal
                    choices.pop(i-1) #remove counterpart positive literal
                else:
                    choices.pop(i) #remove positive choice
                    choices.pop(i) #remove counterpart negative  literal
                break


        #remove clauses that include chosen variable 
        #as to not influence score calculation for remaining literals in next iteration,
        #since those clauses would be true anyways
        atemp=delete_clause(atemp,Best_choices[chosen].symbol,Best_choices[chosen].score)
    
    
    return truthtable #return Initiliazed truthtable with the best choices

def literal_score(atemp,symbol):
    score = 0
    for r in range(len(atemp)):
        trueclause = False #make the trueclause False for the next literal
        for c in range(3):
            slot1 = atemp[r][c] #slot -> -1 1 6 ktlp
     
            if (symbol == slot1): #check if symbol == every symbol in the literal 
                trueclause = True

        if( trueclause == False):
            score+=1 #count score of the line in the table
    return score

def delete_clause(atemp,symbol,score):
    P=len(atemp)
    sizechanged = False
    for s in range (P-score): #removes as many literals as N-score
        for r in range(len(atemp)):
            if (sizechanged):
                sizechanged = False
                break
            for c in range(3):
                slot1 = atemp[r][c] #slot -> -1 1 6 ktlp
            
                if (symbol == slot1): #check if symbol == every symbol in the literal 
                    atemp.pop(r)
                    sizechanged = True
                    break
                
    return atemp