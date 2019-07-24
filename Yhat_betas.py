# Betas and Yhat

import pandas as pd
import numpy as np
from numpy.linalg import inv

def Yhat_betas(Y,Z):
 beta = np.matmul(inv(np.matmul(Z.T,Z)),df.dot(Z).T).T 
 Yhat = beta.dot(Z.T)
 return(beta,Yhat)
