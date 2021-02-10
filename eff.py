import filters
import numpy as np
from math import *
flt=[]
@filters.Filter(0,'Normal')
def normal(mus):
	return mus
flt+=[normal]
@filters.Filter(1,'Robot')
def robot(mus):
	new=[]
	for tone in mus.data:
		new+=[tone*(tone-sin(tone))/1000]
	new=np.array(new,'int16')
	mus.data=new
	return mus
flt+=[robot]
@filters.Filter(2,'Girl')
def girl(mus):
	new=[]
	for tone in mus.data:
		new+=[tone*(tone-sin(tone))/1000]
	del new[::4]
	new=np.array(new,'int16')
	mus.data=new
	return mus
flt+=[girl]
@filters.Filter(3,'Child')
def child(mus):
	new=[]
	for tone in mus.data:
		new+=[tone]
	del new[::4]
	new=np.array(new,'int16')
	mus.data=new
	return mus
flt+=[child]
@filters.Filter(4,'Old')
def old(mus):
	new=[]
	for tone in mus.data:
		new+=[tone*6]
		new+=[tone*6]
	del new[::3]
	new=np.array(new,'int16')
	mus.data=new
	return mus
flt+=[old]
@filters.Filter(5,'Baddie')
def baddie(mus):
	new=[]
	i=0
	for tone in mus.data:
		new+=[tone]
		new+=[mus.data[i-10]]
		i+=1
	mus.data=np.array(new,'int16')
	return mus
flt+=[baddie]
@filters.Filter(6,'Crunch')
def crunch(mus):
	new=[]
	for tone in mus.data:
		new+=[tone*6]
	mus.data=np.array(new,'int16')
	return mus
flt+=[crunch]
flt=filters.export(flt)