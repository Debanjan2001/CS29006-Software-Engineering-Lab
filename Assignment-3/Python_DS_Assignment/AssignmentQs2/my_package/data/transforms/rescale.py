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
        dim = self.img.size

        if isinstance(self.output_size,int):

            if dim[0]<dim[1]:
                newdim = (self.output_size,int((dim[1]*self.output_size)/dim[0]))
                self.img = self.img.resize( newdim )
            else:
                newdim =( int((dim[0]*self.output_size)/dim[1]),self.output_size )
                self.img = self.img.resize( newdim )
        
        elif isinstance(self.output_size,tuple):
            self.img = self.img.resize(self.output_size)

        elif isinstance(self.output_size,float):
            newdim = ( int(self.output_size*dim[0]),int(self.output_size*dim[1]) )
            self.img = self.img.resize( newdim)

        return self.img
