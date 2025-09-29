#Author Niranjan D B
import time
def decorator(funcpointer):
    def innerfunction(*args,**kwds):
        a=time.time()
        f= funcpointer(*args,**kwds)
        b=time.time()
        return(b-a,f)
    return innerfunction

def logwriting(funcpointer):
    def innerfunction(*args,**kwds):
        with open("D:/Learning/Coding/Python/log.txt",'w') as file:
            file.write("Function started...\nTime Taken to execute the given function is ")
            file.write(str(funcpointer(*args,**kwds)[0]))
            file.write("\nOutput of the given function is ")
            file.write(str(funcpointer(*args,**kwds)[1]))
            file.write("\nFunction Completed...")
    return innerfunction

@logwriting
@decorator
def Avg(*args):
    if(len(args))==0:
        return None        #Here Value error will not be excecuted. Expected to return None when no inputs.
        raise ValueError("Expecte atleast an integer/float Value to return the average")
    
    else:
        return sum(args)/len(args)
