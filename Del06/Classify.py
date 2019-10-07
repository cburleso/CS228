import pickle
import numpy as np
from knn import KNN


openTrain0File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_train0.p", 'rb')
openTest0File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_test0.p", 'rb')
openTrain0File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Clark_train0.p", 'rb')
openTest0File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Clark_test0.p", 'rb')

openTrain1File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Genovese_train1.p", 'rb')
openTest1File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Genovese_test1.p", 'rb')
openTrain1File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Newton_train1.p", 'rb')
openTest1File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Newton_test1.p", 'rb')

openTrain2File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Gordon_train2.p", 'rb')
openTest2File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Gordon_test2.p", 'rb')
openTrain2File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Gordon_train2.p", 'rb')
openTest2File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Gordon_test2.p", 'rb')

openTrain3File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Liu_train3.p", 'rb')
openTest3File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Liu_test3.p", 'rb')
openTrain3File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Trinity_train3.p", 'rb')
openTest3File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Trinity_test3.p", 'rb')

openTrain4File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Warren_train4.p", 'rb')
openTest4File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Warren_test4.p", 'rb')
openTrain4File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Ortigara_train4.p", 'rb')
openTest4File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Ortigara_test4.p", 'rb')


# ME DATA
openTrain5File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_train5.p", 'rb')
openTrain6File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_train6.p", 'rb')
openTest5File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_test5.p", 'rb')
openTest6File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_test6.p", 'rb')
openTrain5File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_train5.p", 'rb')
openTrain6File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_train6.p", 'rb')
openTest5File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_test5.p", 'rb')
openTest6File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_test6.p", 'rb')


openTrain7File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_train7.p", 'rb')
openTest7File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_test7.p", 'rb')
openTrain7File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Yeung_train7.p", 'rb')
openTest7File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Yeung_test7.p", 'rb')

openTrain8File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Rubin_train8.p", 'rb')
openTest8File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Rubin_test8.p", 'rb')
openTrain8File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Mardis_train8.p", 'rb')
openTest8File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Mardis_test8.p", 'rb')

openTrain9File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_train9.p", 'rb')
openTest9File = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Burleson_test9.p", 'rb')
openTrain9File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Lee_train9.p", 'rb')
openTest9File_ = open(r"C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/Del06/userData/Lee_test9.p", 'rb')



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

train0 = pickle.load(openTrain0File)
train0 = ReduceData(train0)
train0 = CenterData(train0)
test0 = pickle.load(openTest0File)
test0 = ReduceData(test0)
test0 = CenterData(test0)
train0_ = pickle.load(openTrain0File_)
train0_ = ReduceData(train0_)
train0_ = CenterData(train0_)
test0_ = pickle.load(openTest0File_)
test0_ = ReduceData(test0_)
test0_ = CenterData(test0_)

train1 = pickle.load(openTrain1File)
train1 = ReduceData(train1)
train1 = CenterData(train1)
test1 = pickle.load(openTest1File)
test1 = ReduceData(test1)
test1 = CenterData(test1)
train1_ = pickle.load(openTrain1File_)
train1_ = ReduceData(train1_)
train1_ = CenterData(train1_)
test1_ = pickle.load(openTest1File_)
test1_ = ReduceData(test1_)
test1_ = CenterData(test1_)

train2 = pickle.load(openTrain2File)
train2 = ReduceData(train2)
train2 = CenterData(train2)
test2 = pickle.load(openTest2File)
test2 = ReduceData(test2)
test2 = CenterData(test2)
train2_ = pickle.load(openTrain2File_)
train2_ = ReduceData(train2_)
train2_ = CenterData(train2_)
test2_ = pickle.load(openTest2File_)
test2_ = ReduceData(test2_)
test2_ = CenterData(test2_)

train3 = pickle.load(openTrain3File)
train3 = ReduceData(train3)
train3 = CenterData(train3)
test3 = pickle.load(openTest3File)
test3 = ReduceData(test3)
test3 = CenterData(test3)
train3_ = pickle.load(openTrain3File_)
train3_ = ReduceData(train3_)
train3_ = CenterData(train3_)
test3_ = pickle.load(openTest3File_)
test3_ = ReduceData(test3_)
test3_ = CenterData(test3_)

train4 = pickle.load(openTrain4File)
train4 = ReduceData(train4)
train4 = CenterData(train4)
test4 = pickle.load(openTest4File)
test4 = ReduceData(test4)
test4 = CenterData(test4)
train4_ = pickle.load(openTrain4File_)
train4_ = ReduceData(train4_)
train4_ = CenterData(train4_)
test4_ = pickle.load(openTest4File_)
test4_ = ReduceData(test4_)
test4_ = CenterData(test4_)

#######MEEEE#####
train5 = pickle.load(openTrain5File)
train5 = ReduceData(train5)
train5 = CenterData(train5)
train5_ = pickle.load(openTrain5File_)
train5_ = ReduceData(train5_)
train5_ = CenterData(train5_)

train6 = pickle.load(openTrain6File)
train6 = ReduceData(train6)
train6 = CenterData(train6)
train6_ = pickle.load(openTrain6File_)
train6_ = ReduceData(train6_)
train6_ = CenterData(train6_)

test5 = pickle.load(openTest5File)
test5 = ReduceData(test5)
test5 = CenterData(test5)
test5_ = pickle.load(openTest5File_)
test5_ = ReduceData(test5_)
test5_ = CenterData(test5_)

test6 = pickle.load(openTest6File)
test6 = ReduceData(test6)
test6 = CenterData(test6)
test6_ = pickle.load(openTest6File_)
test6_ = ReduceData(test6_)
test6_ = CenterData(test6_)
#####################
train7 = pickle.load(openTrain7File)
train7 = ReduceData(train7)
train7 = CenterData(train7)
test7 = pickle.load(openTest7File)
test7 = ReduceData(test7)
test7 = CenterData(test7)
train7_ = pickle.load(openTrain7File_)
train7_ = ReduceData(train7_)
train7_ = CenterData(train7_)
test7_ = pickle.load(openTest7File_)
test7_ = ReduceData(test7_)
test7_ = CenterData(test7_)

train8 = pickle.load(openTrain8File)
train8 = ReduceData(train8)
train8 = CenterData(train8)
test8 = pickle.load(openTest8File)
test8 = ReduceData(test8)
test8 = CenterData(test8)
train8_ = pickle.load(openTrain8File_)
train8_ = ReduceData(train8_)
train8_ = CenterData(train8_)
test8_ = pickle.load(openTest8File_)
test8_ = ReduceData(test8_)
test8_ = CenterData(test8_)

train9 = pickle.load(openTrain9File)
train9 = ReduceData(train9)
train9 = CenterData(train9)
test9 = pickle.load(openTest9File)
test9 = ReduceData(test9)
test9 = CenterData(test9)
train9_ = pickle.load(openTrain9File_)
train9_ = ReduceData(train9_)
train9_ = CenterData(train9_)
test9_ = pickle.load(openTest9File_)
test9_ = ReduceData(test9_)
test9_ = CenterData(test9_)
##print(train5.shape)
##print(train6.shape)
##print(test5.shape)
##print(test6.shape)


    
def ReshapeData(set0,set1,set2,set3,set4,set5,set6,set7,set8,set9,set10,set11,set12,set13,set14,set15,set16,set17,set18,set19):
    X = np.zeros((20000,5*2*3),dtype='f')
    y = np.zeros(20000,dtype='f')
    for row in range(0,1000):
        col = 0
        for j in range(0,5):
            for k in range(0,2):
                for m in range(0,3):
                    X[row,col]          = set0[j,k,m,row] 
                    y[row]                = 0

                    X[row+1000,col] = set1[j,k,m,row]
                    y[row+1000]       = 1

                    X[row+2000,col] = set2[j,k,m,row]
                    y[row+2000]       = 2

                    X[row+3000,col] = set3[j,k,m,row]
                    y[row+3000]       = 3

                    X[row+4000,col] = set4[j,k,m,row]
                    y[row+4000]       = 4

                    X[row+5000,col] = set5[j,k,m,row]
                    y[row+5000]       = 5

                    X[row+6000,col] = set6[j,k,m,row]
                    y[row+6000]       = 6

                    X[row+7000,col] = set7[j,k,m,row]
                    y[row+7000]       = 7

                    X[row+8000,col] = set8[j,k,m,row]
                    y[row+8000]       = 8

                    X[row+9000,col] = set9[j,k,m,row]
                    y[row+9000]       = 9

                    X[row+10000,col]          = set10[j,k,m,row] 
                    y[row+10000]                = 0

                    X[row+11000,col] = set11[j,k,m,row]
                    y[row+11000]       = 1

                    X[row+12000,col] = set12[j,k,m,row]
                    y[row+12000]       = 2

                    X[row+13000,col] = set13[j,k,m,row]
                    y[row+13000]       = 3

                    X[row+14000,col] = set14[j,k,m,row]
                    y[row+14000]       = 4

                    X[row+15000,col] = set15[j,k,m,row]
                    y[row+15000]       = 5

                    X[row+16000,col] = set16[j,k,m,row]
                    y[row+16000]       = 6

                    X[row+17000,col] = set17[j,k,m,row]
                    y[row+17000]       = 7

                    X[row+18000,col] = set18[j,k,m,row]
                    y[row+18000]       = 8

                    X[row+19000,col] = set19[j,k,m,row]
                    y[row+19000]       = 9
                    
                    col += 1
    return X,y

trainX, trainy = ReshapeData(train0,train1,train2,train3,train4,train5,train6,train7,train8,train9,train0_,train1_,train2_,train3_,train4_,train5_,train6_,train7_,train8_,train9_)
testX, testy = ReshapeData(test0,test1,test2,test3,test4,test5,test6,test7,test8,test9,test0_,test1_,test2_,test3_,test4_,test5_,test6_,test7_,test8_,test9_)
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
##for row in range(0,10000):
##    prediction = int(knn.Predict(testX[row,:]))
##    actualClass = int(testy[row])
##    print(row,prediction,actualClass)
##    if (prediction == actualClass):
##        predictCorrect += 1
##percentage = float(predictCorrect)
##percentage = percentage/2000
##percentage = percentage * 100
##print("Accuracy: " + str(percentage))

# START DEL6
pickle.dump(knn,open('userData/classifier.p','wb'))
