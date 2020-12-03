# importing libraries 
import numpy as np 
import cv2 
import imutils
import sys, getopt
# Create a VideoCapture object and read from input file 
def main(argv):
    monochrome = False
    file_path = 'video_1.mp4'
    fps = 5
    height = 480
    width = 600

    opts, args = getopt.getopt(argv,"hi:f:r:i:w:m:",["file","rfps","height","width","monochrome"])
    for opt, arg in opts:
        if opt == '-h':
            print('video_processor.py -i <inputfile> -r <fps> -i <height> -w <width> -m <monochrome>')
            sys.exit()
        elif opt in ("-f", "--file"):
            file_path = arg
        elif opt in ("-r", "--rfps"):
            fps = int(arg)
        elif opt in ("-i", "--height"):
            height = int(arg)
        elif opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-m", "--monochrome"):
            monochrome = bool(arg)

    cap = cv2.VideoCapture(file_path)

    # Check if camera opened successfully 
    if (cap.isOpened()== False): 
        print("Error opening video file") 

    i = 0
    tmpFrame = {}
    paused = False
    # Read until video is completed 
    while(cap.isOpened()): 
            
        # Capture frame-by-frame 
        ret, frame = cap.read() 
        if ret == True and i % fps==0: 
            key = cv2.waitKey(200)
            # Press Q on keyboard to exit 
            if key == ord('q'): 
                break
            if key == ord('p'):
                paused = True
                cv2.waitKey(-1)
            if paused and key == ord('b'):
                tmpFrame = imutils.resize(tmpFrame, width)
                tmpFrame = imutils.resize(tmpFrame, height)

                if monochrome:
                    grayFrame = cv2.cvtColor(tmpFrame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow('Frame', grayFrame)  
                else:
                    cv2.imshow('Frame', tmpFrame)
                cv2.waitKey(-1)
            
            # Display the resulting frame 
            frame = imutils.resize(frame, width)
            frame = imutils.resize(frame, height)

            if monochrome:
                grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('Frame', grayFrame)  
            else:
                cv2.imshow('Frame', frame)
            tmpFrame = frame
        # Break the loop 
        elif not ret: 
            break
        i+=1
    # When everything done, release 
    # the video capture object 
    cap.release() 

    # Closes all the frames 
    cv2.destroyAllWindows()
if __name__ == "__main__":
   main(sys.argv[1:])
