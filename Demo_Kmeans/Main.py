# -*- coding: utf-8 -*-
'''
Created on Mar 17, 2016

@author: JuniorK
'''
import matplotlib.pyplot as plt
import random
import math
import csv
random.seed()                   
colors=["yellow","blue","gray","red","black","green","pink"]
training_set=[]
centroid=[]
num=100
k=4
def distance(p1,p2):
    return math.sqrt((p1[1]-p2[1])**2+(p1[0]-p2[0])**2)
def kmeans(training_set,centroid):
    clustering_index=[0*x for x in range(num)]
    dim= len(training_set)
    check=True
    while check==True:  
        check=False 
        for i in range(dim):
            min_dis=9999999
            pos=0
            for j in range(k):
                dis=distance(training_set[i], centroid[j])
                if dis<min_dis:
                    min_dis=dis
                    pos=j
            clustering_index[i]=pos
        for i in range(k):
            sumx=0
            sumy=0
            cnt=0
            for j in range(dim):
                if clustering_index[j]==i: 
                    sumx+=training_set[j][0]
                    sumy+=training_set[j][1]
                    cnt+=1
            if centroid[i]!=(sumx/cnt,sumy/cnt): check=True
            centroid[i]=(sumx/cnt,sumy/cnt)            
    return clustering_index


def plot_2d(training_set, clustering_index):

    for i in range(len(training_set)):
        plt.scatter(training_set[i][0], training_set[i][1], color=colors[clustering_index[i]])
    plt.show()
if __name__ == "__main__":
    #for i in range(num):
        #training_set.append((random.randint(0,100),random.randint(0,100)))
        #file.write(str(training_set[len(training_set)-1][0])+","+str(training_set[len(training_set)-1][1])+"\n")
    x= csv.reader("DATA.csv")
    with open('DATA.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            training_set.append((int(row[0]),int(row[1])))
    
    Set=list(set(training_set))
    if len(Set)<k: raise "Số cụm nhiều hơn số tập dữ liệu"
    for i in range(k):
        centroid.append(Set[i])   
    clustering_index=kmeans(training_set,centroid)
    plot_2d(training_set, clustering_index)