# Pet-Image-Classifier
This project is a pet image classification system implemented in Python. It uses a Convolutional Neural Network (CNN) to classify images of pets and determine whether the pet in the image is a dog and identify its breed. The project is organized into multiple modules to handle different aspects of the classification process.

# Features
* Image Classification: Classifies images to identify if the pet is a dog and, if so, determines the breed.
* Statistics Calculation: Computes various statistics on the classification results, such as the number of correct matches, correct dog identifications, and correct breed   
  identifications.
* Results Adjustment: Adjusts the classification results to include additional metadata.
* Input Arguments Handling: Manages input arguments for running the classification script.
* Results Printing: Provides formatted output of the classification results and statistics.

# Modules
* adjust_results4_isadog.py: Adjusts the results dictionary to include whether the pet image label and the classifier label are of dogs.
* calculates_results_stats.py: Calculates statistics of the results, including the number of correct matches and classifications.
* check_images.py: Entry point for running the classification on a batch of images.
* classifier.py: Contains the CNN model used for classification.
* classify_images.py: Classifies the images using the CNN model.
* get_input_args.py: Parses input arguments required for the script.
* get_pet_labels.py: Extracts pet labels from the image filenames.
* print_results.py: Prints the classification results and statistics.

# How to Use
1.Place your pet images in the pet_images directory.
2.Run the check_images.py script with appropriate arguments to classify the images.
3.View the results and statistics printed by the script or saved in the output files.

```
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
```
