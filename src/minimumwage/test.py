from datetime import datetime
from scipy.stats import norm, zscore

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import csv 

# reward = 0.65
# min wage = 15.00

def apply_calc(diffs, rate):
    bonus = diffs.apply(lambda x: max(0,rate * (x / 60) - 0.65))
    return bonus

def print_stats(bonus):
    print (bonus.min() / 60, bonus.max() / 60, bonus.mean() / 60, bonus.std() / 60, bonus.median() / 60, bonus.quantile([.25, .75]))

if __name__=="__main__":
    df = pd.read_csv('../../data/testing.csv')
    accepts = df['AcceptTime']
    submits = df['SubmitTime']
    accepts = accepts.apply(lambda x: datetime.strptime(x[0:x.rfind("-")], "%Y-%m-%d %H:%M:%S").timestamp())
    submits = submits.apply(lambda x: datetime.strptime(x[0:x.rfind("-")], "%Y-%m-%d %H:%M:%S").timestamp())
    diffs = submits - accepts  # difference in submit - accept time
    bonus = apply_calc(diffs, 15)
    print("for 15:")
    print_stats(bonus)
    bonus = apply_calc(diffs, 7.70)
    print ("for 7.7:")
    print_stats(bonus)
    bonus = apply_calc(diffs, 2.76)
    print ("for 2.76")
    print_stats(bonus)


    '''
    #pay = diffs.apply(lambda x: x * 15 / 3600 - .65)  # this gives some really high number like a bonus of $13
    print (3600 / diffs.median() * .65)
    #pay = diffs.apply(lambda x: 15 / (diffs.mean() + (x - diffs.mean()) / diffs.std()))  # this gives all really low numbers.
    #print (pay)
    #print (15 * diffs.mean() / 3600 * .65)
    x = diffs[diffs.between(0, diffs.quantile(.15))]
    z_scores = zscore(diffs)
    abs_z_scores = np.abs(z_scores)
    cnt = 0
    print (sum(1 for abs_z_score in abs_z_scores if abs_z_score < 3))
    print (len(diffs))
    print (len(x))
    print (len(diffs) - len(x))
    print (60 / (diffs.mean() / 60) * .65, 60 / (diffs.median() / 60) * .65)
    print (diffs.min() / 60, diffs.max() / 60, diffs.mean() / 60, diffs.std() / 60, diffs.median() / 60, diffs.quantile([.25, .75]))
    '''
    
    
    
    
    
    '''
    stats = [diffs.mean(), diffs.std()]
    diffs.plot(kind='kde', legend=True)
    range = np.arange(-2000, 5000, 1)
    plt.plot(range, norm.pdf(range, 846, 1000))
    plt.show()
    print (diffs.max(), diffs.min(), diffs.mean(), diffs.std())
    '''