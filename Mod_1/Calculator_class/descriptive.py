#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math
import statistics
# add_data and remove_data should be the only public functions
# for private methods - put it in the __init__ 
# method is performing an action, attributes is pulling info
# private = stuff that's happening in the inside of the class. users do not have access to private functions because they have no reason to use it... only you should be using it.

class Calculator:
    
    def __init__(self, data):
        self.data = sorted(data)
        self.calc_stats()
        
    def add_data(self, new_data):
        self.data.extend(new_data)
        self.calc_stats()
        
    def remove_data(self, bad_data):
        for data in bad_data:
            self.data.remove(data) # .remove(int)
            
        #self.data.remove(bad_data) # .remove([int])
        self.calc_stats()
    
    def calc_length(self):
        return len(self.data)
    
    def calc_mean(self):
        return sum(self.data) / len(self.data)
    
    def calc_median(self):
        return statistics.median(self.data)
    
    def calc_variance(self):
        return statistics.variance(self.data)
    
    def calc_stand_dev(self):
        return statistics.stdev(self.data)
    
    def calc_stats(self):
        self.length = self.calc_length()
        self.mean = self.calc_mean()
        self.median = self.calc_median()
        self.variance = self.calc_variance()
        self.stand_dev = self.calc_stand_dev()
        
