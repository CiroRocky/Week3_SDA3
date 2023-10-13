import cv2

# Open the saved video file for reading
cap = cv2.VideoCapture('output.avi')

# Read and display the video frames
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Show the video frame
        cv2.imshow('Video Playback', frame)

        # Break the loop if 'q' key is pressed or when the video ends
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
