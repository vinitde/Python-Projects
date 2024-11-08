import cv2
import numpy as np

def remove_specular_highlight(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect specular highlights using a threshold
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    # Inpainting to remove specular highlights
    inpainted_image = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
    
    return inpainted_image

# Load the image
image = cv2.imread('strawberries.jpg')

# Remove specular highlights
result_image = remove_specular_highlight(image)

# Display the original and result images
cv2.imshow('Original Image', image)
cv2.imshow('Specular Highlight Removed', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
