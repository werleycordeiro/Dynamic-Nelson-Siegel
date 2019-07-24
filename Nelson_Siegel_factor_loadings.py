#Loading matrix

import numpy as np

def Nelson_Siegel_factor_loadings(lam,matu):
 c1 = np.ones(matu.shape[0])
 c2 = (1-np.exp(-lam*matu))/(lam*matu)
 c3 = c2-np.exp(-lam*matu)
 lambmat = np.vstack((c1,c2,c3)).T
 return(lambmat)
