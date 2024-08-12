import argparse

def get_input_args():
    """
    Parses command line arguments provided by the user when they run the script.
    This function uses Python's argparse module to create and define these arguments.
    
    Command Line Arguments:
      1. --dir: The path to the folder of pet images (default: 'pet_images/')
      2. --arch: The CNN model architecture to use for classification 
                 (default: 'vgg', options: 'resnet', 'alexnet', 'vgg')
      3. --dogfile: The path to the file that contains the list of valid dog names (default: 'dognames.txt')
      
    This function returns these arguments as an ArgumentParser object.
    """
    
    # Create ArgumentParser object
    parser = argparse.ArgumentParser()

# Argument 1: path to the pet images folder
    parser.add_argument("--dir",type = str,default = "pet_images/",help = "path to pet images folder")

 # Argument 2: CNN model architecture
    parser.add_argument("--arch",type = str,default = "vgg",help = "CHoose one CNN Model Architecture: resnet, alexnet, or vgg")

    # Argument 3: path to the dog names file
    parser.add_argument("--dogfile",type = str,default = "dognames.txt",help = "Type in the dog file to access")

    # Parse the arguments
    inp = parser.parse_args()

    # Print the argument values for debugging purposes   
    print("Argument 1:", inp.dir)
    print("Argument 2:", inp.arch)
    print("Argument 3:", inp.dogfile)
     
    return inp
