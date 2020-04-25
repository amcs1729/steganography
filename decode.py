import cv2
import numpy as np
import math
import helping
import sys

sys.dont_write_bytecode = True


def decode_image():
    path = raw_input("Enter path")

    image_sequence = cv2.imread(path)
    img_y = image_sequence.shape[0]
    img_x = image_sequence.shape[1]
    x_encode = 0
    y_encode = 0
    new_length = ''
    for val in range(8):
        for ite in range(3):
            r = image_sequence[y_encode][x_encode][ite]
            r = r & 1
            new_length += str(r)
        x_encode += 1
        if(x_encode >= img_x):
            y_encode += 1
            x_encode -= img_x
    new_length = int(helping.BinaryStringtoDecimal(new_length))
    res = ''
    for val in range(new_length):
        r = image_sequence[y_encode][x_encode][0]
        r = r & 1
        res += str(r)
        x_encode += 1
        x_encode += r
        if(x_encode >= img_x):
            y_encode += 1
            x_encode -= img_x


    decrypted = ''
    for i in range(int((len(res)/8))):
        seq = res[8*i: 8*(i+1)]
        decrypted += (chr(int(helping.BinaryStringtoDecimal(seq))))
    print(decrypted)
