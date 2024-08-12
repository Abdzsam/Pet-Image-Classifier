from classifier import classifier 


def classify_images(images_dir, results_dic, model):
   
    for key in results_dic:
       model_label = images_dir + "" + key
       model_label = classifier(model_label,model)

       model_label = model_label.lower()
       model_label = model_label.strip()


       true_value = results_dic[key][0]

       if true_value in model_label:
        results_dic[key].extend([model_label,1])
      
       else:
        results_dic[key].extend([model_label,0])