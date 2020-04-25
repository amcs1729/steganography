import cv2
import numpy as np
import math
import helping
import sys
import os

sys.dont_write_bytecode = True






def encode_image():


     
    if(os.name=="posix"):
	c= "/"
    else:
	c= "\\"
	
    

    img_path = raw_input(
        "Enter path of image to use. Provide full path with extension \n")


    try:
        image_sequence = cv2.imread(img_path)
    except:
        print("Oops!! Image not found :(")
        sys.exit()

    


    delta = image_sequence.copy()
    dest_path = img_path[img_path.rindex(c)+1:]
    ext = dest_path[dest_path.rindex("."):]
    name = dest_path[:dest_path.rindex(".")]

    dest_path = name+"_encrypted"
    dest_path += ".png"

    message = raw_input("Enter message to encrypt:")
    length_req = ((len(message) + ((len(message)) % 2))*8) + 8
    img_y = image_sequence.shape[0]
    img_x = image_sequence.shape[1]
    pixels = img_x*img_y
    if(length_req > pixels):
        print("Sorry input message too long..Try another picture with more resolution")
        sys.exit()

    text = str(helping.binary(message))
    length = len(text)
    skip = 0
    length = helping.decimalToBinarystring(len(text))
    counter = 0
    x_encode = 0
    y_encode = 0
    cou = 0

    for i in range(8):

        alpha = length[(3*i)]
        beta = (length[(3*i)+1])
        gamma = (length[(3*i)+2])
        seq = [alpha, beta, gamma]

        for val in range(3):
            cou += 1
            image_sequence = helping.change_val(
                image_sequence=image_sequence, x=x_encode, y=y_encode, channel=val, ch=seq[val])

        x_encode += 1
        if(x_encode >= img_x):
            y_encode += 1
            x_encode -= img_x

    for ch in text:
        x_encode += skip
        skip = int(ch, 10)
        if(x_encode >= img_x):
            y_encode += 1
            x_encode -= img_x
        for channel in range(3):
            image_sequence = helping.change_val( image_sequence=image_sequence, x=x_encode, y=y_encode, channel=channel, ch=ch)
        x_encode += 1

    im2 = image_sequence.copy()

    cv2.imshow(dest_path, im2)
    key = cv2.waitKey(0)
    if(key == ord('q') or key == ord('s')):
        cv2.destroyAllWindows
    if(key == ord('s')):
        cv2.imwrite(dest_path, im2)
        print("IMAGE SAVED ")


