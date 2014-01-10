import random, os
 
def val(n,length):
    if n<0:
        return 0
    if n>length-1:
        return length-1
    return n
 
def createPits(numPits,numLines):
    pits=[]
    while len(pits)<numPits:
        xp=random.randrange(0,numLines)
        yp=random.randrange(0,numLines)
        #print (xp,yp)
        if (xp,yp) in pits:
            pass
        elif (xp,yp)==(0,0):
            pass
        elif (xp,yp)==(numLines-1,numLines-1):
            pass
        else:
            pits.append((xp,yp))
    return pits
 
def printBoard(character,x,y,numPits,moves,pits=[],flag=None):
    for i in range(numPits):
        line='-'*numPits
        if i==numPits-1:
            line=line[:-1]+'D'
        for move in moves:
            if move[1]==i:
                line=line[:move[0]]+' '+line[move[0]+1:]
        if y==i:
            line=line[:x]+character+line[x+1:]
        if flag=='end':
            for (xp,yp) in pits:
                if yp==i:
                    line=line[:xp]+'O'+line[xp+1:]
                if i==numPits-1:
                    line=line[:-1]+'D'
        print line
 
def winner(x,y,numPits,moves,pits):
    print 'You made it to the door!!!\n'
    printBoard('D',x,y,numPits,moves,pits=pits,flag='end')
    print ''
    print 'YOU WIN!!!'
    return
     
def loser(x,y,numPits,moves,pits):
    print 'You fell in the pit!\n'
    printBoard('O',x,y,numPits,moves,pits=pits,flag='end')
    print ''
    print 'Game Over.  Good Bye.'
    return
 
def difficulty():
    clear()
    diff=raw_input('Choose difficulty:\n'
                    '(E)asy\n'
                    '(M)edium\n'
                    '(H)ard\n'
                    '(I)mpossible\n'
                    ':')
    diff=diff.lower()
    diffDict= {'e':[3,10],'m':[8,15],'h':[20,20],'i':[50,30]}
    if diff not in diffDict:
        return difficulty()
    return createPits(diffDict[diff][0],diffDict[diff][1]),diffDict[diff][1]
 
def lineCreate(character,x,y,numPits,pits):
    line='-'*numPits
    if y==i:
        line=line[:x]+character+line[x+1:]
    if i==numPits-1:
        line=line[:-1]+'D'
    return line
 
def clear():
    try:
        os.system('clear')
    except:
        os.system('cls')
    return
 
def retry():
    while True:
        retry=raw_input('Do you want to try again? (Y)es or (N)o?\n'
                        ':')
        retry=retry.lower()
        if retry=='y':
            return True
        if retry=='n':
            return False
