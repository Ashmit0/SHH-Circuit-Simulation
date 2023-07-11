import numpy as np 
import pandas as pd
import sys , math , os
import PyLTSpice as spice
import matplotlib.pyplot as plt 

c1 = 1e-7   
l = '1e-05'
ini_stdout = sys.stdout

def print_netlist( t , N ):
    c2 = c1 / t 
    resonance_w = 1/( 2*math.pi*math.sqrt( (1e-5)*(c1 + c2)))
    
    filename = 'file.net'
    with open( filename , 'w') as f :
        sys.stdout = f  
        print( '*SSH circuit netlist with N =' ,\
        str( N ) , '\n')
        print('*sources')
        print('I1 1 10 AC 1\n')
        # print('I1 1 9 SINE(0 1' , str(op_w) , ')\n' )
        print('*capacitors')
        print('Cb1 1 0 ' , str(c2)  , \
            'Rser=0 Lser=0 Rpar=0 Cpar=0')
        for i in range( 1 , N  ):
            if i % 2 == 0 :
                print( 'C' + str(i), str(i) ,\
                    str(i+1) , str( c2 ) , \
                        'Rser=0 Lser=0 Rpar=0 Cpar=0' )
            else :
                print( 'C' + str(i) , str(i), str(i+1) , \
                    str( c1 ) , 'Rser=0 Lser=0 Rpar=0 Cpar=0' )
        print('Cb2', str(N), ' 0 ' , str(c2) , \
            'Rser=0 Lser=0 Rpar=0 Cpar=0')
        print('\n *inductors')
        for i in range( 1 , N +1): 
            print( 'L'+ str(i), str(i) , '0' ,\
                l , 'Rser=0 Rpar=0 Cpar=0' ) 
        print('\n * directive ')
        # print('.ac lin 100000000' , str( 0.7*( resonance_w)) ,  str( 1.3*( resonance_w )))
        # print('.ac dec 1000 1 1e8')
        # print('.tran' , str( 50e-3 ))
        # print('.tran' , str( 10/op_w))
        print('.end')
        sys.stdout = ini_stdout



def extract_data( tList , N ):
    data = pd.DataFrame()
    data['freq'] = np.linspace(0.8 , 1.2 , 100000)
    runner = spice.SimRunner()
    net = spice.SpiceEditor('file.net')
    for t in tList:
        c2 = c1/t 
        for i in np.arange(2,10,2):
            capName = 'C' + str(i)
            net.set_component_value(capName , str(c2))
        net.set_component_value('Cb1' , str(c2))
        net.set_component_value('Cb2' , str(c2))
        rFreq = 1/(2*math.pi*math.sqrt(1e-5*( c1 + c2)))
        sweepRange = [ str( 0.8*rFreq) , str(1.2*rFreq)]
        trace = [ 'V(1)' , 'V(' + str(N) + ')' ]
        net.add_instructions( '*Directive' , '.ac lin 100000'  \
            + sweepRange[0] + ' ' + sweepRange[1])
        net.write_netlist('Rfile.net')
        raw , log = runner.run_now( net , switches=None, run_filename='Rfile.net')
        rawData = spice.RawRead('Rfile.raw' , traces_to_read= trace )
        subData = rawData.to_dataframe()
        data[str(t)] = np.absolute( subData[trace[0]] - subData[trace[1]])
        net.reset_netlist()
    os.remove('Rfile.log')
    os.remove('Rfile.net')
    os.remove('file.net')
    os.remove('Rfile.op.raw')
    os.remove('Rfile.raw')
    os.remove('SpiceBatch.log')
    return data


print_netlist( 1 , 10 )
data = extract_data( [.1,.2,.3,.5,1.2,1.5], 10 )
data.to_csv("data.csv")