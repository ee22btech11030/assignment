import numpy as np
numb=np.array(np.random.randint(1,7,size=10000))
c=np.sum(np.logical_and(numb<3,numb%2!=0))
print(c/10000)
