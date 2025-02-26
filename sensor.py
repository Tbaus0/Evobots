# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:49:00 2025

@author: Thomas Bausman
"""
import pyrosim.pyrosim as pyrosim
import numpy as np


class SENSOR:
    def __init__(self, linkName: str):
        
        self.linkName = linkName
        
        self.values = np.zeros(1000)    #Create vector for detection
        
    def Get_Value(self,step: int):
        
        self.values[step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
        if step+1 == len(self.values):
            print(self.values)
            
    def Save_Values(self):

        np.save(f'data/Sensor_Data_{self.linkName}.npy', self.values)