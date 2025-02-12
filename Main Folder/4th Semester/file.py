# # Python code to read image
# import cv2

# # To read image from disk, we use
# # cv2.imread function, in below method,
# img = cv2.imread(r"C:\Users\DELL\OneDrive\Desktop\Main Folder\pic23-300x243.png", cv2.IMREAD_COLOR)

# # Creating GUI window to display an image on screen
# # first Parameter is windows title (should be in string format)
# # Second Parameter is image array
# cv2.imshow("1.png", img)

# # To hold the window on screen, we use cv2.waitKey method
# # Once it detected the close input, it will release the control
# # To the next line
# # First Parameter is for holding screen for specified milliseconds
# # It should be positive integer. If 0 pass an parameter, then it will
# # hold the screen until user close it.
# cv2.waitKey(0)

# # It is for removing/deleting created GUI window from screen
# # and memory
# cv2.destroyAllWindows()

#import cv2, numpy and matplotlib libraries
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread(r"C:\Users\DELL\OneDrive\Desktop\Main Folder\pic23-300x243.png")
# #Displaying image using plt.imshow() method
# plt.imshow(img)

# #hold the window
# plt.waitforbuttonpress()
# plt.close('all')

# # Python program to explain cv2.imread() method 

# # importing cv2 
# # import cv2 

# # # path 
# # path = r'C:\Users\DELL\OneDrive\Desktop\Main Folder\1.png.png'

# # # Using cv2.imread() method 
# # # Using 0 to read image in grayscale mode 
# # img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 

# # # Displaying the image 
# # cv2.imshow('image', img) 
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()


# # Python program to explain cv2.imread() method 

# importing cv2 
# import cv2 

# # path 
# path = r'C:\Users\DELL\OneDrive\Desktop\Main Folder\pic23-300x243.png'

# # Using cv2.imread() method 
# # Using 0 to read image in grayscale mode 
# img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 

# # Displaying the image 
# cv2.imshow('image', img) 
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Python program to illustrate 
# arithmetic operation of 
# bitwise AND of two images 
	
# # organizing imports 
# import cv2 
# import numpy as np 
	
# # path to input images are specified and 
# # images are loaded with imread command 
# img1 = cv2.imread(r'C:\Users\DELL\OneDrive\Desktop\Main Folder\1bit1.png') 
# img2 = cv2.imread(r'C:\Users\DELL\OneDrive\Desktop\Main Folder\2bit2.png') 

# # cv2.bitwise_and is applied over the 
# # image inputs with applied parameters 
# dest_and = cv2.bitwise_and(img2, img1, mask = None) 

# # the window showing output image 
# # with the Bitwise AND operation 
# # on the input images 
# cv2.imshow('Bitwise And', dest_and) 

# # De-allocate any associated memory usage 
# if cv2.waitKey(0) & 0xff == 27: 
# 	cv2.destroyAllWindows() 

# Python program to illustrate 
# arithmetic operation of 
# bitwise OR of two images 
	
# # organizing imports 
# import cv2 
# import numpy as np 
	
# # path to input images are specified and 
# # images are loaded with imread command 
# img1 = cv2.imread(r'C:\Users\DELL\OneDrive\Desktop\Main Folder\1bit1.png') 
# img2 = cv2.imread(r'C:\Users\DELL\OneDrive\Desktop\Main Folder\2bit2.png') 

# # cv2.bitwise_or is applied over the 
# # image inputs with applied parameters 
# dest_or = cv2.bitwise_or(img2, img1, mask = None) 

# # the window showing output image 
# # with the Bitwise OR operation 
# # on the input images 
# cv2.imshow('Bitwise OR', dest_or) 

# # De-allocate any associated memory usage 
# if cv2.waitKey(0) & 0xff == 27: 
# 	cv2.destroyAllWindows() 


# Python program to illustrate 
# arithmetic operation of 
# bitwise XOR of two images 
	
# # organizing imports 
# import cv2 
# import numpy as np 
	
# # path to input images are specified and 
# # images are loaded with imread command 
# img1 = cv2.imread(r'C:\Users\DELL\OneDrive\Desktop\Main Folder\1bit1.png') 
# img2 = cv2.imread(r'C:\Users\DELL\OneDrive\Desktop\Main Folder\2bit2.png') 

# # cv2.bitwise_xor is applied over the 
# # image inputs with applied parameters 
# dest_xor = cv2.bitwise_xor(img1, img2, mask = None) 

# # the window showing output image 
# # with the Bitwise XOR operation 
# # on the input images 
# cv2.imshow('Bitwise XOR', dest_xor) 

# # De-allocate any associated memory usage 
# if cv2.waitKey(0) & 0xff == 27: 
# 	cv2.destroyAllWindows() 

# Python program to illustrate 
# arithmetic operation of 
# bitwise NOT on input image 
	
# # organizing imports 
# import cv2 
# import numpy as np 
	
# # path to input images are specified and 
# # images are loaded with imread command 
# img1 = cv2.imread(r'C:\Users\DELL\OneDrive\Desktop\Main Folder\1bit1.png') 
# img2 = cv2.imread(r'C:\Users\DELL\OneDrive\Desktop\Main Folder\2bit2.png') 

# # cv2.bitwise_not is applied over the 
# # image input with applied parameters 
# dest_not1 = cv2.bitwise_not(img1, mask = None) 
# dest_not2 = cv2.bitwise_not(img2, mask = None) 

# # the windows showing output image 
# # with the Bitwise NOT operation 
# # on the 1st and 2nd input image 
# cv2.imshow('Bitwise NOT on image 1', dest_not1) 
# cv2.imshow('Bitwise NOT on image 2', dest_not2) 

# # De-allocate any associated memory usage 
# if cv2.waitKey(0) & 0xff == 27: 
# 	cv2.destroyAllWindows() 

# Python program to explain cv2.imshow() method

# importing cv2
import cv2

# path
path = r'C:\Users\DELL\OneDrive\Desktop\Main Folder\geeks14.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'image'

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()


