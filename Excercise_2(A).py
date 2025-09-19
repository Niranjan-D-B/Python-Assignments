#Author: Niranjan D B

def Centroid(*args):
    '''Give a LIST of co-ordinates of any number of 'n' dimensional points to calculate centroid, where n tends to inifinity.
Also, not all points have same dimensions.
        Ex: Input--> ([1,0],[0,0,0],[5,0,0])
            Output --> [2.0, 0.0, 0.0] '''
    a=[]
    c=[]
    d=0
    for i in range(len(args)):
        c.append(len(args[i]))

    for i in range(len(args)):
        for j in range(len(args)):
            if(max(c)>=len(args[j])):
                args[j].append(0)
            d+=args[j][i]
        d=d/(j+1)
        a.append(d)
        d=0
    return a

def Centroid2(*args):
    '''gives centroid of any number of 'n' dimensional points,where n tends to inifinity.
Also, not all points have same dimensions.
        Ex: Input--> ([1,0],[0,0,0],[5,0,0])
            Output --> [2.0, 0.0, 0.0] '''
    b=[]
    import itertools
    a=itertools.zip_longest(*args,fillvalue=0)
    for i in a:
        #print(i)
        b.append(sum(i)/len(i))
    return b



         
    
