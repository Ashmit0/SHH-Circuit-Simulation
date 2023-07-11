import sys 
import math
import netlist
import PyLTSpice 
import numpy as np 

sys.argv.pop(0)
N = int( sys.argv.pop(0) ) 
t_list = np.array(  sys.argv , dtype= float )
# creates LTspice netlist for the given N
# netlist.print_lin_netlist( t , N ) 
for t in t_list: 
    netlist.print_lin_netlist(t , N )