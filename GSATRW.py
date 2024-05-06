
import random

def gsatrw(a,maxTries,maxFlips,N,propability):
    P=len(a) #Number of problems
    finished = False
    flipcounter =0 #Counter of flips
    trycounter = 1 #Counter of tries
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
                if (random.uniform(0,1) <= propability): # propability for greedy step
                    for x in range(N):
                        truthtable[x] = not truthtable[x] #find score for each possible flip
                        scoreperflip[x] = return_score(a,P,truthtable)
                        truthtable[x] = not truthtable[x]
                
                    lowscore = scoreperflip[0]
                    tempx = 0
                    for x in range(N):
                        if (scoreperflip[x] < lowscore):#find best score
                            lowscore = scoreperflip[x]
                            tempx = x
                        if (scoreperflip[x] == currentscore):#fill sidestep array in any case
                            sidestep.append(x)
                    if (lowscore < currentscore):#if best score is better than current flip
                        truthtable[tempx] = not truthtable[tempx]
                        flipcounter+=1
                    else: #else random sidestep
                        luckyx = sidestep[random.randint(0,len(sidestep)-1)]
                        truthtable[luckyx] = not truthtable[luckyx]
                        flipcounter+=1
                else: #propability for random step here (1-p)low chance
                    index = falseIndex(a,P,truthtable) #find random index from clause that is false
                    truthtable[index] = not truthtable[index] #flip it
                    flipcounter+=1 #flipcounter++

        print("try #",trycounter," variables flipped: ",flipcounter,"Total cost: ",currentscore)
        trycounter+=1
        flipcounter = 0
                    
    if(finished):
        print("Model found:\n",truthtable,"\n Total cost: ",currentscore)
    else:
        print("No model found!!! \n")
                   

def falseIndex(a,P,truthtable):#find random index from clause that is false
    indexes = []
    trueclause = False

    #same code as return_score to detect false clause
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

        #at false clause append its literals to index list
        if( trueclause == False):
            for c in range(3):
                if (a[r][c]<0):
                    indexes.append(-(a[r][c])) #flip index if its negative
                else:
                    indexes.append(a[r][c]) #appends indexes from false clause to list
            return (indexes[(random.randint(0,len(indexes)-1))]-1) #returns random element from list
        


def return_score(a,P,truthtable):
    #1 point for each false clause
    score = 0
    trueclause = False
    for r in range(P): #for each problem if at least one literal is true -> clause true
        trueclause = False #make the trueclause False for the next literal
        for c in range(3):
            slot1 = a[r][c] #slot -> -1 1 6 ktlp

            if (slot1 > 0):
                if (truthtable[(a[r][c])-1] == True):#check if literal coresponds to truth table
                    trueclause = True
            else:
                if (truthtable[((-a[r][c]))-1] == False):
                    trueclause = True
        if( trueclause == False):
            score+=1 #count score of the line in the table

    return score
        

    


    