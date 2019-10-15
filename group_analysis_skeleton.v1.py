#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename

os.getcwd() #find current WD 

#for loop to move files/rename (same thing)
testingrooms = ['A','B','C']   #index testing room names
for r in testingrooms:
    print('/Users/joelleg/Desktop/ps2-girgisjo/testingroom' + r ) #ensure you've pointed to each folder
    orig_location = '/Users/joelleg/Desktop/ps2-girgisjo/testingroom' + r + '/experiment_data.csv' #assign source path/directory for each folder
    print(orig_location) #again, just double check code
    shutil.copyfile(orig_location, '/Users/joelleg/Desktop/ps2-girgisjo/rawdata/' +  'testroom' + r + '.csv') #copy/rename file using function(old location, new location)


#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT

s.chdir('/Users/joelleg/Desktop/ps2-girgisjo/rawdata')  #change directory


data = np.empty((0,5))   #create empty np array
print(data)
 

#for loop
for r in testingrooms:
    print('/Users/joelleg/Desktop/ps2-girgisjo/rawdata/testroom' + r ) #test code
    tmp = sp.loadtxt('/Users/joelleg/Desktop/ps2-girgisjo/rawdata/testroom' + r + '.csv',delimiter=',')  #read in files in rawdata folder
    data = np.vstack([data,tmp])  #stack/combine data from the 3 testrooms
    print(tmp)
    print(data)


#Can I change variable types? Once I have columns, i think so



#%%
# calculate overall average accuracy and average median RT
#
acc_avg = ...   # 91.48%
mrt_avg = ...   # 477.3ms


#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
#
...

# words: 88.6%, 489.4ms   faces: 94.4%, 465.3ms


#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
#
acc_wp = ...  # 94.0%
acc_bp = ...  # 88.9%
mrt_wp = ...  # 469.6ms
mrt_bp = ...  # 485.1ms


#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)
#
...

# words - white/pleasant: 478.4ms
# words - black/pleasant: 500.3ms
# faces - white/pleasant: 460.8ms
# faces - black/pleasant: 469.9ms


#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats
...

# words: t=-5.36, p=2.19e-5
# faces: t=-2.84, p=0.0096


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
...