import numpy
import pickle as np

pickleIn1 = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/train7.p', 'rb')
train7 = np.load(pickleIn1)
#print(train7)
#print(train7.shape)

pickleIn2 = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/train8.p', 'rb')
train8 = np.load(pickleIn2)
#print(train8)
#print(train8.shape)


pickleIn3 = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/test7.p', 'rb')
test7 = np.load(pickleIn3)
#print(test7)
#print(test7.shape)


pickleIn4 = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/test8.p', 'rb')
test8 = np.load(pickleIn4)
#print(test8)
#print(test8.shape)

def ReshapeData(set1, set2):
    X = np.zeros((2000,5*2*3),dtype='f')
    for frame in range(0, 1000):
        col = 0
        for finger in range(0, 5):
            for bone in range(0, 4):
                for coordinate in range(0, 6):
                    X[row, col] = set1[finger, bone, coordinate, frame]
                    col = col + 1
    return X

trainX = ReshapeData(train7, train8)
print(trainX)
print(trainX.shape)


    
