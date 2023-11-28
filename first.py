import cv2
img1 = cv2.imread("Path of the image")
img1 = cv2.resize(img1, (1280,700))
print(img1)
cv2.imshow("ORIGINAL",img1)
cv2.waitKey(0)   
cv2.destroyAllWindows() 


