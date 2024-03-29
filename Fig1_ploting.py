#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:25:56 2021
@author: watsonlevens
"""
import pickle 
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting panel A 
# # FOF_L numerical results for n_q = infinity, q = 0.3
#########################################################################################################################
openfile = open('FOF_L_all_all_degq3.pkl', 'rb') 
all_all_degq3 = pickle.load(openfile)
#########################################################################################################################

# FOF_L theoretical results for n_q = infinity, q = 0.3
#########################################################################################################################
openfile = open('FOF_L_Theoretical_q3.pkl', 'rb') 
P3 = pickle.load(openfile)
#########################################################################################################################

# Data for ploting panel B
# FOF_L theoretical results n_q = infinity, q=0.8
#########################################################################################################################
openfile = open('FOF_L_Theoretical_q8.pkl', 'rb') 
P8 = pickle.load(openfile)
#########################################################################################################################

##########################################################################################################################
# FOF_L numerical results for n_q = infinity, q = 0.8
########################################################################################################################
openfile = open('FOF_L_all_all_degq8.pkl', 'rb') 
all_all_degq8 = pickle.load(openfile)
#########################################################################################################################


## Data for ploting panel C
openfile = open('NumericalDegree_and_Pk.pkl', 'rb') 
kn_and_Pkn = pickle.load(openfile) 

openfile = open('TheoreticalDegree_and_Pk.pkl', 'rb') 
kt_and_Pkt = pickle.load(openfile) 

###PROCCESSING NUMERICAL DEGREES FOR THE MODEL   
#Binning for q = 0.3
degrees_friendq3=np.ndarray.flatten(np.array(all_all_degq3))
xmin =min(all_all_degq3)
mybins_friendq3= np.unique(np.logspace(np.log10(xmin),np.log10(np.max(degrees_friendq3)+1), num=25, endpoint=True, base=10.0, dtype=int))
degrees_friendq3=np.ndarray.flatten(np.array(degrees_friendq3))  # To make a flat list(array) out of a list(array) of lists(arrays)

hist_friendq3 = np.histogram(degrees_friendq3, bins=mybins_friendq3) # Histogram of the data
pdf_friendq3 =hist_friendq3[0]/np.sum(hist_friendq3[0])#normalize histogram --for pdf


box_sizes=mybins_friendq3[1:]-mybins_friendq3[:-1]  # size of boxes
pdf_friendq3 = pdf_friendq3/box_sizes   # Divide pdf by its box size

#bins = Midpoints of distribution
mid_points_friendq3=np.power(10, np.log10(mybins_friendq3[:-1]) + (np.log10(mybins_friendq3[1:]-1)-np.log10(mybins_friendq3[:-1]))/2)

#Binning for q = 0.8
degrees_friendq8=np.ndarray.flatten(np.array(all_all_degq8))  
xmin =min(all_all_degq8)
mybins_friendq8= np.unique(np.logspace(np.log10(xmin),np.log10(np.max(degrees_friendq8)+1), num=25, endpoint=True, base=10.0, dtype=int))
degrees_friendq8=np.ndarray.flatten(np.array(degrees_friendq8))  

hist_friendq8 = np.histogram(degrees_friendq8, bins=mybins_friendq8) # Histogram of the data
pdf_friendq8 =hist_friendq8[0]/np.sum(hist_friendq8[0])


box_sizes=mybins_friendq8[1:]-mybins_friendq8[:-1]  # size of boxes
pdf_friendq8 = pdf_friendq8/box_sizes   # Divide pdf by its box size

#bins = Midpoints of distribution
mid_points_friendq8=np.power(10, np.log10(mybins_friendq8[:-1]) + (np.log10(mybins_friendq8[1:]-1)-np.log10(mybins_friendq8[:-1]))/2)

#Plot
fig,(ax1,ax2,ax3)=plt.subplots(nrows=1, ncols=3,figsize=(18, 6), sharex=False, sharey=False, squeeze= True)
# Set general font size
plt.rcParams['font.size'] = '20'
 
# FOF L theoretical plot
ax1.loglog(mid_points_friendq3,pdf_friendq3,color='blue',label = 'Numerical simulation', alpha=1,linestyle ='--',linewidth=2)
N = 1000 # Network size used to generate data
k = np.arange(N)
ax1.loglog(k,P3[N-1,],color='red',label = 'Theoretical calculations', alpha=1)

ax2.loglog(mid_points_friendq8,pdf_friendq8,color='blue',label = 'Numerical simulation', alpha=1, linestyle ='--',linewidth=2)
ax2.loglog(k,P8[N-1,],color='red',label = 'Theoretical calculations', alpha=1)

    
# fof model plot
ax3.loglog(kn_and_Pkn[0],kn_and_Pkn[1],color='blue',label = 'Numerical simulation', alpha=1,linestyle ='--',linewidth=2)
ax3.loglog(kt_and_Pkt[0], kt_and_Pkt[1],color='red',label = 'Theoretical simulation', alpha=1, linestyle ='-',linewidth=2)


for ax in fig.get_axes():
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
 	    label.set_fontsize(20)
    ax.set(xlabel='Degree $k$', ylabel='Frequency')
    ax.label_outer()  # Set axis scales outer


### Setting the limits of the plot
ax1.axes.set_xlim([1,100])
ax1.axes.set_ylim([max(min(pdf_friendq3),min(P3[N-1,])),  max(max(pdf_friendq3),max(P3[N-1,]))])

ax2.axes.set_xlim([8,1000])
ax2.axes.set_ylim([max(min(pdf_friendq8),min(P8[N-1,])),   max(max(pdf_friendq8),max(P8[N-1,]))])

ax3.axes.set_xlim([10,  max(kn_and_Pkn[0])]) 
ax3.axes.set_ylim([min(kn_and_Pkn[1]),max(kn_and_Pkn[1])]) 


## Panels labels
ax1.text(0.6, 0.2, 'A', fontsize=20,fontweight='bold')
ax2.text(5, 0.005, 'B', fontsize=20,fontweight='bold')
ax3.text(6, 0.05, 'C', fontsize=20,fontweight='bold')
#Splt.savefig('fof_l_loglog_plot2.pdf')







