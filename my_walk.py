#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-24 下午8:39
# @Author  : chen
# @Site    : 
# @File    : my_walk.py
# @Software: PyCharm Community Edition
from __future__ import division
import numpy as np
import snap
import datetime

def subroute(g,begin,l,visited):
    factor=1.
    walker=begin
    for j in range(l):
        Ni = g.GetNI(walker)
        OutNeibors = list(Ni.GetOutEdges())
        OutDeg = Ni.GetOutDeg()
        if OutDeg==0:
            break
        walker=np.random.choice(OutNeibors)
        if walker not in visited:
            InDeg=g.GetNI(walker).GetInDeg()
            factor*=OutDeg/InDeg
        else:
            break
    else:
        return factor,walker
    return 0,walker

def ssRWalk(u,c,L,R,g):
    N=g.GetNodes()
    ss=np.zeros(N)
    ss[u]=R
    for r in range(R):
        walker=u
        visited=set()
        visited.add(walker)
        for j in range(1,L+1):
            Ni=g.GetNI(walker)
            InNeibors=list(Ni.GetInEdges())
            InDeg=Ni.GetInDeg()
            if InDeg==0:
                break
            walker=np.random.choice(InNeibors)
            if walker in visited:
                break
            visited.add(walker)
            factor,end=subroute(g,walker,j,visited)
            ss[end]+=factor*(c**j)
    ss/=R
    return ss

def my_walk(g,c,L,R):
    N=g.GetNodes()
    s=np.zeros((N,N))
    for i in range(N):
        s[i]=ssRWalk(i,c,L,R,g)
    return s

def main():
    start=datetime.datetime.now()
    g = snap.LoadEdgeList(snap.PNGraph, './email-Eu-core.txt')
    N=g.GetNodes()
    c=0.6
    L=6
    R=1000
    s=my_walk(g,c,L,R)
    np.save('./simByMW.npy',s)
    end=datetime.datetime.now()
    print("the process time is ",(end-start).seconds,"seconds")

if __name__=="__main__":
    main()