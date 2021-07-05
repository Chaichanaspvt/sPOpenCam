from CameraManager import CameraLineScan
import cv2
import threading


"""
Eaxmple Open Camera Balser Camera From OpenCV
Requirement 
pypylon version 1

"""

        

if __name__ == "__main__":
    #OpenCamera
    cam =  CameraLineScan()
    #Start thread CameraLineScan
    cam.run()
    while True:
        cv2.namedWindow('title', cv2.WINDOW_NORMAL)
        cv2.imshow('title', cam.getImage())
        k = cv2.waitKey(1)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.StopCamera()
            print("Close Camera")
            break
      
    cv2.destroyAllWindows()
          


