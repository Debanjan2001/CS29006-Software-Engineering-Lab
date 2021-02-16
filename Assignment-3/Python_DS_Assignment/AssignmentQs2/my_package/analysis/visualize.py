#Imports
from PIL import Image,ImageDraw
import numpy as np

def plot_boxes(prediction_data,image): # Write the required arguments

    # The function should plot the predicted boxes on the images and save them.
    # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
    
    image = (image.transpose(1,2,0) * 255).astype(np.uint8) 

    img = Image.fromarray(image)
    draw = ImageDraw.Draw(img)

    pred_boxes = prediction_data[0]
    pred_class = prediction_data[1]

    for i in range(min(5,len(pred_boxes))):
        box = pred_boxes[i]
        draw.rectangle(box,outline="rgb(0, 255, 0)",width = 3)
        draw.text(box[0],pred_class[i],fill="rgb(255,0,0)")

    return img
