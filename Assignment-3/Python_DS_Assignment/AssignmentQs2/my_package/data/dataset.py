#Imports
import json
from PIL import Image
import numpy as np


class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''

        self.annotation_file = annotation_file
        self.transforms = transforms

        with open(self.annotation_file, 'r') as json_file:
            self.annotation_list = list(json_file)
        
        # for json_str in self.annotations_list:
        #     result = json.loads(json_str)
            
    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.annotation_list)


    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the array would be (3, H, W).
            3. Scale the values in the array to be with [0, 1].
            4. Create a dictonary with both the image and annotations
            4. Perform the desired transformations.
            5. Return the transformed image and annotations as specified.
        '''
        annotation = json.loads(self.annotation_list[idx])
        imgfile = annotation["img_fn"]
        image = Image.open('./data/'+imgfile)
        img_array = np.array(image,np.float64)

        dim = img_array.shape

        transformed_image = self.transforms[2](image)
        image.show()
        transformed_image.show()

        # for i in range(dim[0]):
        #     for j in range(dim[1]):
        #         for k in range(dim[2]):
        #             img_array[i,j,k] = img_array[i,j,k]/255.0
        

        # print(img_array[0][0])
        # print(img_array.shape)









        