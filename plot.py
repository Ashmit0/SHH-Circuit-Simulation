import pandas as pd 
import matplotlib.pyplot as plt 
data = pd.read_csv("data.csv")
data.drop('s',axis = 1 , inplace = True )
data.plot( x = 'freq' , y = data.columns.delete(0))
plt.yscale('log')
plt.show()