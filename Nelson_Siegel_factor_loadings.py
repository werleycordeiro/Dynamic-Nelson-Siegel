#Loading matrix

import numpy as np

def Nelson_Siegel_factor_loadings(lam,m):
 c1 = np.ones(m.shape[0])
 c2 = (1-np.exp(-lam*m))/(lam*m)
 c3 = c2-np.exp(-lam*m)
 lambmat = np.vstack((c1,c2,c3)).T
 return(lambmat)
