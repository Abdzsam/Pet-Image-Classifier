import argparse

def get_input_args():
    
    parser = argparse.ArgumentParser()

    parser.add_argument("--dir",type = str,default = "pet_images/",help = "path to pet images folder")

    parser.add_argument("--arch",type = str,default = "vgg",help = "CHoose one CNN Model Architecture: resnet, alexnet, or vgg")

    parser.add_argument("--dogfile",type = str,default = "dognames.txt",help = "Type in the dog file to access")

    inp = parser.parse_args()
    print("Argument 1:", inp.dir)
    print("Argument 2:", inp.arch)
    print("Argument 3:", inp.dogfile)
     
    return inp
