#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:25:51 2019

@author: ericson
"""

import numpy as np
import matplotlib.pyplot as plt

# Señal del problema
N  = 100
M  = 4
fs = 1000

w0         = 3
phi0       = np.pi/4
amp_noise  = 0.02 

ts = 1/fs # tiempo de muestreo

tt     = np.linspace(0, (N-1)*ts, N).flatten()
signal = np.sin(2*w0*np.pi*tt + phi0)

# Creacion de ruido
noise  =  np.random.normal(0,amp_noise,np.size(signal))
signal_noise  = signal + noise


## Se aplica weiner filter

# Crear matriz hermetica [M,N-M+1]
rows    = M
columns = np.size(signal_noise) - M + 1
hmatrix = np.zeros((rows, columns))
                   
for i in np.arange(columns):
    hmatrix[ : , i ]  =   signal_noise[np.arange(M + (i - 1) , (i-1) , -1 )]

