from PIL import Image
import cv2
def transpose_image(im,im1):
    #OPENING THE IMAGE
    img = Image.open(im)
    #TRANSPOSING THE IMAGE
    transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
    transposed_img.save(im1)
    print("done flipping")
def rotate_image(im,degree):
    #OPENING THE IMAGE
    img = Image.open(im)
    #rotate img 180
    rotateimg=img.rotate(degree)
    rotateimg.show()
def grayscale(im,im1):
    #cv2
    img=cv2.imread(im)
    #preparation for clahe
    clahe=cv2.createCLAHE()
    #convert to gray scale image
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #apply enhancement
    enh_img=clahe.apply(gray_img)
    cv2.imwrite(im1,enh_img)
    print('done enhancing')
print("welcome to image processing"+"\n"+"1.transpose the imaage \n2.rotate the image\n3.grayscale color")
choice=int(input("enter your choice 1 or 2 or 3\n"))          
im=input("\nenter the path for image :")
if(choice==1):
           im1=input("\nenter the path for saving the imge:")
           transpose_image(im,im1)
elif(choice==2):
    degree=int(input("enter the degree for rotating the image:"))
    rotate_image(im,degree)
elif(choice==3):
    im1=input("\nenter the path for saving the imge:")
    grayscale(im,im1)
else:
    print("invalid choice")
    
    
