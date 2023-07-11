import PyLTSpice as lts 

net = lts.SpiceEditor("file1.net")



for i in range( 1 , 10):
    name = 'C' + str(i)
    net.set_component_value(name , 10 )

# print(net.get_component_nodes('Cb1'))
filename = "file3.net" 
net.write_netlist(filename)
