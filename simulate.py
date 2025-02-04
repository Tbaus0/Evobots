#import libraries
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import os
#import random

physicsClient = p.connect(p.GUI)    #Connecting to physics engine
p.setAdditionalSearchPath(pybullet_data.getDataPath())  #To load URDF files i think

planeId = p.loadURDF("plane.urdf")  #create floor
robotId = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)  #set gravity to -9.8

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)    #Create vector for detection
frontLegSensorValues = np.zeros(1000)

#Back Leg movement
backLeg_amplitude = 0
backLeg_frequency = 10
backLeg_phaseOffset = 0

backLeg_x = np.linspace(0, 2 * np.pi, 1000)
backLeg_targetAngles = backLeg_amplitude * np.sin(backLeg_frequency * backLeg_x + backLeg_phaseOffset)

#Front Leg movement
frontLeg_amplitude = -(np.pi/4)
frontLeg_frequency = 6
frontLeg_phaseOffset = np.pi

frontLeg_x = np.linspace(0, 2 * np.pi, 1000)
frontLeg_targetAngles = frontLeg_amplitude * np.sin(frontLeg_frequency * frontLeg_x + frontLeg_phaseOffset)

file_path = os.path.join("data", "backLeg_targetAngles.npy")
np.save(file_path, backLeg_targetAngles)

# file_path = os.path.join("data", "frontLeg_targetAngles.npy")
# np.save(file_path, frontLeg_targetAngles)

# exit()
for i in range(0,1000):
  p.stepSimulation()
  
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") #Checks for touch on BackLeg
  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  
  pyrosim.Set_Motor_For_Joint(  #Back Leg

      bodyIndex = robotId,  #telling simulator we are simulating a robot named: robotId

    jointName = b'BackLeg_Torso',  #What joint the motor will be acting on

    controlMode = p.POSITION_CONTROL,  #determines how the motor will attempt to control the motion of the joint

    targetPosition = backLeg_targetAngles[i],   #angle in radians we want the arm to have

    maxForce = 250)
  
  pyrosim.Set_Motor_For_Joint(  #Front Leg

      bodyIndex = robotId,  #telling simulator we are simulating a robot named: robotId

    jointName = b'Torso_FrontLeg',  #What joint the motor will be acting on

    controlMode = p.POSITION_CONTROL,  #determines how the motor will attempt to control the motion of the joint

    targetPosition = frontLeg_targetAngles[i],   #angle in radians we want the arm to have

    maxForce = 250)
  
  time.sleep(1/100)

file_path = os.path.join("data", "backLegSensorValues.npy")
np.save(file_path, backLegSensorValues)

file_path = os.path.join("data", "frontLegSensorValues.npy")
np.save(file_path, frontLegSensorValues)

p.disconnect()
