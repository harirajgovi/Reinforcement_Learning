# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:27:24 2019

@author: hari4
"""

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

#importing math library
import math

#UCB Algorithm implementation
rounds = 10000
choices = 10
no_of_times_ads_posted = [0] * choices
summ_of_rewards = [0] * choices
ads_posted = []
total_rewards = 0

for n in range(0, rounds):
    max_upper_confidence_bound = 0
    ad = 0
    
    initial = [num for num in range(0, choices)]
    if n in initial:
        ad = n    
    else:
        for i in range(0, choices):
            avg_i = summ_of_rewards[i] / no_of_times_ads_posted[i]
            delta_i = math.sqrt((3 / 2) * (math.log(n + 1) / no_of_times_ads_posted[i]))
            upper_confidence_bound = avg_i + delta_i
            if upper_confidence_bound > max_upper_confidence_bound:
                max_upper_confidence_bound = upper_confidence_bound
                ad = i
    
    ads_posted.append(ad)
    no_of_times_ads_posted[ad] = no_of_times_ads_posted[ad] + 1
    reward = dataset.values[n, ad]
    summ_of_rewards[ad] = summ_of_rewards[ad] + reward
    total_rewards = total_rewards + reward
                
#Visualizing results
plt.hist(ads_posted)
plt.title("Histogram of ads posted on internet")
plt.xlabel("Ads")
plt.ylabel("No. of times each ad was posted")   
plt.show()         

