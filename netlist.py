import sys 
import math
import numpy as np 

c1 = 1e-7
# c2 =  c1/t     
l = '1e-05'
ini_stdout = sys.stdout

# generates the netlist code for the \ 
    # SHH-circuit with userspecified 't' and unit cell count
# creates and save the code into a cir file \
    # which is later run to simulate the circuit
def print_lin_netlist( t , N ):
    c2 = c1 / t 
    op_w = 1/( 2*math.pi*math.sqrt( (1e-5)*(c1 + c2)))
    
    filename = 'file' + str( int(10*t) ) + '.cir'
    with open( filename , 'w') as f :
        sys.stdout = f  
        print( '*SSH circuit netlist with N =' ,\
        str( N ) , '\n')
        print('*sources')
        print('I1 1 10 AC 1\n')
        # print('I1 1 9 SINE(0 1' , str(op_w) , ')\n' )
        print('*capacitors')
        print('cb1 1 0 ' , str(c2)  , \
            'Rser=0 Lser=0 Rpar=0 Cpar=0')
        for i in range( 1 , N  ):
            if i % 2 == 0 :
                print( 'c' + str(i), str(i) ,\
                    str(i+1) , str( c2 ) , \
                        'Rser=0 Lser=0 Rpar=0 Cpar=0' )
            else :
                print( 'c' + str(i) , str(i), str(i+1) , \
                    str( c1 ) , 'Rser=0 Lser=0 Rpar=0 Cpar=0' )
        print('cb2', str(N), ' 0 ' , str(c2) , \
            'Rser=0 Lser=0 Rpar=0 Cpar=0')
        print('\n *inductors')
        for i in range( 1 , N +1): 
            print( 'l'+ str(i), str(i) , '0' ,\
                l , 'Rser=0 Rpar=0 Cpar=0' ) 
        print('\n * directive ')
        print('.ac lin 100000000' , str( 0.7*( op_w )) , \
            str( 1.3*( op_w )))
        # print('.ac dec 1000 1 1e8')
        # print('.tran' , str( 50e-3 ))
        # print('.tran' , str( 10/op_w))
        print('.end')
        sys.stdout = ini_stdout