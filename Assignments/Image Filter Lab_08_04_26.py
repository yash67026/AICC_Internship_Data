import cv2

# Load image
image = cv2.imread("Sample.jpg")  # replace with your image path

if image is None:
    print("Error: Image not found")
    exit()

# 1. Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Blur (Gaussian Blur)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. Edge Detection (Canny)
edges = cv2.Canny(blur, 100, 200)

# Show images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blurred", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
