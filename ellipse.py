from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import math
#%matplotlib inline

nx=251
ny=201
nt=10000

h=200.0/(ny-1)
x = np.linspace(0,250,nx)
y = np.linspace(-100,100,ny)
X,Y = np.meshgrid(x,y)
u=0.3
dy=5

# u = np.zeros((ny, nx))
# v = np.zeros((ny, nx))
c = np.zeros((ny, nx))

def solvePde(nt,c,h,ny,u,dy):
    uc=np.empty_like(c)

    for n in range(nt):
        uc=c.copy()
        temp=u/dy
        c[1:-1,1:-1]=h/4*(temp*uc[1:-1,2:]-temp*uc[1:-1,0:-2])-1/2*(uc[2:,1:-1]+uc[0:-2,1:-1])

        c[0,:]=0
        c[-1,:]=0
        c[:,-1]=0
        start=(ny-1)*70/200.0+1
        end=start+(ny-1)*60/200.0
        c[start:end,0]=37.73
        c[0:start,0]=y[0:start]*0.539+53.9
        c[end:-1,0]=y[end:-1]*(-0.539)+53.9
        # c[0:start,0]=0
        # c[end:-1,0]=0
    return c

cc=solvePde(nt,c,h,ny,u,dy)
fig=plt.figure(figsize=(11,7), dpi=100)
plt.contourf(X,Y,cc,alpha=0.5)    ###plnttong the pressure field as a contour
plt.colorbar()
# plt.contour(X,Y,cc)
plt.xlabel('X')
plt.ylabel('Y');
plt.show()
