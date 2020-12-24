# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 20:01:51 2020

@author: daf
"""
# https://github.com/nathan-git123
# This is a normal distribution-based VaR model. It assumes the user is aware
# of trading conventions (e.g. 252-day vs 365-day convention).

import scipy.stats as stats
import math

port_size = float(input("Enter the portfolio size: "))
port_sd = float(input("Enter the portfolio percent daily standard deviation: "))
p_value = float(input('Enter the percent VaR: '))
t = float(input('Enter the VaR time in days: '))
z_score = stats.norm.ppf(p_value/100)
var = port_size * z_score * port_sd/100 * math.sqrt(t)

print("For a", port_size, "dollar portfolio,", 
      port_sd, "percent annual portfolio standard deviation,", 
      p_value, "percent VaR, and",
      t, "day analysis period, your VaR is", abs(round(var, 2)))
