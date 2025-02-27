# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:37:12 2025

@author: Thomas Bausman
"""
#import libraries
from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import constants as c


class SIMULATION:
    def __init__(self):
        
        self.world = WORLD()
        self.robot = ROBOT()
        
        p.setGravity(0,0,c.gravity)  #set gravity to -9.8
        
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
        
        
    def Run(self):
        for i in range(0,1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
          
            time.sleep(1/100)
        self.robot.Save()
    
    def __del__(self):

        p.disconnect()