import defs, move
 
def game():
    pits,numLines=defs.difficulty()
    print pits, numLines
    x=0
    y=0
    moves=[]
    while True:
        defs.clear()
        x=defs.val(x,numLines)
        y=defs.val(y,numLines)
        #print (x+1,y+1)
        if (x,y) in pits:
            defs.loser(x,y,numLines,moves,pits)
            if defs.retry():
                game()
            break
        if (x,y)==(numLines-1,numLines-1):
            defs.winner(x,y,numLines,moves,pits)
            if defs.retry():
                game()
            break
        defs.printBoard('x',x,y,numLines,moves)
        print ''
        moves.append([x,y])
        x,y=move.command(x,y)
        if x==-100:
            break
    return
 
game()
