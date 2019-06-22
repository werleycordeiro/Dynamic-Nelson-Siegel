# author: Werley Cordeiro
# werleycordeiro@gmail.com

# Lib
python -m pip install --user numpy pandas matplotlib # cmd

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

def Nelson_Siegel_factor_loadings(lam,m):
 c1 = np.ones(m.shape[0])
 c2 = (1-np.exp(-lam*m))/(lam*m)
 c3 = c2-np.exp(-lam*m)
 lambmat = np.vstack((c1,c2,c3)).T
 return(lambmat)

z = Nelson_Siegel_factor_loadings(lam=lam,m=m)

# Betas and Yhat

from numpy.linalg import inv

def Yhat_betas(Y,Z):
 beta = np.matmul(inv(np.matmul(z.T,z)),df.dot(z).T).T 
 Yhat = beta.dot(z.T)
 return(beta,Yhat)
