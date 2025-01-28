import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxs.sdf")

#Cube initial Position
x_i = -2.5
y = 0.5
z = -3

#Setting initial block size
length = 1
width = 1
height = 1
for j in range(0,5):
    z += 1
    for i in range(0,5):
        x = x_i + (1*i)
        #Generating cube tower
        for p in range(0,10): 
            jump = pow(0.9,p)
            pyrosim.Send_Cube(name="Box", pos=[x,z,y+p] , size=[length * jump ,width * jump ,height * jump])
    x = x_i
pyrosim.End()
