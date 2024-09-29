import cv2 as cv

img=cv.imread('Picture/Cat_Image.png')

def rescale_frame(frame,scale=0.75):
    #this works for images,videos and live videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

cv.imshow('Cat',img)
res=rescale_frame(img)
cv.imshow('Cat Resized',res)
cv.waitKey(0)


#Below is the code to change the resolution of a live video
# def changeres(width,height):
#     capture.set(3,width)  3 stands for width
#     capture.set(4,height) 4 stands for height
#This is to change res of a live video  




# Below is the code to resize a video
# while True:
#     istrue,frame=capture.read()
#     rf=rescale_frame(frame,scale=0.2)

#     cv.imshow('Cat',frame)
#     cv.imshow('Cat',rf)

#     if cv.waitKey(20) and 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
