#!/Users/ashmitbathla/opt/anaconda3/bin/python3
import sys 
import math
import numpy as np 
import netlist

N = int( sys.argv[1] ) 
if N < 2 or N % 2 != 0 : 
    sys.exit( 1 ) 
t = float( sys.argv[2] )
# 'N' variable must be a even number \
    # N == 2 --> signifies a unit cell  of  the \
        # transitional lattice 
        
netlist.print_lin_netlist( t , N ) 