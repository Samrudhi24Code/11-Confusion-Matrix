# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:51:49 2024

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt

#Target value(true value)
true_value=50

#Simulate the data(true value)

#1.Accurate and Precise(close to true value and tightly grouped)

'''
loc=true_value(true value=50);The vakue will be centered the true value
(50).
scale=1:The stndard deviaton (spread ) is small,
meaning the values will be tightly grouped arounf the true value.

This implies high precision.
The measurement will vary only a little from true value,
so they'll be both accurate (close to 50) & precise (close to each other)'
'''


accurate_precise=np.random.normal(loc=true_value,scale=1,size=10)

#2.Accurate but not precise (closeto true value but spread out.)
accurate_not_preice=np.random.normal(loc=true_value,scale=10,size=10)

'''
The two line of code you've highlighted may look similar,but they
differ in one important aspect:the value of scale,which controls
the spread of the generated values around the true vale(loc)'''

#3.Precise but not Accurate(far from true value but tightly grouped)
precise_not_accurate=np.random.normal(loc=70,scale=1,size=10)

#4.Neither Accurate nor Precise (far true value and spread out)
not_accurate_not_precise=np.random.normal(loc=70,scale=10,size=10)

#Plotting the result
plt.figure(figsize=(10,6))

#Plot1 Accurate and precise
plt.scatter(accurate_precise,[1]*10,color='green',label='Accurate and precise')

#plot 2 Accurate but not precise
plt.scatter(accurate_not_preice,[2]*10,color='blue',label='Accurate but not Precise')

#Plot 3:Precise but not Accurate
plt.scatter(precise_not_accurate,[3]*10,color='orange',label='Precise but not Accurate')

#Plot 4: Neither Accurate and nor precise
plt.scatter(not_accurate_not_precise,[4]*10,color='red',label='Neither Accurate nor Precise')

#Adding target line
plt.axvline(true_value,color='black',linestyle='--',label='True value')

#label and legend

plt.yticks([1,2,3,4],['Accurate and precise','Accurate but not precise','Precise  but not Accurate','Neither Accurate nor Precise'])

plt.xlabel('Measurement value')
plt.legend()
plt.title('Accuracy and Precision Demontration')
plt.show()


#thIS IS ACCURATE(gREEN)

#ITS STAND ARD DEVAITION IS LOW(rED)

#accurate but not precise =blue mean value of this dot is 50 but st std deviation os low

#(orange) mean value greater than 60 but std de low Precise but not Accurate

#neither 