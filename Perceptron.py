#!/usr/bin/python3

# Author: Deepak Pandita
# Date created: 26 Jan 2018

import numpy as np
import argparse
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


#using optional parameters
parser = argparse.ArgumentParser()
parser.add_argument('--iterations', action="store", help = "No. of iterations to run", type = int)
parser.add_argument('--nodev', help = "Not use the dev set", action = "store_true")
args = parser.parse_args()

#file paths
train_file = '/data/adult/a7a.train'
dev_file = '/data/adult/a7a.dev'
test_file = '/data/adult/a7a.test'


#default no. of iterations
iterations  = 10
dev = True

if args.iterations:
	iterations = args.iterations
if args.nodev:
	dev=False

#Read train file
print('Reading file: '+train_file)
f = open(train_file)
train_examples = f.readlines()
f.close()


#weights (There are 123 features in the data + bias)
w = np.zeros(124)
Ws = []

#Perceptron
print('Running Perceptron...')
iter = 0
while(iter<iterations):
	iter+=1
	print('Iteration: ' + str(iter))
	
	for line in train_examples:
		tokens = line.strip().split(' ')
		y = float(tokens[0])	#label
		instance = tokens[1:]
		x=np.zeros(124)
		x[-1]=1.0
		for token in instance:
			feature = int(token.split(":")[0])
			value = float(token.split(":")[1])
			#print feature
			x[feature-1] = value
		if y*sum(w*x) <= 0:
			w+=y*x
	
	Ws.append(w.tolist())

#This function predicts the label on given examples using given weights and returns the accuracy
def predict(examples,W):
	correct = 0
	for line in examples:
		tokens = line.strip().split(' ')
		y = float(tokens[0])	#label
		instance = tokens[1:]
		x=np.zeros(124)
		x[-1]=1.0
		for token in instance:
			feature = int(token.split(":")[0])
			value = float(token.split(":")[1])
			#print feature
			x[feature-1] = value
		if y*sum(W*x) > 0:
			correct+=1
	accuracy = float(correct)/len(examples)
	return accuracy

#If dev set is given
if dev:
	#Read dev file
	print('Reading file: '+dev_file)
	d = open(dev_file)
	dev_examples = d.readlines()
	d.close()

	accuracies = []
	for W in Ws:
		accuracy = predict(dev_examples,W)
		accuracies.append(accuracy)
	print("Accuracies on dev set: " + str(accuracies))

	plt.plot(accuracies)
	plt.xlabel("#Iterations")
	plt.ylabel("Accuracy")
	plt.title("Plot of accuracy on dev set")
	plt.show()

#Read test file
print('Reading file: '+test_file)
t = open(test_file)
test_examples = t.readlines()
t.close()

accuracy = predict(test_examples,w)
print("Test accuracy: " + str(accuracy))
weight_str = ""
for wt in w:
	weight_str += str(wt)+" "
print("Feature weights (bias last): "+weight_str.strip())