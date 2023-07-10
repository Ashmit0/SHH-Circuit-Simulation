#!/Users/ashmitbathla/opt/anaconda3/bin/python3
import sys 
import math
import numpy as np 

# generates the netlist code for the SHH-circuit with userspecified 't' and unit cell count
node_count = int( sys.argv[1] ) 
# 'node_count' variable must be a even number 
# node_count == 2 --> signifies a unit cell  of the transitional lattice 
# total number of unitcells --> node_count/2 
if node_count < 2 or node_count % 2 != 0 : 
    sys.exit( 1 )
t = float( sys.argv[2] )

ini_stdout = sys.stdout
c1 = 1e-7
c2 =  c1/t     
l = '1e-05' 


filename = 'file' + str( int(10*t) ) + '.cir'
op_w = 1/( 2*math.pi*math.sqrt( (1e-5)*(c1 + c2)))
# creates and save the code into a cir file which is later run to simulate the circuit
with open( filename , 'w') as f :
    sys.stdout = f  
    print( '*SSH circuit netlist with N =' , str( node_count ) , '\n')
    print('*sources')
    print('I1 1 10 AC 1\n')
    # print('I1 1 9 SINE(0 1' , str(op_w) , ')\n' )
    print('*capacitors')
    print('cb1 1 0 ' , str(c2)  , 'Rser=0 Lser=0 Rpar=0 Cpar=0')
    for i in range( 1 , node_count  ):
        if i % 2 == 0 :
            print( 'c' + str(i), str(i) , str(i+1) , str( c2 ) , 'Rser=0 Lser=0 Rpar=0 Cpar=0' )
        else :
            print( 'c' + str(i) , str(i), str(i+1) , str( c1 ) , 'Rser=0 Lser=0 Rpar=0 Cpar=0' )
    print('cb2', str(node_count), ' 0 ' , str(c2) , 'Rser=0 Lser=0 Rpar=0 Cpar=0')
    print('\n *inductors')
    for i in range( 1 , node_count +1): 
        print( 'l'+ str(i), str(i) , '0' , l , 'Rser=0 Rpar=0 Cpar=0' ) 
    print('\n * directive ')
    print('.ac lin 100000000' , str( 0.7*( op_w )) , str( 1.3*( op_w )))
    # print('.ac dec 1000 1 1e8')
    # print('.tran' , str( 50e-3 ))
    # print('.tran' , str( 10/op_w))
    print('.end')
    sys.stdout = ini_stdout 