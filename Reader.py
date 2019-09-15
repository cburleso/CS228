import pickle
class READER:
    def __init__(self):
        pickleIn = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/userData/gesture.p', 'rb')
        gestureData = pickle.load(pickleIn)
        print(gestureData)
