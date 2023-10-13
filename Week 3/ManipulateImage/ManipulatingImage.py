import cv2
import numpy as np

# Load the image from the same directory as your script
image_path = r"C:\Users\pixel\OneDrive\Documents\fontys\Year 2\SDA3\Week 3\ManipulateImage\SDA_Dog.png"
# Load the image
original_image = cv2.imread(image_path)

# Show the original image
cv2.imshow("Original Image", original_image)
cv2.waitKey(0)

# Resize the image to 60%
resized_image = cv2.resize(original_image, None, fx=0.6, fy=0.6)

# Convert the resized image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Show the grayscale image
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)

# Crop the image to size 400x400, starting at (20, 20)
cropped_image = resized_image[20:420, 20:420]

# Draw a yellow circle on the top-left corner of the cropped image
cv2.circle(cropped_image, (40, 40), 20, (0, 255, 255), 2)

# Draw a blue filled ellipse on the top-right corner of the cropped image
cv2.ellipse(cropped_image, (380, 40), (75, 40), 0, 0, 360, (255, 0, 0), -1)

# Draw an unfilled square in the bottom-left corner
cv2.rectangle(cropped_image, (40, 360), (85, 405), (192, 75, 15), 1)

# Draw a filled square in the bottom-right corner
cv2.rectangle(cropped_image, (315, 360), (360, 405), (192, 75, 15), -1)

# Show the final cropped and modified image
cv2.imshow("Modified Image", cropped_image)
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
