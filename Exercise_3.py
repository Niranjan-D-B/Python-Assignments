#Author Niranjan D B
import time,os

if os.path.exists("D:/Learning/Coding/Python/log.txt"):
            os.remove("D:/Learning/Coding/Python/log.txt")


def decorator(funcpointer):
    def innerfunction(*args,**kwds):
        a=time.time()
        f=funcpointer(*args,**kwds)
        b=time.time()
        print("Time Taken to execute the function is ",b-a)
        return f
    return innerfunction

def logwriting(funcpointer):
    def innerfunction(*args,**kwds):
        with open("D:/Learning/Coding/Python/log.txt",'a') as file:
            file.write("Function started...\nOutput of the given function is ")
            z=funcpointer(*args,**kwds)
            file.write(str(z))
            file.write("\nFunction Completed...\n\n")
            return z
    return innerfunction

@logwriting
@decorator
def Avg(*args):
    if(len(args))==0:
        return None
        raise ValueError("Expected atleast an integer/float Value to return the average")
    
    else:
        return sum(args)/len(args)
