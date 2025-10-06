def myrange(start,End=None,step=1):
    if End==None:
        End=start
        start=0
    if start>End and step>0:
        raise ValueError
    elif start<End and step<0:
        raise ValueError
    
    if start<End:
        while start<End:
            yield start
            start+=step
    else:
        while start>End:
            yield start
            start+=step
        
