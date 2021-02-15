#Imports
from my_package.model import ObjectDetectionModel
from my_package.data import Dataset
from my_package.analysis import show_boxes
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage

def experiment(annotation_file, detector, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        detector: The object detector
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''

    #Create the instance of the dataset.

    dataset = Dataset(annotation_file=annotation_file,transforms=transforms)

    #Iterate over all data items.
    
    data_dict_list = [dataset[i] for i in range(len(dataset))]

    #Get the predictions from the detector.
    
    predicted_data = [detector(data_dict["image"]) for data_dict in data_dict_list]

    #Draw the boxes on the image and save them.

    for i in range(len(data_dict_list)):
        image = show_boxes(prediction_boxes = predicted_data[i][0],prediction_class = predicted_data[i][1],image = data_dict_list[i]["image"])
        image.save(outputs+"img{}.jpg".format(i),'JPEG')

    
    #Do the required analysis experiments.

    


def main():
    detector = ObjectDetectionModel()
    experiment('./data/annotations.jsonl', detector, [FlipImage()], './data/predicted_boxes/') # Sample arguments to call experiment()


if __name__ == '__main__':
    main()