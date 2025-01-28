import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxs.sdf")

#Cube Position
x = 0
y = 0.5
z = 0

#Setting block size
length = 1
width = 1
height = 1

#Generating cube1
pyrosim.Send_Cube(name="Box", pos=[x,z,y] , size=[length,width,height])
#Generate cube 2
pyrosim.Send_Cube(name="Box2", pos=[1,0,1.5] , size=[1,1,1])

pyrosim.End()
