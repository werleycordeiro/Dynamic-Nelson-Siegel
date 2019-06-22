import numpy as np
import pandas as pd
from numpy.linalg import inv 

def VARcoeff(betas,l):
 YY = betas.values # To convert a pandas dataframe to a numpy ndarray
 XX = np.column_stack((np.ones(betas.shape[0]),YY))
 XX = np.delete(XX,(l-1),axis=0)
 YY = np.delete(YY,0,axis=0)
 var= np.matmul(inv(np.matmul(XX.T,XX)),np.matmul(XX.T,YY)).T
 return(var)
