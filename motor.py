# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:49:00 2025

@author: Thomas Bausman
"""
import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet as p


class MOTOR:
    def __init__(self, jointName: str):
        
        self.jointName = jointName #labeling self with a name kinda
        self.Prepare_To_Act()
        
    def Prepare_To_Act(self):
        
        
        self.amplitude = np.pi/4
        self.frequency = 8
        self.offset = 0
        
        x = np.linspace(0, 2 * np.pi, 1000)
        self.motorValues = self.amplitude * np.sin(self.frequency * x + self.offset)
        

    def Get_Value(self, desiredAngle, robot):
        
        pyrosim.Set_Motor_For_Joint(  #Back Leg

        bodyIndex = robot,  #telling simulator which robot we are acting on

        jointName = self.jointName,  #What joint the motor will be acting on

        controlMode = p.POSITION_CONTROL,  #determines how the motor will attempt to control the motion of the joint

        targetPosition = desiredAngle,   #angle in radians we want the arm to have

        maxForce = 250)
        
    def Save_Values(self):
        np.save(f'data/Motor_Data_{self.jointName}.npy', self.motorValues)