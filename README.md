# Implement perceptron for the adult income dataset using Python.
Experiment with performance as a function of number of iterations.


Task
=============================================================================================================
Predict whether income exceeds $50K/yr based on census data. Also known as "Census Income" dataset.

First column is class label, remaining columns are a sparse representation
of the feature vector in format <feature>:<value>.  All other features are 0.

more information on the task:
http://archive.ics.uci.edu/ml/datasets/Adult

preprocessed version from: 
http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html


Instructions for running "Perceptron.py"
=============================================================================================================
To run the script "Perceptron.py" type "python3 Perceptron.py"
The default number of iterations is 10 and it will use the dev set.

We can also specify the number of iterations to run using the optional argument "--iterations" and
whether to use the dev set or not using the optional argument "--nodev"


Output
=============================================================================================================
Reading file: adult/a7a.train
Running Perceptron...
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
Iteration: 5
Iteration: 6
Iteration: 7
Iteration: 8
Iteration: 9
Iteration: 10
Reading file: adult/a7a.dev
Accuracies on dev set: [0.7875, 0.81675, 0.80025, 0.783125, 0.802875, 0.809375, 0.809375, 0.81025, 0.74875, 0.819125]
Reading file: adult/a7a.test
Test accuracy: 0.8124335184966316
Feature weights (bias last): -6.0 -3.0 4.0 3.0 -2.0 0.0 -1.0 6.0 10.0 1.0 1.0 -6.0 0.0 -9.0 3.0 4.0 -2.0 0.0 -2.0 -1.0 0.0 -1.0 1.0 -1.0 3.0 1.0 -5.0 7.0 -1.0 2.0 1.0 7.0 -3.0 -12.0 -9.0 -1.0 -1.0 2.0 5.0 8.0 -4.0 -5.0 -6.0 -1.0 -6.0 10.0 2.0 0.0 0.0 3.0 8.0 -1.0 0.0 2.0 0.0 -5.0 -3.0 -2.0 7.0 0.0 5.0 -1.0 -4.0 0.0 -3.0 -1.0 0.0 4.0 -2.0 -3.0 -3.0 -4.0 0.0 -7.0 3.0 -7.0 3.0 -5.0 -1.0 -3.0 2.0 3.0 5.0 8.0 4.0 -5.0 8.0 -2.0 0.0 -9.0 5.0 -1.0 -1.0 -4.0 5.0 -1.0 0.0 4.0 5.0 4.0 2.0 -10.0 -1.0 -3.0 8.0 0.0 -5.0 -2.0 12.0 -3.0 0.0 -8.0 -6.0 3.0 5.0 6.0 -6.0 12.0 2.0 -4.0 -8.0 -3.0 0.0 -4.0
