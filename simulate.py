#import libraries
import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)    #Connecting to physics engine
p.setAdditionalSearchPath(pybullet_data.getDataPath())  #To load URDF files i think

planeId = p.loadURDF("plane.urdf")  #create floor
p.setGravity(0,0,-9.8)  #set gravity to -9.8

p.loadSDF("boxs.sdf")

for i in range(0,1000):
  p.stepSimulation()
  time.sleep(1/60)
  print(i)

p.disconnect()
