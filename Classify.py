import numpy
import pickle as np

pickleIn = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/userData/gesture.p', 'rb')
gestureData = np.load(pickleIn)
print(gestureData.shape)

