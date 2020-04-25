import encode
import decode
import sys
sys.dont_write_bytecode = True

def start():
    c = raw_input("Press 1 to encrypt|| 2 to decrypt  ")

    if(c == "1"):
        encode.encode_image()
    elif(c == "2"):
        decode.decode_image()


if __name__ == "__main__":
    start()


   
   
