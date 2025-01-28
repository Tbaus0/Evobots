import pyrosim.pyrosim as pyrosim



def Create_World():
    
    
    pyrosim.Start_SDF("world.sdf")  #start new SDF file
    
    #Cube initial Position
    x = 2
    y = 2
    z = 0.5

    #Setting initial block size
    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width ,height])
    
    pyrosim.End()

def Create_Robot():
    
    #Robot initial Position
    x = 0
    y = 0
    z = 0.5

    #Setting initial Torso size
    length = 1
    width = 1
    height = 1

    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name="0", pos=[x,y,z] , size=[length, width ,height])
    pyrosim.Send_Joint( name = "0_1" , parent= "0" , child = "1" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="1", pos=[0,0,0.5] , size=[length, width ,height])
    pyrosim.Send_Joint( name = "1_2" , parent= "1" , child = "2" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="2", pos=[0,0,0.5] , size=[length, width ,height])
    pyrosim.Send_Joint( name = "2_3" , parent= "2" , child = "3" , type = "revolute", position = [0,0.5,0.5])
    pyrosim.Send_Cube(name="3", pos=[0,0.5,0] , size=[length, width ,height])
    pyrosim.Send_Joint( name = "3_4" , parent= "3" , child = "4" , type = "revolute", position = [0,0.5,0])
    pyrosim.Send_Cube(name="4", pos=[0,0.5,0] , size=[length, width ,height])
    pyrosim.Send_Joint( name = "4_5" , parent= "4" , child = "5" , type = "revolute", position = [0,0.5,-0.5])
    pyrosim.Send_Cube(name="5", pos=[0,0,-0.5] , size=[length, width ,height])
    pyrosim.Send_Joint( name = "5_6" , parent= "5" , child = "6" , type = "revolute", position = [0,0,-1])
    pyrosim.Send_Cube(name="6", pos=[0,0,-0.5] , size=[length, width ,height])

    pyrosim.End()
    

Create_World()
Create_Robot()