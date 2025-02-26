# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:41:03 2025

@author: Thomas Bausman
"""
#import libraries

import pybullet as p
import pybullet_data

class WORLD:
    def __init__(self):
        self. physicsClient = p.connect(p.GUI)    #Connecting to physics engine
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  #To load URDF files i think
        
        self.planeId = p.loadURDF("plane.urdf")   #create floor
        p.loadSDF("world.sdf")