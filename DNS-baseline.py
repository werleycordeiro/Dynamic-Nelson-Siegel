prev = "FALSE";
ahead = 12;
lik = "TRUE";
matu =  np.array([3,6,9,12,15,18,21,24,30,36,48,60,72,84,96,108,120]);

def kalman(para,Y,lik,prev,ahead,matu):
 l = para[0];
 M = ahead;
 
if prev=="TRUE":
  T = Y.shape[0]
  Yf = Y
  Yf.iloc[(T-M):T,] = np.nan
  Y = Y.iloc[1:(T-M),]
  T = Y.shape[0]
else:
  T = Y.shape[0]
    
 
 W = Y.sahpe[1];
 N = 3;
 
 mu = 
  
