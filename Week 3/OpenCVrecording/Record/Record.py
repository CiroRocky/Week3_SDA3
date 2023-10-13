import cv2
import time

# Initialize video capture from the default camera (0)
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Record for a maximum of 5 seconds
start_time = time.time()
while cap.isOpened() and time.time() - start_time <= 5:
    ret, frame = cap.read()
    if ret:
        # Show the video stream
        cv2.imshow('Video Stream', frame)

        # Write the frame to the output video file
        out.write(frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release video capture and writer, and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
