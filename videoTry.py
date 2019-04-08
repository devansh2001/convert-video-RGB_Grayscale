import numpy as np
import cv2

def convertVideo(video):
    cap = cv2.VideoCapture(video)

    ret, frame = cap.read()
    height = frame.shape[0]
    width = frame.shape[1]

    fps = 25.0
    size = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    # initialize Output file control
    out = cv2.VideoWriter('Output.avi', fourcc, fps, size, 0)

    while(cap.isOpened()):
        ret, frame = cap.read()

        # check if any more frames are left
        if not ret: break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = gray

        # Add frame to final video
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break

    # Release all memory after loop is over
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    videoPath = 'trial.mp4'
    convertVideo(videoPath)

if __name__ == '__main__':
    main()
