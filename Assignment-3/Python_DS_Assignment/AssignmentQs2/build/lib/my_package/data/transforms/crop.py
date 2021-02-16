#Imports
from PIL import Image
from random import randrange

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

        # Write your code here
        self.shape = shape
        self.crop_type = crop_type
        

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        self.img = image

        previous_width,previous_height = self.img.size
        new_height,new_width = self.shape

        if self.crop_type == "center":

            left = (previous_width - new_width)/2
            top = (previous_height - new_height)/2
            right = (previous_width + new_width)/2
            bottom = (previous_height + new_height)/2

            self.img = self.img.crop((left,top,right,bottom))

        elif self.crop_type == "random":

            left = randrange(0,previous_width - new_width)
            top = randrange(0,previous_height - new_height)
            right = left + new_width
            bottom = top + new_width

            self.img = self.img.crop((left,top,right,bottom))

 
        return self.img

        







        

 