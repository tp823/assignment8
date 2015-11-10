import numpy as np
import matplotlib.pyplot as plt
import sys
from invest_simulator import investment_simulator

#For # 1 of positions 
x = investment_simulator(1,10000)
x.investment_size(1000)
x.cumu_result()
x.stimulation()
x.histogram()
x.get_summary()

#For # 10 of positions 
x = investment_simulator(10,10000)
x.investment_size(1000)
x.cumu_result()
x.stimulation()
x.histogram()
x.get_summary()

#For # 100 of positions 
x = investment_simulator(100,10000)
x.investment_size(1000)
x.cumu_result()
x.stimulation()
x.histogram()
x.get_summary()

#For # 1000 of positions 
x = investment_simulator(1000,10000)
x.investment_size(1000)
x.cumu_result()
x.stimulation()
x.histogram()
x.get_summary()

        