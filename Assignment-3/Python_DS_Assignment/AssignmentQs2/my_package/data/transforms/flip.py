#Imports
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        # Write your code here
        self.flip_type = flip_type


        
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''


        # Write your code here
        self.img = image
        if self.flip_type == 'horizontal':
            self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)

        return self.img
        
       