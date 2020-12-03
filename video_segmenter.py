# importing libraries 
import numpy as np 
import cv2 
from matplotlib import pyplot as plt
import sys, getopt, os

 
def main(argv):
    input_file_path = 'video_1.mp4'
    output_file_path = os.path.splitext(input_file_path)[0]+'_processed.mp4'

    opts, args = getopt.getopt(argv,"hi:i:o:",["input","output"])
    for opt, arg in opts:
        if opt == '-h':
            print('video_segmenter.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--input"):
            input_file_path = str(arg)
        elif opt in ("-o", "--output"):
            output_file_path = str(arg)
    
    cap = cv2.VideoCapture(input_file_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    out = cv2.VideoWriter(output_file_path, -1,fps, (int(width), int(height)))

    # Check if camera opened successfully 
    if (cap.isOpened()== False): 
        print("Error opening video file") 
    
    # Read until video is completed 
    back_sub = cv2.createBackgroundSubtractorMOG2()
    while(cap.isOpened()): 
            
        # Capture frame-by-frame 
        ret, frame = cap.read() 
        if ret == True: 
            key = cv2.waitKey(5)
            # Press Q on keyboard to exit 
            if key == ord('q'): 
                break
            
            fg_mask = back_sub.apply(frame)
    
    
            cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
            cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
            
            
            # cv2.imshow('Frame', frame)
            # cv2.imshow('FG Mask', fgMask)

            res = cv2.bitwise_and(frame,frame,mask = fg_mask)
            # cv2.imshow('result', res)

            out.write(res)

        # Break the loop 
        elif not ret: 
            break
    # When everything done, release 
    # the video capture object 
    cap.release() 
    out.release()
    # Closes all the frames 
    cv2.destroyAllWindows()
if __name__ == "__main__":
   main(sys.argv[1:])
