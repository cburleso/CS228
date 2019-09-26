import pickle
import numpy as np
from knn import KNN

openTrain7File = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/train7.p', 'rb')
openTrain8File = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/train8.p', 'rb')
openTest7File = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/test7.p', 'rb')
openTest8File = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/test8.p', 'rb')

def ReduceData(X):
    X = np.delete(X,1,1)
    X = np.delete(X,1,1)
    return X

def CenterData(X):
    allXCoordinates = X[:,:,0,:]
    meanValue = allXCoordinates.mean()
    X[:,:,0,:] = allXCoordinates - meanValue
    
    allYCoordinates = X[:,:,1,:]
    meanValue = allYCoordinates.mean()
    X[:,:,1,:] = allYCoordinates - meanValue
    
    allZCoordinates = X[:,:,2,:]
    meanValue = allZCoordinates.mean()
    X[:,:,2,:] = allZCoordinates - meanValue
    return X

train7 = pickle.load(openTrain7File)
train7 = ReduceData(train7)
train7 = CenterData(train7)

train8 = pickle.load(openTrain8File)
train8 = ReduceData(train8)
train8 = CenterData(train8)

test7 = pickle.load(openTest7File)
test7 = ReduceData(test7)
test7 = CenterData(test7)

test8 = pickle.load(openTest8File)
test8 = ReduceData(test8)
test8 = CenterData(test8)

##print(train5.shape)
##print(train6.shape)
##print(test5.shape)
##print(test6.shape)


    
def ReshapeData(set1,set2):
    X = np.zeros((2000,5*2*3),dtype='f')
    y = np.zeros(2000,dtype='f')
    for row in range(0,1000):
        col = 0
        for j in range(0,5):
            for k in range(0,2):
                for m in range(0,3):
                    y[row] = 5
                    y[row+1000] = 6
                    X[row,col] = set1[j,k,m,row]
                    X[row+1000,col] = set2[j,k,m,row]
                    col = col + 1
    return X,y

trainX, trainy = ReshapeData(train7, train8)
testX, testy = ReshapeData(test7,test8)
##print(trainX)
##print(trainX.shape)
##print(trainy)
##print(trainy.shape)
##print(testX)
##print(testX.shape)
##print(testy)
##print(testy.shape)

knn = KNN()
knn.Use_K_Of(15)
knn.Fit(trainX,trainy)

predictCorrect = 0
for row in range(0,2000):
    prediction = int(knn.Predict(testX[row,:]))
    actualClass = int(testy[row])
    #print(row,prediction,actualClass)
    if (prediction == actualClass):
        predictCorrect += 1
percentage = float(predictCorrect)
percentage = percentage/2000
percentage = percentage * 100
print("Accuracy: " + str(percentage))
