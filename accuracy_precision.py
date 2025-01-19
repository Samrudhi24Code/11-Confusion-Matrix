# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:09:21 2024

@author: Dell
"""

import numpy as np
#Let define a true value that we want to measure
#we first define the true value of 50.
#THis is the reference point.

true_value=50

#Simulate the measurements
#Accurate but not precise (close to true valuse but spread out)

'''
Simulating Measurements
We simulate two set of measurements:
    
    Accurate but not precise:
        These values are centered around the tree values(50),but there
        is some spread(random variation).
        This simulates measurement that are accurate(close to the true value) but not precise.
        (spread out)
        
'''
accurate_measurements=np.random.normal(loc=true_value,scale=5,size=10)

#Precise but not accurate(far from true value but tightly grouped)
'''
Precise but not accurate:
    These values are tightly clustered around 60,
    not near the true value of 50.
    THis simulates measurements that are precise(Closely grouped)
    but not accurate(far from the true values).
'''

precise_measurements=np.random.normal(loc=60,scale=1,size=10)

#Func to calculate accuracy

'''
WE calculte the mean(average) of the measurement
Then,we calculate how close this average is to the true value.
The closer the average is to the true value,the higher the accuracy.

formula for accuracy:=1-(difference/true_value)
0=low accuracy
1=high accuracy
'''

def calcalute_accuracy(measurements,true_value):
    average_measurement=np.mean(measurements)
    accuracy=1-abs(average_measurement-true_value)/true_value
    return accuracy

#func  to calcuate precision
'''
It is standard derivation of the measurements.sd how spread
out the measurement are.If small then closee else............
1/std_dev to represent precision                      
'''

def calcalute_precision(measurements):
    precision=1/np.std(measurements)
    return precision


#calculate accuracy and precision from both sets

'''
Accurate measurement:We calculate the acc and prec

that are close to true value but spread out.

Precise measurement::We calculate the acc and prec

that are closely grped but far from true value.

'''
accuracy_of_accurate=calcalute_accuracy(accurate_measurements, true_value)
precision_of_accurate=calcalute_precision(accurate_measurements)

accuracy_of_precise=calcalute_accuracy(precise_measurements, true_value)
precision_of_precise=calcalute_precision(precise_measurements)

print("Accurate but not Precise Measurement :")
print(f"Measurement: {accurate_measurements}")
print(f"Accuracy: {accuracy_of_accurate:.2f}")
print(f"Precision: {precision_of_accurate:.2f}")

print("\nPrecise but not Accurate Measurement:")
print(f"Measurements:{precise_measurements}")
print(f"Accuracy: {accuracy_of_precise:.2f}")
print(f"Precision: {precision_of_precise:.2f}")

















