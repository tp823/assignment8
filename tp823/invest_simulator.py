'''
Created on Nov 5, 2015

@author: ds-ga-1007
'''
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class investment_simulator():
    "Stimulates different Investment Scenarios"
    def __init__(self, shares, trials):
        if shares in [1,10,100,1000]: 
            self.shares= shares
        else: 
                print 'Invalid number of position(s). Please enter 1,10,100,or 1000' 
        if type(trials) != int:
            print 'Please enter a integer'
        else: 
            self.trails=trials 
            
    def investment_size(self,value):
        self.value= value
        self.investment_size=self.value/self.shares
 
    def cumu_result(self):
        "Stimulates the total return on investment for one day"
        n=np.random.random(self.shares)
        payout=map(lambda n: 1 if n>.49 else -1, n) # 1= Success, -1=Failure 
        payout_array=sum(i for i in payout if i>0)
        success= 2* self.investment_size*payout_array
        return success 
    
 
    def stimulation(self):
        "Stimulates the return of investment for n trials(Days)"
        cumu_result = [self.cumu_result() for _ in range(self.trails)]
        daily_ret=map(lambda cumu_result: (cumu_result/1000)-1, cumu_result)
        daily_ret_array= np.array(daily_ret).reshape(self.trails,1)
        return daily_ret_array
  
    def histogram(self):
        "Histogram of Daily Returns"
        values= self.stimulation()
        plt.hist(values)
        plt.title("Daily Return On Investment")
        plt.xlabel("Return Value")
        plt.ylabel("Frequency")
       # plt.show()
       # plt.savefig("histogram.pdf")
        
    def get_summary(self):   
        "Returns Mean and Standard Deviation From Stimulation"
        values= self.stimulation()
        mean=np.mean(values)
        std= np.std(values)
        
        results = open('results.txt', 'w')
        print >>results, 'Mean:', '/n', mean
        print >>results, 'Std:', '/n', std
        results.close()
        
        
        
        
