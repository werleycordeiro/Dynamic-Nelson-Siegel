# Betas and Yhat

import pandas as pd
import numpy as np
from numpy.linalg import inv

def Yhat_betas(Y,Z):
 beta = np.matmul(inv(np.matmul(z.T,z)),df.dot(z).T).T 
 Yhat = beta.dot(z.T)
 return(beta,Yhat)
