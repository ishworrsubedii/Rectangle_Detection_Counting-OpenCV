# Importing openCV and numpy
 
import cv2 as cv
import numpy as np

# Load input image from Input Images Folder
image = cv.imread('Input Images\Input_Rectangle.png')

# Extract four rectangular regions from original image
rectangle_1 = image[200:500, 300:700]
rectangle_2 = image[0:200, 0:250]
rectangle_3 = image[0:200, 300:600]
rectangle_4 = image[200:600, 0:300]

# Function to rotate an image according to different angle
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# Rotate each rectangle using different angle
rectangle_1 = rotate(rectangle_1, 30)
cv.imshow('Rectangle 1', rectangle_1)

rectangle_2 = rotate(rectangle_2, 15)
cv.imshow('Rectangle 2', rectangle_2)

rectangle_3 = rotate(rectangle_3, -15)
cv.imshow('Rectangle 3', rectangle_3)

rectangle_4 = rotate(rectangle_4, -30)
cv.imshow('Rectangle 4', rectangle_4)

# Save the rotated images to Output Image Folder
cv.imwrite('Output Images\Straight_Rectangle_1.png', rectangle_1)
cv.imwrite('Output Images\Straight_Rectangle_2.png', rectangle_2)
cv.imwrite('Output Images\Straight_Rectangle_3.png', rectangle_3)
cv.imwrite('Output Images\Straight_Rectangle_4.png', rectangle_4)

cv.waitKey(0)
cv.destroyAllWindows()
