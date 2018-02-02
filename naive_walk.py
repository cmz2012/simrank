#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-29 下午2:35
# @Author  : chen
# @Site    : 
# @File    : naive_walk.py
# @Software: PyCharm Community Edition
from __future__ import division
import numpy as np
import snap
import datetime

def path_sample(g,source,L):
    path=list()
    path.append(source)
    walker=source
    for i in range(L):
        Ni=g.GetNI(walker)
        InDegree=Ni.GetInDeg()
        InNeibors=list(Ni.GetInEdges())
        if InDegree==0:
            break
        walker=np.random.choice(InNeibors)
        path.append(walker)
    return path

def naive_walk(g,c,L,R):
    N=g.GetNodes()
    s=np.zeros((N,N))
    for r in range(R):
        print("round ",r)
        all_path=list()  ## sample a path of length L form every node in the graph g
        for n in range(N):
            all_path.append(path_sample(g,n,L))
        for i in range(N):
            for j in range(i,N):
                pathi=all_path[i]
                pathj=all_path[j]
                sd=0.
                for k in range(min(len(pathi),len(pathj))):
                    if pathi[k]==pathj[k]:
                        sd=c**k
                        break
                s[i,j]+=sd
                s[j,i]+=sd
    s/=R
    return s

def main():
    start = datetime.datetime.now()
    g = snap.LoadEdgeList(snap.PNGraph, './email-Eu-core.txt')
    N = g.GetNodes()
    c = 0.6
    L = 6
    R = 1000
    s = naive_walk(g,c,L,R)
    np.save('./simByNaive.npy',s)
    end=datetime.datetime.now()
    print("the process time is",(end-start).seconds,"seconds")

if __name__ == '__main__':
    main()