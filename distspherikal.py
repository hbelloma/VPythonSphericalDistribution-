from visual import*
from math import*
R=50   #radio de la distribución esférica
#m>0,n>0,ñ>0
m=4   #numero radial (numero de partículas en el radio R,numero de cascarones)
n=50   #numero angular (numero de partículas por  angulo axial (y), número de paralelos)
ñ=50   #número azimuthal (numaro de partículas por angulo azimutal, numero de meridianos)

for u in range (m):
    r=R*u/m
    for v in range (n):
            theta=pi*v/n
            for w in range (ñ):
                phi=2*pi*w/ñ
                x=r*sin(theta)*cos(phi)
                y=r*cos(theta)
                z=r*sin(theta)*sin(phi)
                cum=sphere(pos=(x,y,z),radius= 0.1, color=vector(1,1,1))

#casos partículares   
#m=1 es una esfera  (monopolo) no acepta valores de n,ñ mayores a m

# m=2, n=1, (dipolo)  no acepta valores ñ>m o ñ>n

# m=2  n=3, ñ=1 (cuadrupolo esferico)
#m=2, n=15, ñ=1 (semicirculo y un punto c)
#m=2, n=15, ñ=2 (circulo y un punto central)
#m=2, n=15, ñ=3 (pretzel esferico y un punto central)
#m=2, n=15, ñ=4 (anillos ortogonales y un punto central)
#m=2, n=15, ñ=35(cascaron esferico con n paralelos, ñ meridianos)

#m=3, n=15, ñ=1  (2 semicirculos y un punto=m)
#m=10, n=15, ñ=2 (plano circular radial)
#m=10, n=15, ñ=6 (distribucion esferica radial en sextos)  
#m=25, n=25, ñ=25 (cistribución esférica radial )
