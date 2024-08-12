import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__

# Load pretrained models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

# Dictionary to map model names to model objects
models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Load the mapping from ImageNet class IDs to human-readable labels
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    """
    Classifies an image using a specified pretrained CNN model.

    Parameters:
    img_path (str): Path to the image file.
    model_name (str): Name of the pretrained model to use ('resnet', 'alexnet', or 'vgg').

    Returns:
    str: Human-readable label of the predicted class.
    """
     
    # Open the image file
    img_pil = Image.open(img_path)

    # Define the preprocessing steps for the image
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Apply the preprocessing steps to the image
    img_tensor = preprocess(img_pil)
    
    # Add a batch dimension (in-place operation)
    img_tensor.unsqueeze_(0)
    
    # Check the version of PyTorch
    pytorch_ver = __version__.split('.')
    
     # Disable gradient calculation based on PyTorch version
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)
    
    else:
        data = Variable(img_tensor, volatile = True) 

# Get the specified model and set it to evaluation mode
    model = models[model_name]

    model = model.eval()
    
    # Perform the forward pass and get the output
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        output = model(img_tensor)

    else:
        output = model(data)

# Get the index of the predicted class
    pred_idx = output.data.numpy().argmax()

# Return the human-readable label of the predicted class
    return imagenet_classes_dict[pred_idx]
