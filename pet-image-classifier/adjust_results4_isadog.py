def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Adds key-value pairs to the results dictionary.

    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. The list contains:
                      index 0 = pet image label (string)
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int) where 1 = match between pet image and 
                        classifer labels and 0 = no match between labels
      dogfile - A text file that contains names of all dogs from the classifier 
                function and pet image files. This file has one dog name per line,
                and dog names are all in lowercase with spaces separating the 
                distinct words of the dog name. Dog names from the classifier function
                can be a string of dog names separated by commas when a particular 
                breed of dog has multiple dog names associated with that breed.
                
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    
    # Create a dictionary to hold the dog names        
    dognames_dic = dict()

    # Read the dog names from the dogfile
    with open (dogfile,"r") as df:
      rd_line = df.readline()

      while rd_line != "":
        # Process each line to remove whitespace and convert to lowercase
        rd_line = rd_line.lower().strip()

        # Add the dog name to the dictionary
        if rd_line not in dognames_dic:
          dognames_dic[rd_line] = 1
        else:
          dognames_dic[rd_line] = 0

        rd_line = df.readline()

      # Update the results dictionary with dog/not-dog classification
      for key in results_dic:
         # Check if pet image label is a dog name
         if results_dic[key][0] in dognames_dic:
            # Check if classifier label is also a dog name
            if results_dic[key][1] in dognames_dic:
              results_dic[key].extend((1, 1))
            else:
              results_dic[key].extend((1, 0))
            
         else:
          # Check if classifier label is a dog name
          if results_dic[key][1] in dognames_dic:
            results_dic[key].extend((0, 1))
          else:
            results_dic[key].extend((0, 0))


