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
##rename so u can move in, dont delete

os.getcwd() #find current WD 


#for loop to move files/rename (same thing)
testingrooms = ['A','B','C']   #index testing room names
for r in testingrooms:
    print('/Users/joelleg/Desktop/ps2-girgisjo-V2/testingroom' + r ) #ensure you've pointed to each folder
    orig_location = '/Users/joelleg/Desktop/ps2-girgisjo-V2/testingroom' + r + '/experiment_data.csv' #assign source path/directory for each folder
    print(orig_location) #again, just double check code
    shutil.copyfile(orig_location, '/Users/joelleg/Desktop/ps2-girgisjo-V2/rawdata/' +  'testroom' + r + '.csv') #copy/rename file using function(old location, new location)


#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT
#
os.chdir('/Users/joelleg/Desktop/ps2-girgisjo-V2/rawdata')  #change directory


data = np.empty((0,5))   #create empty np array
print(data)
 

#for loop ---first print up to print(tmp), then run whole for loop
for r in testingrooms:
    print('/Users/joelleg/Desktop/ps2-girgisjo-V2/rawdata/testroom' + r ) #test code
    tmp = sp.loadtxt('/Users/joelleg/Desktop/ps2-girgisjo-V2/rawdata/testroom' + r + '.csv',delimiter=',')  #read in files in rawdata folder
    print(tmp)   #temp value
    data = np.vstack([data,tmp])  #stack/combine data from the 3 testrooms
    print(data)



#Assign variables for each column
sbj=data[:,0]     # select 1st column
print(sbj)
print(sbj.dtype)
sbj = sbj.astype('int32')   #convert to string

stim=data[:,1]  #select 2nd column
print(stim)
stim = stim.astype('int32')   #convert to string

pair=data[:,2]   #select 2nd column
print(pair)
pair = pair.astype('int32')  #convert to string

acc=data[:,3]# select 4th column
print(acc)

mrt=data[:,4]# select 5th column
print(mrt)

#%%
# calculate overall average accuracy and average median RT

acc_avg =np.mean(acc)   # 91.48%
print(acc_avg)

mrt_avg =np.mean(mrt)   # 477.3ms
print(mrt_avg)

#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)


newtableWords=np.empty([0,5])
newtableFaces=np.empty([0,5])

for s in stim: 
    tempValue=stim[s,:] #take that row and create a new variable to house  #ERROR: too many indices
    if tempValue[1] == 1: #if a value in stimulus is 1... 
        print(tempValue) # stim[s] has not enough information here depending on how your script is indented. 


for s in stim:
    if stim[s,3]==1:   #if a value in stimulus is 1...
        tempValue=stim[s,3]  #take that row and create a new variable to house these values
        newtableWords=np.vstack([newtableWords,tempValue])   ####stack rows from 'words' condition, within the emtpy numpy array
    elif stim[s] == 2:
        tempValue=stim[s,3]  #take that row and create a new variable to house these values
        newtableFaces=np.vstack([tempValue, newtableFaces])   ##stack rows from 'faces' condition, within the emtpy numpy array
        print(stim[s])


AccWords=np.vstack([tempValue,newtableWords]) #create variable that merges stimulus tables with corresponding acc tables
AccFaces=np.vstack([tempValue,newtableFaces])


#Now to get the average:
#np.mean(acc)
AccWords_avg=np.mean(newtableCondition1)
AccFaces_avg=np.mean(newtableCondition1)

## etc. this needs to be in its own table too: np.mean(mrt)
mrtWords=np.vstack([tempValue,newtableWords_mrt])
mrtFaces=np.vstack([tempValue,newtableFaces_mrt])

# words: 88.6%, 489.4ms   faces: 94.4%, 465.3ms


#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
#
#create variable for each condition
acc_wp =
np.mean(acc, pair == 1)
np.mean(acc_wp)
print(np.mean(acc_wp))    # 94.0%

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

scipy.stats.ttest_rel(mrtWords_avg,mrtFaces_avg)

# words: t=-5.36, p=2.19e-5
# faces: t=-2.84, p=0.0096


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
...