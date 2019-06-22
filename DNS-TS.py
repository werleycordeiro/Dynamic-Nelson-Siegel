# author: Werley Cordeiro
# werleycordeiro@gmail.com

# Lib
python -m pip install --user numpy pandas matplotlib # cmd

import os
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# Data
url = "https://www.dropbox.com/s/inpnlugzkddp42q/bonds.csv?dl=1"
df = pd.read_csv(url,sep=';',index_col=0)
df.head()
df.tail()

l=df.shape[0]

m=np.array([3,6,9,12,15,18,21,24,30,36,48,60,72,84,96,108,120])

T=m.shape[0]

lam=0.0609

#Loading matrix

# os.getcwd()
# os.chdir("")
import Nelson_Siegel_factor_loadings as Nelson_Siegel_factor_loadings 
z = Nelson_Siegel_factor_loadings(lam=lam,m=m)

# Betas and Yhat

import Yhat_betas as Yhat_betas
results = Yhat_betas(Y=df,Z=z)
results[0].head()
results[1].head()

# VAR(1) coeffient matrix

from numpy.linalg import inv 

def VARcoeff(betas,l):
 YY = betas.values # To convert a pandas dataframe to a numpy ndarray
 XX = np.column_stack((np.ones(betas.shape[0]),YY))
 XX = np.delete(XX,(l-1),axis=0)
 YY = np.delete(YY,0,axis=0)
 var= np.matmul(inv(np.matmul(XX.T,XX)),np.matmul(XX.T,YY)).T
 return(var)

var = VARcoeff(betas=results[0],l=l) # Start point to pars$phi in Kalman-Filter-Dynamic-Nelson-Siegel

