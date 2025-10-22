import random,csv
def trigen(p1,p2,p3):
    while True:
        a=random.uniform(0,1)
        b=random.uniform(0,1-a)
        c=1-a-b
        yield ((a*p1[0]+b*p2[0]+c*p3[0]),(a*p1[1]+b*p2[1]+c*p3[1]),(a*p1[2]+b*p2[2]+c*p3[2]))
tri1=trigen([0,0,0], [1,0,0], [1,1,0])
#print(next(tri1))
with open('D:/Learning/Coding/Python/tri.csv', mode='w', newline='') as file:
    writer = csv.writer(file)  # Move outside loop
    for i in range(10000):
        r = next(tri1)
        writer.writerow(r)  # Use writerow instead of writerows
