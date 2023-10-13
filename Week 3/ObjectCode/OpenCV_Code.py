import cv2
import numpy as np

def detect_red_square(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper thresholds for red color
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # If the contour has 4 vertices and meets area and aspect ratio criteria, it's a square
        if len(approx) == 4:
            area = cv2.contourArea(approx)
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h

            # Adjust these values based on the size and shape of your square
            area_threshold = 1000  # Example area threshold
            aspect_ratio_threshold = 0.9  # Example aspect ratio threshold

            # Check if the contour meets the criteria
            if area > area_threshold and aspect_ratio > aspect_ratio_threshold:
                # Calculate the centroid of the square
                M = cv2.moments(approx)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # Draw the centroid and contour on the frame
                cv2.circle(frame, (cX, cY), 10, (0, 0, 255), -1)
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)

                # Print centroid coordinates
                print(f"Red square detected at coordinates: ({cX}, {cY})")

                # Here, you can add logic to control the robot arm based on the detected object's position

    return frame

# Initialize the webcam (assuming 0 for the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Detect the red square and get the updated frame
    frame = detect_red_square(frame)

    # Display the frame
    cv2.imshow("Red Square Detection", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
