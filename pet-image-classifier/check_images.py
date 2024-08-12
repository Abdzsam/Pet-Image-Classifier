from time import time, sleep

from print_functions_for_lab_checks import *

from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    """
    Main function to run the pet image classifier pipeline. It includes:
    - Parsing command line arguments
    - Getting pet image labels
    - Classifying images
    - Adjusting results for dog/non-dog classification
    - Calculating statistics on the results
    - Printing the results and statistics
    """
    
     # Record the start time of the program
    start_time = time()
    
    # Parse command line arguments
    in_arg = get_input_args()

  # Check the command line arguments
    check_command_line_arguments(in_arg)

# Get pet labels from the image directory
    results = get_pet_labels(in_arg.dir)

# Check the pet image labels
    check_creating_pet_image_labels(results)

# Classify the images using the specified CNN model architecture
    classify_images(in_arg.dir, results, in_arg.arch)
   
   # Check the image classification results
    check_classifying_images(results)    

    # Adjust the results for dog/non-dog classification
    adjust_results4_isadog(results, in_arg.dogfile)

    # Check the labels for dog/non-dog classification
    check_classifying_labels_as_dogs(results)

    # Calculate statistics on the results
    results_stats = calculates_results_stats(results)

# Check the calculated results
    check_calculating_results(results, results_stats)

# Print the results and statistics
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Introduce a short sleep period (can be adjusted or removed)
    sleep(0)
    # Record the end time of the program
    end_time = time()
    
    # Calculate the total runtime
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )

# Check if the script is run directly (and not imported as a module)
if __name__ == "__main__":
    main()
