from simplex import *

if __name__ == "__main__":
    m = gen_matrix(2,2)
    constrain(m,'2,-1,G,10')
    constrain(m,'1,1,L,20')
    obj(m,'5,10,0')
    print(maxz(m))
    m = gen_matrix(2,4)
    constrain(m,'2,5,G,30')
    constrain(m,'-3,5,G,5')
    constrain(m,'8,3,L,85')
    constrain(m,'-9,7,L,42')
    obj(m,'2,7,0')
    print(minz(m))