# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 18:08:32 2021

@author: sssalas
"""

def reweight(pi,q1,r1):
    """the correction factor"""
    r0 = 1-r1
    q0 = 1-q1
    tot = pi*(q1/r1)+(1-pi)*(q0/r0)
    w = pi*(q1/r1)
    w /= tot
    return w