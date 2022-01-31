import numpy as np
from random import randint
sqrt = np.sqrt


class Cell():
    def __init__(self,x,y,vx):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = sqrt(v**2-self.vx**2)
        self.color = 0
        self.state = 0  # 0 = susceptible
        self.days = 0 # jours depuis début état
    
    def inc_day(sefl):
        self.days += 1
        
    def change_sate(self):
        self.state += 1
        self.days = 0
        
    def report(self):
        return (self.x, self.y, self.vx, self.vy, self.color, self.days)
    
class Echantillon():        
    def __init__(self,name, n, color):
        self.name = name
        self.color = color
        self.set = []
        for i in range(n):        
            c1 = Cell(randint(1,width),randint(1,height),randint(1,v))
            c1.color = color
            #print(c1.report())
            self.set.append(c1)
            
    def add(self, cell):  # add to group
        cell.state += 1
        if self.name == 'mort' :
            cell.color = 5
        else: cell.color += 1
        self.set.append(cell)
        
    def sub(self, index):
        return self.set.pop(index)

states = ['susceptible', 'infecté', 'hospitalisé', 'réanimé', 'guéri', 'mort']
colors = [(0,0,255), (255,0,255), (255,0,0), (0,255,255), (255,255,255), (0,0,0)]
marks = ['go', 'b^', 'm>', 'rv', 'yD', 'rs']
v = 5
width = 200
height = 200
area = (width, height)
population = 1000
infected = 1
susceptible = population - infected
delay = 7
min = 50

S = Echantillon('susceptible', susceptible,0)
I = Echantillon('infecté', infected,1)
H = Echantillon('hospitalisé',0,2)
R = Echantillon('réanimation',0,3)
G = Echantillon('guéri',0,4)
M = Echantillon('mort',0,5)

sets = (S,I,H,R,G,M)

def trans(s,d,i=None):  # i = None random choice
    if i == None :
        i = randint(0,len(s.set)-1)
    k = s.sub(i)
    d.add(k)
    #print(len(s.set), len(d.set))

# aléatoirement tombé malade
r = randint(min, len(S.set))
for i in range(r):
    trans(S,I)  
# premier infecté
#trans(S,I,0)  
#hospitalisé = min moitié des infectés
r = randint(min/2, len(I.set))
for i in range(r):
    trans(I,H)

# en réanimation
r = randint(1, len(H.set))
for i in range(r):
    trans(H,R)
# guéris
if  len(H.set)>1:
    r = randint(1, len(H.set))
    for i in range(r):
        trans(H,G)    

#mort en réanimation
r = randint(1, len(R.set))
for i in range(r):
    trans(R,M)

for k in range(6):
    print(states[k],len(sets[k].set))

import matplotlib.pyplot as plt
for s in sets:
    #print(s.name, len(s.set))
    if len(s.set) != 0:
        x = []
        y = []
        for i in range(len(s.set)):
            #print(i,end=' ')
            cell = s.set[i]
            color = marks[s.color]
            x.append(cell.x)
            y.append(cell.y)
            #plt.plot(cell.x,cell.y,color)
        #print()
        plt.plot(x,y,color,label=s.name)
plt.legend()
# Place a legend to the right of this smaller subplot.
#plt.legend(bbox_to_anchor=(1.005, 1.0), loc='upper left', borderaxespad=0.)

plt.show()
'''
s = M
for i in range(len(s.set)):
    #print(i,end=' ')
    cell = s.set[i]
    color = marks[cell.color]
    plt.plot(cell.x,cell.y,color)
print()
plt.show()
'''

def distance(c1, c2):
    d = sqrt((c1.x-c2.x)**2 + (c1.y-c2.y)**2)
    return d


Risque = []
d_min = 3
D = []
c1 = I.set[0]
#print(c1.x, c1.y)
plot = False
for i,c in enumerate(S.set):
    #c = I.set[0]
    risque = False
    #print(c.x, c.y)
    if plot : plt.plot(c1.x, c1.y,'ro')
    #plt.plot(c.x, c.y,'ko')
    d = distance(c1, c)
    #print(d)
    if d < d_min :
        risque = True
        Risque.append((i,d))
        if plot : plt.plot(c.x, c.y,'rs')
    else :
        if plot : plt.plot(c.x, c.y,'ko')
    D.append((i,d, risque))
#print(D)
print(Risque)
if plot : plt.show()

