from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image files.
    The pet image labels are used to check the accuracy of the classifier function.

    Parameters:
     image_dir (str): The directory containing the pet images.

    Returns:
     dict: A dictionary with the key as the image filename and the value as a list.
           The list contains the pet image label (string).
    """
    
    # List all files in the image directory
    all_images = listdir(image_dir)
    results_dic = dict()
    pet = ""

# Process each image file   
    for i in range(len(all_images)):
       # Split the filename by underscores to get words
      label_arr = all_images[i].split("_")

      # Concatenate alphabetic parts to form the pet label
      for x in label_arr:
        if x.isalpha():
          pet += x.lower() + " "
      # Add the pet label to the results dictionary
      if pet not in results_dic:
        results_dic[all_images[i]] = [pet.strip()]
        pet = ""

    return results_dic
