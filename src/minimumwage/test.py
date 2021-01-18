from datetime import datetime
from scipy.stats import norm, zscore

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import csv 

# reward = 0.65
# min wage = 15.00

def apply_calc(diffs, rate):
    bonus = diffs.apply(lambda x: max(0,rate * x / 60 - 0.65))
    return bonus

def print_stats(bonus):
    print (bonus.min() / 60, bonus.max(), bonus.mean(), bonus.std(), bonus.median(), bonus.quantile([.25, .75]))


def apply_calc_list(l, rate):
    output = []
    for x in l:
        def calc(x): return max(0, rate * x / 60 - 0.65)
        output.append(calc(x))
    return output

def print_stats_list(l):
    print (np.min(l), np.max(l), np.mean(l), np.std(l), np.median(l), np.quantile(l, [.25, .75]))



if __name__=="__main__":
    df = pd.read_csv('../../data/testing.csv')
    df = df.sort_values(by=['WorkerId']).set_index(keys=['WorkerId']).groupby(by=['WorkerId'])  # sort values by WorkerId to performgroupby
    groups = df.groups
    avg_time_per_task = []
    weighted_avg_time_per_task = []
    #cnt = 0
    for group in groups:
        group_df = df.get_group(group)
        group_df.sort_values(by=['AcceptTime'], ignore_index=True, inplace=True)
        group_accepts = group_df['AcceptTime']
        group_submits = group_df['SubmitTime']
        group_accepts = group_accepts.apply(lambda x: datetime.strptime(x[0:x.rfind("-")], "%Y-%m-%d %H:%M:%S").timestamp() / 60)
        group_submits = group_submits.apply(lambda x: datetime.strptime(x[0:x.rfind("-")], "%Y-%m-%d %H:%M:%S").timestamp() / 60)
        totaltime_overlapping = 0
        totaltime = 0
        task_times = []
        for index, asmt in group_accepts.items():
            if (index != 0 and asmt < group_submits[index-1]):
                totaltime += group_submits[index] - group_submits[index - 1]
                task_times.append(group_submits[index] - group_submits[index - 1])
                totaltime_overlapping += group_submits[index] - asmt 
            else:
                totaltime += group_submits[index] - asmt
                task_times.append(group_submits[index] - asmt)
                totaltime_overlapping += group_submits[index] - asmt 
        #print (totaltime, totaltime_overlapping, len(group_submits))
        avg_time_per_task.append(totaltime / len(group_submits))
        med = np.median(task_times)
        total_by_med = med * len(group_submits)
        '''
        if (cnt == 6):
            rg = range(1,10)
            plt.plot(rg, task_times)
            plt.ylabel("Completion time (mins.)")
            plt.xlabel("Assignment #")
            plt.title("Completion time trend")
            plt.show()
        cnt+=1
        '''
        bonus = [max(0, i * total_by_med/ 60 - .65 * len(group_submits)) for i in [5.84, 7.65, 15]]
        print (bonus, len(group_submits))



        #avg_time_per_task.extend([totaltime / len(group_submits)]*len(group_submits))
        #print (len(group_submits) * .65, totaltime * 15 / 60 - len(group_submits) * .65)
    #print (np.mean(avg_time_per_task), np.median(avg_time_per_task), np.std(avg_time_per_task), np.max(avg_time_per_task), np.min(avg_time_per_task), np.quantile(avg_time_per_task, [.25, .75]))
    #print (60 / np.mean(avg_time_per_task) * .65, 60 / np.median(avg_time_per_task) * .65)
    #bonus = apply_calc_list(np.array(avg_time_per_task), 5.84)
    #print ("for 5.84:")
    #print_stats_list(bonus)
    #bonus = apply_calc_list(np.array(avg_time_per_task), 7.65)
    #print ("for 7.65:")
    #print_stats_list(bonus)
    #bonus = apply_calc_list(np.array(avg_time_per_task), 15)
    #print ("for 15:")
    #print_stats_list(bonus)

        #print (group_df[['AcceptTime', 'SubmitTime']])




    '''
    accepts = df['AcceptTime']
    submits = df['SubmitTime']
    accepts = accepts.apply(lambda x: datetime.strptime(x[0:x.rfind("-")], "%Y-%m-%d %H:%M:%S").timestamp() / 60)
    submits = submits.apply(lambda x: datetime.strptime(x[0:x.rfind("-")], "%Y-%m-%d %H:%M:%S").timestamp() / 60)
    diffs = submits - accepts  # difference in submit - accept time
    print (diffs.min(), diffs.max(), diffs.mean(), diffs.std(), diffs.median(), diffs.quantile([.25, .75]))

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
    '''
    
    
    
    
    
    '''
    stats = [diffs.mean(), diffs.std()]
    diffs.plot(kind='kde', legend=True)
    range = np.arange(-2000, 5000, 1)
    plt.plot(range, norm.pdf(range, 846, 1000))
    plt.show()
    print (diffs.max(), diffs.min(), diffs.mean(), diffs.std())
    '''