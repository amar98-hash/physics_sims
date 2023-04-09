import numpy as np
import math as mth





def calc_mag(i,j,k):
    if i==0 and j==0 and k==0:
        return 1
    else:
        return mth.sqrt(i*i+j*j+k*k)

N = 5 # size of the array
vectors = np.empty((N, N, N, 3)) # create empty array to hold vectors

# fill the array with vectors
for i in range(N):
    for j in range(N):
        for k in range(N):
            
            mag= calc_mag(i,j,k)
            vectors[i, j, k] = [i/mag, j/mag, k/mag]

print(vectors[0,0,0])




    

