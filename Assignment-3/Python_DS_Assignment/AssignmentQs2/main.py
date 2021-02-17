#Imports
import math
import matplotlib.pyplot as plt
from numpy.lib.function_base import quantile
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

    dataset = Dataset(annotation_file=annotation_file,transforms=[])

    #Iterate over all data items.
    
    data_dict_list = [dataset[i] for i in range(len(dataset))]

    #Get the predictions from the detector.
    
    predicted_data = []
    for cnt,data_dict in enumerate(data_dict_list):
        predicted_data.append(detector(data_dict["image"]))
        print("Trained "+str(cnt)) 

    #Draw the boxes on the image and save them.

    for i in range(len(data_dict_list)):
        image = show_boxes(prediction_data=predicted_data[i],image = data_dict_list[i]["image"])
        image.save(outputs+"Image_{}.png".format(i),quality = 95)
        print("Saved Image"+str(i))
    
    #Do the required analysis experiments.

    rows = math.ceil((float)(len(transforms)+1)/3)
    fig = plt.figure(figsize=(rows,3))

    original_img = show_boxes(prediction_data=predicted_data[4],image = data_dict_list[4]["image"])

    ax = fig.add_subplot(rows,3,1)

    ax.imshow(original_img)

    #19CS3001[4]
    for i in range(len(transforms)):

        current_dataset = Dataset(annotation_file,[transforms[i]])
        current_data_dict = current_dataset[4]
        current_predicted_data = detector(current_data_dict["image"])
        current_image = show_boxes(prediction_data=current_predicted_data, image = current_data_dict["image"]) 
        ax = fig.add_subplot(rows,3,i+2)
        ax.imshow(current_image)
        print("Subplot Image[4] :id ="+str(i))

    fig.tight_layout()
    fig.savefig(outputs+'analysis.png', dpi=1500)


def main():
    detector = ObjectDetectionModel()
    experiment('./data/annotations.jsonl', detector,[FlipImage(),BlurImage(1),RescaleImage(2.0),RescaleImage(0.5),RotateImage(270),RotateImage(45)], './Detection_Images/') # Sample arguments to call experiment()


if __name__ == '__main__':
    main()
