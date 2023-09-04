import pandas as pd 
import matplotlib.pyplot as plt 
plt.style.use('style.mplstyle')
data = pd.read_csv("data.csv")
data.drop('s',axis = 1 , inplace = True )
# data.plot( x = 'freq' , y = data.columns.delete(0))
# plt.xlabel( r'$\omega_0/\omega$' )
# plt.ylabel( r'$Z^{1,2N}_{SHH}$')
# plt.yscale('log')
# plt.show()

print( data.iloc[110000].to_numpy()  )
plt.scatter( x = [ 1 , 2  ,3 ] , y = data.iloc[110000].to_numpy()  )
plt.plot(  [ 1 , 2 ,3 ] ,  data.iloc[110000].to_numpy())
plt.show()