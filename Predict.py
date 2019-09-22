import matplotlib.pyplot as plt
import numpy as np
from knn import KNN

knn = KNN()
knn.Load_Dataset('iris.csv')

x = knn.data[:, 0] # col one / first iris feature 
y = knn.data[:, 1] # col two / second iris feature

# training set 
trainX = knn.data[::2, 1:3] # col two and three , 'even' rows 
trainy = knn.target[::2]

# test set
testX = knn.data[1::2, 1:3] # col two and three, 'odd' rows 
testy = knn.target[1::2]

# applying kNN to Iris data set
knn.Use_K_Of(15)
knn.Fit(trainX, trainy)
for i in range(75):
    actualClass = testy[i]
    prediction = knn.Predict(testX[i, :])
    # print(actualClass, prediction)

# colors matrix
colors = np.zeros((3, 3), dtype='f')
colors[0, :] = [1, 0.5, 0.5]
colors[1, :] = [0.5, 1, 0.5]
colors[2, :] = [0.5, 0.5, 1]

# visualization lines

# training points loop
plt.figure()
[numItems, numFeatures] = knn.data.shape
for i in range(0, numItems / 2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass, :]
    plt.scatter(trainX[i, 0], trainX[i, 1], facecolor=currColor, s = 50,
            lw = 2)

numCorrect = 0
# testing points loop
[numItems, numFeatures] = knn.data.shape
for i in range(0, numItems / 2):
    prediction = int(knn.Predict(testX[i, :]))
    edgeColor = colors[prediction, :]
    itemClass = int(testy[i])
    currColor = colors[itemClass, :]
    if (prediction == itemClass):
        numCorrect += 1
    plt.scatter(testX[i, 0], testX[i, 1], facecolor=currColor, s = 50, lw = 2,
                edgecolor = edgeColor)

percentCorrect = float((numCorrect / 75.) * 100.)
print(percentCorrect)
    
#plt.scatter(trainX[:,0], trainX[:,1], c = trainy) # plot training set 
#plt.scatter(testX[:,0], testX[:,1], c = testy) # plot test set 
plt.show()


