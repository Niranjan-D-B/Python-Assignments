#Author: Niranjan D B 

def Avg(*args):
    '''Provide a number of integer/Float values to calculate the average of given numbers.
If no values are given, then None is return.
        Ex: input--> (1,2,3,4.0)
            Output--> 2.5'''
    x=0
    if(len(args))==0:
        return None        #Here Value error will not be excecuted. Expected to return None when no inputs.
        raise ValueError("Expecte atleast an integer/float Value to return the average")
    
    else:
        for i in range(len(args)):
            x+=args[i]
        x=x/(i+1)
        return x

