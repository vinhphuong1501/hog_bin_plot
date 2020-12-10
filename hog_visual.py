import matplotlib.pyplot as plt
import numpy as np
image=np.random.randint(0,256,size=(10,10))
gx=np.zeros(shape=(8,8))
gy=np.zeros(shape=(8,8))
gra=np.zeros(shape=(8,8))
ori=np.zeros(shape=(8,8))
for i in range (1,9):
    for j in range (1,9):
        gy[i-1,j-1]=image[i+1][j]-image[i-1][j]
        gx[i-1,j-1]=image[i][j+1]-image[i][j-1]
ori=np.arctan2(gy,gx)
gx2=np.square(gx)
gy2=np.square(gy)
tot=np.zeros(shape=(8,8))
tot=np.add(gx2,gy2)
gra=np.sqrt(tot)
ori=np.arctan2(gy,gx)
#print(ori)
for i in range (0,8):
    for j in range (0,8):
        if ori[i][j] <0: ori[i][j]= 3.14 + ori[i][j]
        elif ori[i][j] >3.14: ori[i][j]= ori[i][j] - 3.14
#print(ori)
bins=np.zeros(shape=(9))
for i in range (0,8):
    for j in range (0,8):
        if gra[i][j]==0: continue
        bin0=-1
        bin1=-1
        bin0=int((ori[i][j] - 3.14/18)/(2*3.14/18))
        bin1=bin0+1
        if ori[i][j]<(3.14/18):
            bin0=-1
            bin1=0        
        #print(bin0,bin1)
        bin0center=(bin0*2*3.14/18)+3.14/18
        bin1center=(bin1*2*3.14/18)+3.14/18
        if bin1>8: bin1=-1
        w0=(bin1center-ori[i][j])/(2*3.14/18)
        w1=(ori[i][j]-bin0center)/(2*3.14/18)
        #print(bin0,bin1)
        if bin0>=0: bins[bin0]=gra[i][j]*w0 + bins[bin0]
        if bin1>=0: bins[bin1]=gra[i][j]*w1 + bins[bin1]

plt.figure()
tb = plt.table(cellText=image, loc=(0,0), cellLoc='center')
tb.set_fontsize(18)
tb_props=tb.properties()
tc = tb_props['children']
for cell in tc: 
    cell.set_height(1/8)
    cell.set_width(1/8)

ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])

values=[0,1,2,3,4,5,6,7,8]
fig = plt.figure(figsize = (10, 5))
plt.bar(values, bins, color ='maroon',  width = 0.4)
plt.xlabel("Bin") 
plt.ylabel("Aggregated magnitude") 
plt.title("Histogram of gradients of a cell") 
plt.show()