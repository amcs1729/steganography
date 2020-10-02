# Steganography

Steganography is a method of encryption that is used to securely transfer message encrypted within an image. The LSB steganography technique is a common and popularly used technique but is quiet vulnerable to frequency attacks and therefore less secure. In this project, I attempt to build a program that relies on the message itself to choose the bits to encrypt and therefore it is much less vulnerable to failre due to frequency attacks.
The project contains a encoder and decoder method that can be accessed from the main method.



Please note that the idea behind the project is not mine and i donot own the copyright to this research paper.I have just tried to implememnt the idea which can be found in this publication[1].



Reference:

[1]Swain, Gandharba & Kumar, Dodda & Pradhan, Anita & Lenka, Saroj. (2010). A Technique for Secure Communication Using Message Dependent Steganography. IJCCT. 2. 


# Building the project on local machine

1) First clone the repo and pull it to local machine.

2) Make sure you have python and pip installed on your computer

3) Navigate to the folder of the repo on local machine

4) Run
   pip install -r requirements.txt
   
5) Run
  python main.py
