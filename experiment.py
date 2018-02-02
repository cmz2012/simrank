#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-2-1 下午4:13
# @Author  : chen
# @Site    : 
# @File    : experiment.py
# @Software: PyCharm Community Edition
from __future__ import division
import my_walk as mw
import naive_walk as nw
import numpy as np
import datetime
import snap

'''this module define two functions,which compute the simrank matrix of the graph as
the sampled path length L changes and sampled paths number R changes.'''

def var_L(g,c,L_list,R):
    N=g.GetNodes()
    d=len(L_list)
    naive_ret=np.zeros((d,N,N))
    my_ret=np.zeros((d,N,N))
    for i,L in enumerate(L_list):
        sn=nw.naive_walk(g,c,L,R)
        sm=mw.my_walk(g,c,L,R)
        naive_ret[i,:,:]=sn
        my_ret[i,:,:]=sm
    return naive_ret,my_ret

def var_R(g,c,L,R_list):
    N=g.GetNodes()
    d=len(R_list)
    naive_ret=np.zeros((d,N,N))
    my_ret=np.zeros((d,N,N))
    for i,R in enumerate(R_list):
        sn=nw.naive_walk(g,c,L,R)
        sm=mw.my_walk(g,c,L,R)
        naive_ret[i,:,:]=sn
        my_ret[i,:,:]=sm
    return naive_ret,my_ret

def main():
    start = datetime.datetime.now()
    g = snap.LoadEdgeList(snap.PNGraph, './email-Eu-core.txt')
    c = 0.6
    L_list=range(1,7)
    R_list=range(200,1200,200)
    print 'computing with L variating...'
    a,b=var_L(g,c,L_list,1000)
    print 'computing with R variating...'
    c,d=var_R(g,c,6,R_list)

    ## save the results to the disk. 'n' represents naive_walk result matrix and
    # 'm' represents my_walk result matrix
    np.savez('./var_L.npz',n=a,m=b)
    np.savez('./var_R.npz',n=c,m=d)

    end=datetime.datetime.now()
    print 'total time: '+str((end-start).seconds)+' seconds'

if __name__ == '__main__':
    main()

