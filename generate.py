import pyrosim.pyrosim as pyrosim



def Generate_Body():
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
    
def Generate_Brain():
    
    pyrosim.Start_NeuralNetwork("brain.nndf")  #start new nndf, for a neural network description format file, specific to pyrosim
    
    #Create a sensor neuron
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    
    #Create a motor neuron
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "BackLeg_Torso")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 0.7 )  #Generate a synapse
    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = -1 )
    
    pyrosim.End()
    

Generate_Body()
Generate_Brain()