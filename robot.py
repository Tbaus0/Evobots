# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:41:04 2025

@author: Thomas Bausman
"""
from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class ROBOT:
    
    
    def __init__(self):
        
        
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
    
    
    def Prepare_To_Sense(self):
        
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices: #listing off the links

            self.sensors[linkName] = SENSOR(linkName)
            
            
    def Sense(self,step: int):
        
        for linkName in pyrosim.linkNamesToIndices: #listing off the links
            self.sensors[linkName].Get_Value(step)

            
    def Prepare_To_Act(self):
        self.motors = {}
        
        for jointName in pyrosim.jointNamesToIndices:
            
            self.motors[jointName] = MOTOR(jointName)
            
            
    def Act(self,step: int):
        
        robot = self.robot
        
        for jointName in pyrosim.jointNamesToIndices: #listing off the links
            self.motors[jointName].Get_Value(step,robot)
            
    def Save(self):
        
        for linkName in pyrosim.linkNamesToIndices: #listing off the links
            self.sensors[linkName].Save_Values()
       
        for jointName in pyrosim.jointNamesToIndices: #listing off the links
            self.motors[jointName].Save_Values()