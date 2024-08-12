def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using the classifier's model 
    architecture to classify pet images. Then puts the results statistics in a dictionary 
    (results_stats_dic) so that it's returned for printing as to help the user determine 
    the 'best' model for classifying images. Note that the statistics calculated are either 
    percentages or counts.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a List. The list 
                    contains the following items:
                      index 0 = pet image label (string)
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int) where 1 = match between pet image and 
                                classifier labels and 0 = no match between labels
                      index 3 = 1/0 (int) where 1 = pet image 'is-a' dog and 
                                0 = pet Image 'is-NOT-a' dog.
                      index 4 = 1/0 (int) where 1 = Classifier classifies image 
                                'as-a' dog and 0 = Classifier classifies image 
                                'as-NOT-a' dog.
                    
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                         a percentage or a count) where the key is the statistic's 
                         name (starting with 'pct' for percentage or 'n' for count)
                         and the value is the statistic's value.
    """
    
    # Initialize a dictionary to hold the results statistics
    results_stats_dic = dict()

    # Initialize counters for the statistics
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    # Process each entry in the results dictionary
    for key in results_dic:
        # Count matches between pet image labels and classifier labels
        if results_dic[key][2] == 1:
                results_stats_dic['n_match'] += 1
        # Count correct breed matches
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
                results_stats_dic['n_correct_breed'] += 1
        # Count number of dog images
        if results_dic[key][3] == 1:
                results_stats_dic['n_dogs_img'] += 1
                # Count correct dog classifications
                if results_dic[key][4] == 1:
                        results_stats_dic['n_correct_dogs'] += 1
        else:
                # Count correct non-dog classifications
                if results_dic[key][3] == 0 and results_dic[key][4] == 0:
                        results_stats_dic['n_correct_notdogs'] += 1


    # Total number of images
    results_stats_dic['n_images'] = len(results_dic)
    # Number of non-dog images
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - results_stats_dic['n_dogs_img'])
    
    # Calculate percentages
    results_stats_dic['pct_match'] = (results_stats_dic['n_match']/results_stats_dic['n_images']) * 100
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs']/results_stats_dic['n_dogs_img']) * 100
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed']/results_stats_dic['n_dogs_img']) * 100

    # Calculate percentage of correct non-dog classifications
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /results_stats_dic['n_notdogs_img'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    return results_stats_dic
