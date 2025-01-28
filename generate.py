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
    x = 0.5
    y = 0
    z = 0.5

    #Setting initial Torso size
    length = 1
    width = 1
    height = 1

    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name="BackLeg", pos=[x,y,z] , size=[length, width ,height])
    pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" , type = "revolute", position = [x+0.5,y,z+0.5])
    pyrosim.Send_Cube(name="Torso", pos=[0.5,y,0.5] , size=[length, width ,height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1,0,0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[length, width ,height])

    pyrosim.End()
    

Create_World()
Create_Robot()