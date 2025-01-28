#import libraries
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import os

physicsClient = p.connect(p.GUI)    #Connecting to physics engine
p.setAdditionalSearchPath(pybullet_data.getDataPath())  #To load URDF files i think

planeId = p.loadURDF("plane.urdf")  #create floor
robotId = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)  #set gravity to -9.8

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)    #Create vector for detection
frontLegSensorValues = numpy.zeros(1000)

for i in range(0,1000):
  p.stepSimulation()
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") #Checks for touch on BackLeg
  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  time.sleep(1/60)

file_path = os.path.join("data", "backLegSensorValues.npy")
numpy.save(file_path, backLegSensorValues)

file_path = os.path.join("data", "frontLegSensorValues.npy")
numpy.save(file_path, frontLegSensorValues)

p.disconnect()
