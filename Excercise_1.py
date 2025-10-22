#Author Niranjan D B

def Vertex(ord1,ord2,ord3):
    x1=float(ord1[0])
    y1=float(ord1[1])
    z1=float(ord1[2])
    x2=float(ord2[0])
    y2=float(ord2[1])
    z2=float(ord2[2])
    x3=float(ord3[0])
    y3=float(ord3[1])
    z3=float(ord3[2])
    a=(((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2))**0.5
    b=(((x2-x3)**2) + ((y2-y3)**2) + ((z2-z3)**2))**0.5
    c=(((x3-x1)**2) + ((y3-y1)**2) + ((z3-z1)**2))**0.5
    d= Area(a,b,c)
    return d
    
def Area(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return area

def Volume(Normal,area,field):
    #print('centroid:',(cent),'Normal:',Normal)
    #field=[(cent[0])/3+ (cent[1]**2)*(cent[2]**2), (cent[1])/3 + (cent[2]**2)*(cent[0]**2) , (cent[2])/3 + (cent[0]**2)*( cent[1]**2)]
    fn=0
    for i in range(len(field)):
        fn+= field[i]* float(Normal[i])
    vol=fn * area
    #print("Fn",fn,"volume",vol)
    return vol

def Centroid(v1,v2,v3):
    cen=[]
    a=zip(v1,v2,v3)
    for i in a:
        c=0
        for j in i:
            c+=float(j)
        cen.append(c/len(i))
    return cen

Surface_area=0
Total_volume=0
file=open('myTet 9.stl','r')
list_nor=[]
f=file.readlines()
list_ver=[]

for i in range(1,len(f)-1):
    if(i%7==3 or i%7==4 or i%7==5):
        d=f[i].strip("vertex ")
        d=d.rstrip('\n')
        vertex1=d.split(' ')
        list_ver.append(vertex1)
    elif(i%7==1):
        e=f[i].strip("facet normal ")
        e=e.rstrip('\n')
        e=e.split(' ')
        list_nor.append(e)
#for i in list_ver:
#   print(i)
for i in range(0,len(list_ver),3):
    vert1=list_ver[i]
    vert2=list_ver[i+1]
    vert3=list_ver[i+2]
    area=Vertex(vert1,vert2,vert3)
    Surface_area=Surface_area+ area
    Total_volume+=Volume(list_nor[i//3],area,Centroid(vert1,vert2,vert3))/3
    
print('Total area:',Surface_area,'\t Total volume:',Total_volume)

#print("Total area:{:.4f}".format(Surface_area),"Total Volume:{:.4f}".format(Total_volume),sep='\n')
file.close()
