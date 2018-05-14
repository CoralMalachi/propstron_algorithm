#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import numpy as np
import argparse
import sys


# the path will be passed as an argument
our_path = sys.argv[1]
#save the training ser X into a matrix as required
X = np.loadtxt(our_path)
#get the number of varibles
d = len(X[0])
numOfTrainingExamples = len(X)
#save the last col of the traing set as vector Y - the right predict result
Y = X[:,- 1]
#print(Y) for myself

#i'll create two arrays for the regular literal and the negative literal and let's
#set them all to value 1
#remember that the all negative hypothesis looks like this: X1 ^ not(x1) ^ x2 ^ not(x2) .....
#and this is the initial hypothesis, so in the first iteration of the algorithem , the prediction
# y will always be wrong, because the hypothsis has 2 versions of every literal.
#so in the first iteration the algorithem remove a single version of every xi/not(xi)

#if regular_literals[i]=1 it means that current hypothesis contains literal xi
regular_literals = np.ones(d-1) 
#if negative_literals[i]=1 it means that current hypothesis contains literal not(xi)
negative_literals = np.ones(d-1)

#so because our initial hypothesis is all_negative_hypothesis both sets of literals set to 1

################################################################################################################
############Start implement the Consistency Algorithm for the task of online boolean conjunction prediction#####
################################################################################################################

#start go over the values of each traingng instance without the last col of the y right prediction
for example in range(numOfTrainingExamples):
	for col in range(d-1):
		#first check if the prediction of current hypothesis with current example is 0or 1
		if(X[example][col] != negative_literals[col] and X[example][col] == regular_literals[col]):
			prediction = 1
		else: #It is enough that one literal to get a value of 0, 
			  #so that the value of the boolean conjunction to be false,
			  #so in that case we can end the loop action
			prediction =0
			break		
	#check the condition to enter the loop : given tag = 1 and predicted tag is 0
	if(Y[example] ==1 and prediction==0):
		for literal in range(d-1):
			#if the value of current literal is 0 :
			if(X[example][literal] == 0):
				#remove the regular literal by set its value to -1
				regular_literals[literal]=-1
			#if the value of current literal is 0 :
			elif(X[example][literal] == 1):
				#remove the negative literal by set its value to -1
				negative_literals[literal]=-1
#print(negative_literals) - for me

#now we can write the final result to output.txt file
file = open('output.txt','w') #open file in writing mode
#help varible to know if we need to add comma before or not
needComma=0
#looping through the literal who left after the machine learning algorithem
for i in range(d-1):
	if(regular_literals[i] == 1):		
		if(needComma==0):
			file.write("x"+str(i+1))
			needComma=1
		else:
			file.write(",x"+str(i+1))

	elif(negative_literals[i]== 1):
		
		if(needComma==0):
			file.write("not(x"+str(i+1)+")")
			needComma=1
		else:
			file.write(",not(x"+str(i+1)+")")
#close file
file.close()


