# Functions 

import numpy as np 
import cv2

def translate_label(x):
    '''
    Function that turns tumor categories to text. 
    Parameters:
        x: Numeric value for tumor
  
    Returns:
        Text translation of tumor category or the number if it does not match a category
    '''
    if x == 1:
        return 'meningioma'
    elif x == 2:
        return 'glioma'
    elif x == 3:
        return 'pituituary'
    else:
        return x
    
def imx_preproc(imx, zero_up_to_one=False, resize=None):
    '''
    Function that preprocess images to put them in the same size and scale pixel values. 
    Parameters: 
        imx: Image to be preprocessed
        zero_up_to_one: Boolean parameter to convert pixel values to a range from 0 to 255 or keep from 0 to 1
        resize: Fraction to what the original image will be resized. 
                e. g. resize = 0.5, the image will be resized to hald of its original size
    
    Returns: 
        imx: processed image
    '''     
    if imx.shape[0] == 256:
        imx = cv2.resize(imx, (0,0), fx=2,fy=2)
    
    if resize is not None:        
        imx = cv2.resize(imx, (0,0), fx=resize,fy=resize)
    
    ### Not sure if it is this
    imx = imx/imx.max() #Values were not normalized
    
    ### Or this
    #     imx = imx/255
    
    if zero_up_to_one:
        return imx
    
    imx = imx*255 #Scale from 0 to 255
    imx = np.round(imx) 
    imx = imx.astype(np.uint8) #np datatype for images
    
    return imx