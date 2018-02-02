#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-2-2 下午2:42
# @Author  : chen
# @Site    : 
# @File    : evaluate.py
# @Software: PyCharm Community Edition

import numpy as np
import matplotlib.pyplot as plt

'''this script evaluate the result of naive walk and my own walk solution by computing
the mean error and top-k precision and plot the figure of the result.'''

def plot_ME(truth,naive,my):
    '''truth is the simrank truth value matrix which is computed by iteration solution,
    naive and my both are a P*N*N matrix, where P is plot point number'''
    k,N,_=naive.shape
