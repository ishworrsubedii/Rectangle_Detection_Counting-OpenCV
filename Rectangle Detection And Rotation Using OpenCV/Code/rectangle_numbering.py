# Importing OpenCV library
import cv2 as cv

# Loading input from Input image folder
img = cv.imread('Input Images\Input_Rectangle.png')

# Converting image intoto grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Performing Canny edge detection on the above image
edges = cv.Canny(gray, 100, 200)

contours, hierarchy = cv.findContours(
    edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Counting Labels 
numbers = ["1", "4", "2", "3"]

for i, contour in enumerate(contours):

    epsilon = 0.01 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)

    if len(approx) == 4:
        # Green rectangle
        cv.drawContours(img, [contour], -1, (0, 255, 0), 3)
        x, y, w, h = cv.boundingRect(contour)
        cv.putText(img, numbers[i], (x, y - 0),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Image showing
cv.imshow('output', img)

# Saving Images
cv.imwrite('Output Images\Rectangle_Image_count.png', img)
cv.imwrite('Output Images\Edge_Detection_Image.png', edges)


cv.waitKey(0)
cv.destroyAllWindows()
