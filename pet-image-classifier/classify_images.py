from classifier import classifier 


def classify_images(images_dir, results_dic, model):
    """
    Classifies images using the specified pretrained CNN model and updates the results dictionary
    with the classifier labels and whether the classifier label matches the true label.

    Parameters:
    images_dir (str): The directory where the images are stored.
    results_dic (dict): Dictionary with key as image filename and value as a list. The list contains:
                        index 0 = pet image label (string).
    model (str): The name of the model to use for classification ('resnet', 'alexnet', or 'vgg').

    Returns:
    None - results_dic is a mutable data type so no return needed.
    """

    for key in results_dic:
       # Create the full path to the image file
       model_label = images_dir + "" + key
       # Classify the image using the specified model
       model_label = classifier(model_label,model)

       # Convert the classifier label to lowercase and strip leading/trailing whitespace
       model_label = model_label.lower()
       model_label = model_label.strip()

       # Get the true label from the results dictionary
       true_value = results_dic[key][0]

       # Check if the true label is in the classifier label
       if true_value in model_label:
        results_dic[key].extend([model_label,1])
      
       else:
        results_dic[key].extend([model_label,0])