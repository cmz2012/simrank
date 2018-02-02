#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-24 下午2:53
# @Author  : chen
# @Site    : 
# @File    : iteration.py
# @Software: PyCharm Community Edition
from __future__ import division
import numpy as np
import snap
import matplotlib.pyplot as plt
import datetime

def sim_truth(g,c,T):
    '''this function compute the simrank of g by iteration, where c is a decay factor and T
    is the number of round. return the simrank matrix and use MSE to record the matrix variation'''
    N=g.GetNodes()
    # M=g.GetEdges()
    s=np.eye(N,N)
    for t in range(T):
        temp=np.eye(N,N)
        for i in range(N):
            Ni=g.GetNI(i)
            DegOfI=Ni.GetInDeg()  #is a integer
            for j in range(i+1,N):
                Nj=g.GetNI(j)
                DegOfJ=Nj.GetInDeg()
                InEdgeOfJ=Nj.GetInEdges()
                InEdgeOfI = Ni.GetInEdges()  # is a generateor
                # for each node of neibors of i and j, add their simrank value up
                # InEdgeOfI and InEdgeOfJ are int generator
                val=0.
                if DegOfI and DegOfJ:
                    for u in InEdgeOfI:
                        for v in InEdgeOfJ:
                            val+=s[u][v]
                    val*=(c/DegOfI/DegOfJ)
                temp[i][j]=val
                temp[j][i]=val
        s=temp
    return s

def main():
    start=datetime.datetime.now()
    g=snap.LoadEdgeList(snap.PNGraph,'./email-Eu-core.txt')
    c=0.6
    T=10
    s=sim_truth(g,c,T)
    np.save('simrank.npy',s)
    end=datetime.datetime.now()
    print 'total time: '+str((end-start).seconds)+' seconds'

if __name__=="__main__":
    main()