import cv2
import matplotlib.pyplot as plt

# Function to display images in Jupyter Notebook
def display_image(img, title=''):
    plt.figure(figsize=(8, 6))
    if len(img.shape) == 3:
        # Convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Read the image
image = cv2.imread("C:\\Users\\itzgo\\Downloads\\gettyimages-185071733-612x612.jpg")

# Display original image
display_image(image, 'Original Image')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
display_image(gray_image, 'Grayscale Image')

# Resize image
resized_image = cv2.resize(image, (200, 200))
display_image(resized_image, 'Resized Image')

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
display_image(blurred_image, 'Blurred Image')

# Detect edges
edges = cv2.Canny(gray_image, 100, 200)
display_image(edges, 'Edges')

# Draw rectangle and line
image_with_shapes = image.copy()
cv2.rectangle(image_with_shapes, (50, 50), (300, 300), (255, 0, 0), 2)
cv2.line(image_with_shapes, (60, 60), (300, 300), (0, 0, 255), 2)
display_image(image_with_shapes, 'Image with Shapes')
