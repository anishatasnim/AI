import random
x1=[9,8,7,6,5,4,3,2]
x2=[6,5,9,8,3,2,5,4]
x3=[3,2,5,4,7,6,9,8]
x4=[2,1,6,5,7,6,5,4]

def fitness(x):
    return ((x[0]-x[1])+(x[2]-x[3])+(x[4]-x[5])+(x[6]-x[7]))
f1=(fitness(x1))
f2=(fitness(x2))
f3=(fitness(x3))
f4=(fitness(x4))
print (f1,f2,f3,f4)


def probability(f):
      total=(f1+f2+f3+f4)
      return (f/total)
print(probability(f1))
print(probability(f2))
print(probability(f3))
print(probability(f4))

def selection():
##    x1:[0-0.25]
##    x2:[0.25-0.50]
##    x3:[0.50-0.75]
##    x4:[0.75-1.00]
    r=random.uniform(0.0,1.0)
    print (r)
    if r>0 and r<0.25:
        return x1
    elif r>=0.25 and r<0.50:
        return x2
    elif r>=0.50 and r<0.75:
        return x3
    elif r>=0.75 and r<=1.00:
        return x4
print (selection())



