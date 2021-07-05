"""
For Basler Camera 
A simple Program for grabing video from basler camera and converting it to opencv img.
Rebuild for SP VISION
https://www.sp-vt.com/
Basic Machine Vision on Youtube SP Vision Technology 
ChaichanaS
"""
from pypylon import pylon
import threading
import cv2

class CameraLineScan:
    def __init__(self):
          #Basler
        #conecting to the first available camera
        self.mstop = False
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

        # Grabing Continusely (video) with minimal delay
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
        self.converter = pylon.ImageFormatConverter()

        # converting to opencv bgr format
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
    def live_model(self):
        #Check Grab Image
       
        if self.camera.IsGrabbing():
            print("Line Scan On")
            print("Line Status ",self.camera.IsGrabbing())
        while self.camera.IsGrabbing():
            grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

            if grabResult.GrabSucceeded():
                # Access the image data
                image = self.converter.Convert(grabResult)
                self.img = image.GetArray()
                #off opencv window
                # cv2.namedWindow('title', cv2.WINDOW_NORMAL)
                # cv2.imshow('title', self.img)
                
                if self.mstop == True:
                    print("Line Scan off")
                    break
        #Stop Camera
        grabResult.Release()
        self.camera.StopGrabbing()
        # cv2.destroyAllWindows()
    def StopCamera(self):
        self.mstop = True
    def run(self):
        #start Thread CameraLineScan
        self.t1 = threading.Thread(target=self.live_model)
        #set Thread Daemon
        self.t1.daemon = True
        self.t1.start()
    def getImage(self):
        #get Image opencv format
            return self.img




