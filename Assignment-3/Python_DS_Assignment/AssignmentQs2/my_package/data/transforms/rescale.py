#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # Write your code here
        self.output_size = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        # Write your code here
        self.img = image
        if isinstance(self.output_size,int):
            previous_size = self.img.size
            # self.img = self.img.resize((round(previous_size[0]*self.output_size), round(previous_size[1]*self.output_size)))
        elif isinstance(self.output_size,tuple):
            self.img = self.img.resize(self.output_size)

        return self.img
