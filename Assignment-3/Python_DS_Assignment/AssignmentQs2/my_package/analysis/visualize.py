#Imports
from PIL import Image,ImageDraw,ImageFont
import numpy as np
def plot_boxes(prediction_boxes,prediction_class,image): # Write the required arguments

    # The function should plot the predicted boxes on the images and save them.
    # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
    
    image = (image.transpose(1,2,0) * 255).astype(np.uint8) 

    img = Image.fromarray(image)
    draw = ImageDraw.Draw(img)

    for i in range(min(5,len(prediction_boxes))):
        box = prediction_boxes[i]
        draw.rectangle(box,outline="rgb(0, 255, 0)",width = 2)

    return img
