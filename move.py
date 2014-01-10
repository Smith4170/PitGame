def command(x,y):
    com=raw_input('Up(W), Down(S), Left(A), Right(D) or (E)xit?\n'
                  ':')
    com=com.lower()
    if com=='a':
        return left(x),y
    elif com=='d':
        return right(x),y
    elif com=='w':
        return x,up(y)
    elif com=='s':
        return x,down(y)
    elif com=='e':
        return -100,-100
    else:
        return command(x,y)
 
def left(x):
    x-=1
    return x
 
def right(x):
    x+=1
    return x
 
def up(y):
    y-=1
    return y
 
def down(y):
    y+=1
    return y
