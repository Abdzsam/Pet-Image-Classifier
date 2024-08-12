from os import listdir

def get_pet_labels(image_dir):

    all_images = listdir(image_dir)
    results_dic = dict()
    pet = ""
    
    for i in range(len(all_images)):
      label_arr = all_images[i].split("_")
      for x in label_arr:
        if x.isalpha():
          pet += x.lower() + " "
      if pet not in results_dic:
        results_dic[all_images[i]] = [pet.strip()]
        pet = ""

    return results_dic
