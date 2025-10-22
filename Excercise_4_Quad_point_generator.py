import random,csv
def trigen(p1,p2,p3):
        while True:
                a=random.uniform(0,1)
                b=random.uniform(0,1-a)
                c=1-a-b
                yield ((a*p1[0]+b*p2[0]+c*p3[0]),(a*p1[1]+b*p2[1]+c*p3[1]),(a*p1[2]+b*p2[2]+c*p3[2]))

def area(p1,p2,p3):
        x1, y1 ,z1 = p1
        x2, y2 ,z2 = p2
        x3, y3, z3 = p3
        Area = 0.5 * abs(x1 * (y2 - y3) +x2 * (y3 - y1) +x3 * (y1 - y2))
        return Area

def mid_point(p1,p2,p3,p4):
        if area(p1,p2,p3)+area(p1,p2,p4)+area(p1,p3,p4)==area(p2,p3,p4):
                return p1
        elif area(p2,p3,p4)+area(p2,p3,p1)+area(p2,p4,p1)==area(p1,p3,p4):
                return p2
        elif area(p3,p4,p1)+area(p3,p4,p2)+area(p3,p1,p2)==area(p4,p1,p2):
                return p3
        elif area(p4,p1,p2)+area(p4,p1,p3)+area(p4,p2,p3)==area(p2,p3,p1):
                return p4
        else:
                return 0
def Quad_point(p1,p2,p3,p4):
        mid= mid_point(p1,p2,p3,p4)
        if mid==0 :
                while True:
                        a=random.uniform(0,1)
                        b=random.uniform(0,1-a)
                        c=random.uniform(0,1-a-b)
                        d=1-a-b-c
                        yield ((a*p1[0]+b*p2[0]+c*p3[0]+d*p4[0]),(a*p1[1]+b*p2[1]+c*p3[1]+d*p4[1]),(a*p1[2]+b*p2[2]+c*p3[2]+d*p4[2]))
                
        else:
                if mid==p1 or mid==p3:
                        tri1=trigen(p1,p3,p4)
                        tri2=trigen(p1,p3,p2)
                                #print("if part \n")
                else:
                        tri1=trigen(p2,p4,p1)
                        tri2=trigen(p2,p4,p3)
                while True:
                        #print("Hey hi")
                        yield(next(tri1))
                        yield(next(tri2))
                                #print("else part \n")
with open('D:/Learning/Coding/Python/Quad.csv', mode='w', newline='') as file:
    writer = csv.writer(file)  # Move outside loop
    pt = Quad_point((0,0,0),(-1,-1,0),(0,1,0),(1,-1,0))
    for i in range(10000):
        writer.writerow(next(pt))
