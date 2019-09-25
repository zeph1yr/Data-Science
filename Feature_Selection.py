import csv
import numpy as np
import pywt
from collections import Counter
import scipy.stats
import matplotlib.pyplot as plt 
from scipy.fftpack import fft



nLabel = 4
nTrial = 40
nUser =32
nChannel = 32
nTime = 8064


channels = ['Fp1','AF3','F3','F7','FC5',
        'FC1','C3','T7','CP5','CP1',
        'P3','P7','PO3','O1','Oz',
        'Pz','Fp2','AF4','Fz','F4',
        'F8','FC6','FC2','Cz','C4',
        'T8','CP6','CP2','P4','P8',
        'PO4','O2']

selcted_ch=["Fp1", "T8", "P8", "F8"]



'''
def calculate_entropy(list_values):
    counter_values = Counter(list_values).most_common()
    probabilities = [elem[1]/len(list_values) for elem in counter_values]
    entropy=scipy.stats.entropy(probabilities)
    return entropy'''


 
def calculate_statistics(list_values):
    maxi = np.max(list_values)
    mini = np.min(list_values)
    median = np.nanpercentile(list_values, 50)
    mean = np.mean(list_values)
    std = np.std(list_values)
    var = np.nanvar(list_values)
    rms = np.nanmean(np.sqrt(list_values**2))
    return [maxi, mini, median, mean, std, var, rms]
 
def calculate_crossings(list_values):
    zero_crossing_indices = np.nonzero(np.diff(np.array(list_values)> 0))[0]
    no_zero_crossings = len(zero_crossing_indices)
    mean_crossing_indices = np.nonzero(np.diff(np.array(list_values)> np.nanmean(list_values)))[0]
    no_mean_crossings = len(mean_crossing_indices)
    return [no_zero_crossings, no_mean_crossings]
 
def get_features(list_values):
    #entropy = calculate_entropy(list_values)
    crossings = calculate_crossings(list_values)
    statistics = calculate_statistics(list_values)
    return statistics + crossings



for user in range(nUser):
    for tr in range(nTrial):
        list4=[]
        if user < 9:
            name = '0' + str(user + 1)
        else:
            name = user + 1
        
        data =[]

        fname = "data/s"+str(name)+"t"+str(tr + 1)+".txt"
        f = open(fname, 'r')
        lines = f.readlines()
        
        for line in lines:
            temp_list = line.strip().split(',')
            data.append(temp_list[1:-1])
        
        features = []
        
        
        for i in range(len(channels)):
            if i in selcted_ch:
                x = data[i]
                coeffs = pywt.wavedec(x, 'db4', level=6)
                cA6, cD6, cD5, cD4, cD3, cD2, cD1 = coeffs
                features = features + get_features(cD1)
                features = features + get_features(cD2)
                features = features + get_features(cD3)
                features = features + get_features(cD4)
                features = features + get_features(cD5)
        
        print(fname)
                    

        with open('features_1.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(features)
        csvFile.close()
        
        
        
        
            
        '''features = []
        
        
        for i in range(len(channels)):
            x = data[i]
            coeffs = pywt.wavedec(x, 'db4', level=6)
            cA6, cD6, cD5, cD4, cD3, cD2, cD1 = coeffs
            features = features + get_features(cD1)
            features = features + get_features(cD2)
            features = features + get_features(cD3)
            features = features + get_features(cD4)
            features = features + get_features(cD5)
        
        print(fname)

        with open('features.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(features)
        csvFile.close()'''
