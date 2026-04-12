import cv2

# Load image
image = cv2.imread("sample.jpg") 

print("Shape of image:", image.shape)


print("\nSample pixel values:\n", image[:5, :5])

if len(image.shape) == 3:
    print("\nChannels:", image.shape[2])
else:
    print("\nGrayscale image (1 channel)")