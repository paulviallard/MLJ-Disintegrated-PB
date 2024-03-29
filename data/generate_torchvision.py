import os
import h5py
import torchvision
from torch.utils.data import DataLoader
from argparse import ArgumentParser


# Initializing the parser
arg_parser = ArgumentParser(description="generate a torchvision dataset")
arg_parser.add_argument(
    "dataset", metavar="dataset", type=str,
    help="name of the dataset"
)
arg_parser.add_argument(
    "path", metavar="path", type=str,
    help="path of the h5 dataset file"
)
arg_list = arg_parser.parse_args()

# Getting the arguments
dataset = arg_list.dataset
dataset_path = arg_list.path


# Loading a folder as dataset
if(os.path.exists(dataset)):
    example_label_train_list = torchvision.datasets.ImageFolder(
        root="./"+dataset+"/train",
        transform=torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
        ])
    )
    example_label_test_list = torchvision.datasets.ImageFolder(
        root="./"+dataset+"/test",
        transform=torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
        ])
    )
    test_size = len(example_label_test_list)
    train_size = len(example_label_train_list)

# Loading a torchvision dataset
else:
    dataset_fun = None
    exec("dataset_fun = torchvision.datasets."+str(dataset))
    example_label_train_list = dataset_fun(
        root="./data-"+dataset, train=True, download=True,
        transform=torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
        ])
    )
    example_label_test_list = dataset_fun(
        root="./data-"+dataset, train=False, download=True,
        transform=torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
        ])
    )
    test_size = example_label_test_list.data.shape[0]
    train_size = example_label_train_list.data.shape[0]

# Getting the train and test data
example_label_train_loader = DataLoader(
    example_label_train_list,
    batch_size=train_size)
example_label_test_loader = DataLoader(
    example_label_test_list, batch_size=test_size)
example_label_train_list = list(example_label_train_loader)
example_label_test_list = list(example_label_test_loader)
example_train_list = example_label_train_list[0][0]
label_train_list = example_label_train_list[0][1]
example_test_list = example_label_test_list[0][0]
label_test_list = example_label_test_list[0][1]

# Creating the dataset file
dataset_file = h5py.File(dataset_path, "w")
dataset_file["x_train"] = example_train_list
dataset_file["y_train"] = label_train_list
dataset_file["x_test"] = example_test_list
dataset_file["y_test"] = label_test_list
