# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:52:51 2019

@author: hari4
"""

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")
         
#importing random library
import random

#implementing Thompson samplinng algorithm
rounds = 10000
choices = 10
ads_posted = []
no_of_rewards = [0] * choices
no_of_punishments = [0] * choices
total_rewards = 0

for n in range(0, rounds):
    max_random_draw = 0
    ad = 0
    
    for i in range(0, choices):
        random_draw_beta = random.betavariate(no_of_rewards[i] + 1, no_of_punishments[i] + 1)
        if random_draw_beta > max_random_draw:
            max_random_draw = random_draw_beta
            ad = i
            
    ads_posted.append(ad)
    reward = dataset.values[n, ad]
    if reward:
        no_of_rewards[ad] = no_of_rewards[ad] + 1
    else:
        no_of_punishments[ad] = no_of_punishments[ad] + 1
    total_rewards = total_rewards + reward
    
#Visualization of Results
plt.hist(ads_posted)
plt.title("Histogram view of ads posted on internet")
plt.xlabel("Ads")
plt.ylabel("No. of times each ad was posted")