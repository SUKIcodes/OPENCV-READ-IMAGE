#AUTHOR - KING
#TECHNOLOGY - OPENCV


#HOW TO READ IMAGE 
#---------------------------------------------------------------------------

# import cv2
# img1 = cv2.imread("C:\\Users\\KING\\Pictures\\Screenshots\\image.png")
# img1 = cv2.resize(img1, (1280,700))
# print(img1)
# cv2.imshow("ORIGINAL",img1)
# cv2.waitKey(0)   
# cv2.destroyAllWindows() 

#HOW TO CONVER IMAGE TO GRAY
#---------------------------------------------------------------------------

# import cv2
# img1 = cv2.imread("C:\\Users\\KING\\Pictures\\Screenshots\\image.png",0)
# img1 = cv2.resize(img1, (1280,700))
# print(img1)
# cv2.imshow("ORIGINAL",img1)
# cv2.waitKey(0)   
# cv2.destroyAllWindows() 

#CONVERT IMAGE TOGRAY AND SAVE ALSO
#---------------------------------------------------------------------------

# import cv2
# path = input("Enter Image Path...")
# img1 = cv2.imread(path,0)
# img1 = cv2.resize(img1, (560,700))
# img1 = cv2.flip(img1,0)
# cv2.imshow("Image",img1)
# k = cv2.waitKey(0)
# if k==ord("s"):
#     cv2.imwrite("C:\\Users\\KING\\Pictures\\Screenshots\\output.png", img1)
# else:
#   cv2.destroyAllWindows()  

# HOW TO READ VIDEO
#---------------------------------------------------------------------------

# import cv2
# cap = cv2.VideoCapture(0)
# while True:
#     ret,frame = cap.read()
#     frame = cv2.resize(frame, (700,450))
#     cv2.imshow("VIDEO", frame)
#     k = cv2.waitKey(25)
#     if k == ord("q") & 0xFF:
#         break
# cap.release()
# cv2.destroyAllWindows()    
    
#TO CONVERT VIDEO INTO GRAY
#----------------------------------------------------------------------------

# import cv2
# cap = cv2.VideoCapture(0)
# while True:
#     ret,frame = cap.read()
#     frame = cv2.resize(frame, (700,450))
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("VIDEO", gray)
#     k = cv2.waitKey(25)
#     if k == ord("q") & 0xFF:
#         break
# cap.release()
# cv2.destroyAllWindows()  

# READ VIDEO AND SAVE
#----------------------------------------------------------------------------
# import cv2
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# output = cv2.VideoWriter("output.mp4",fourcc,20.0,(640,480)) #last ,0 if gray image 
# while cap.isOpened():
#     ret,frame = cap.read()
#     if ret == True:
#         frame = cv2.resize(frame, (640,480))
#         cv2.imshow("VIDEO",frame)
#         output.write(frame)
#         k = cv2.waitKey(25)
#         if k == ord("q"):
#             break
# cap.release()
# output.release()
# cv2.destroyAllWindows()        

# ACCESS MOBILE CAMERA 
#-----------------------------------------------------------------------------
# import cv2
# camera = "http://192.168.0.102/video"
# cap = cv2.VideoCapture(0)
# cap.open(camera)
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# output = cv2.VideoWriter("output.mp4",fourcc,20.0,(640,480)) #last ,0 if gray image 
# while cap.isOpened():
#     ret,frame = cap.read()
#     if ret == True:
#         frame = cv2.resize(frame, (640,480))
#         cv2.imshow("VIDEO",frame)
#         output.write(frame)
#         k = cv2.waitKey(25)
#         if k == ord("q"):
#             break
# cap.release()
# output.release()
# cv2.destroyAllWindows() 



