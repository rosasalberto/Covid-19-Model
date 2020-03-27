# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 03:43:46 2020

@author: arosasga
"""
from spain_data import S,I,R,D,Oi,tr

class SIR_model_adapted:
    
    
    def __init__(self, a, b, mintr, maxtr, rr, mindr, maxdr, icol, inf_test):
        
        """
        New covid19 model.

        Based on the SIR model, but with additions of:
            -Delays
            -Deaths
            -Variable transmission rate, dependent from government action U
            
        State Variables:
            S = Subsceptible
            I = Infective
            R = Removed
            D = Death
            Pd = Probability of death
            Tr = Transmision rate
        
        constant parameters:
            a = number of days for the infected to show sintoms
            b = number of days for the infected to begin infecting
            maxtr = maximum tr, normally before quarantine
            mintr = minimum tr, normally when severe quarantine
            rr = recovery rate, 1/meandaystorecover
            maxdr = maximum death rate, normally when sanitary system are collapsed
            mindr = minimum death rate, normally when the sanitary system is not collapsed.
            Icol = Infected rate to collapse the sanitary system.
            inf_test = rate of tested from infected.
        """
        
        self.a = a
        self.b = b
        self.mintr = mintr
        self.maxtr = maxtr
        self.rr = rr
        self.mindr = mindr
        self.maxdr = maxdr
        self.icol = icol
        self.inf_test = inf_test
        
        self.S = S
        self.I = I
        self.R = R
        self.D = D
        self.Oi = Oi
        self.tr = tr
        
    def run(self, system_control):
        
        """
        system_control = government actions in the coming n days, list with values between 0 and 1.
        """
        S = self.S.copy()
        I = self.I.copy()
        R = self.R.copy()
        D = self.D.copy()
        Oi = self.Oi.copy()
        Tr = [] 
        
        for day in range(len(system_control)):
            
            pd = self.mindr if I[-1] < self.icol else self.maxdr
            
            tr = self.maxtr + (self.mintr-self.maxtr) * system_control[day] 
            s = S[-1] - tr * I[-self.b] * S[-1]
            i = I[-1] + tr * I[-self.b] * S[-1] - self.rr * I[-1]
            r = R[-1] + self.rr * I[-1]
            d = D[-1] + pd * (r - R[-1])
            
            oi = float(I[-self.a]) * self.inf_test
            
            S.append(s)
            I.append(i)
            R.append(r)
            D.append(d)
            Oi.append(oi)
            Tr.append(tr)
            
        y = [S,I,R,D,Oi,Tr]
        
        return y