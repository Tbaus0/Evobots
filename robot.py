# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:41:04 2025

@author: Thomas Bausman
"""
from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import numpy as np

class ROBOT:
    
    
    def __init__(self):
        
        
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
        self.nn = NEURAL_NETWORK("brain.nndf")  #Create a neural network of self and add any neurons and synapses from brain.nndf
    
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
        
        # for jointName in pyrosim.jointNamesToIndices: #listing off the links
        #     self.motors[jointName].Get_Value(step,robot)
            
        for neuronName in self.nn.Get_Neuron_Names():
            
            if self.nn.Is_Motor_Neuron(neuronName): #If motor neuron or not
                
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName) # extract the name of the joint to which this motor neuron connects
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                 
                
                for joint in pyrosim.jointNamesToIndices: #listing off the links
                    self.motors[joint].Get_Value(desiredAngle, robot)
                
                print(f'neuron name:{neuronName} joint name:{jointName} value:{desiredAngle}')
                
    def Save(self):
        
        for linkName in pyrosim.linkNamesToIndices: #listing off the links
            self.sensors[linkName].Save_Values()
       
        for jointName in pyrosim.jointNamesToIndices: #listing off the links
            self.motors[jointName].Save_Values()
            
    def Think(self):
        
        self.nn.Update()
        self.nn.Print()