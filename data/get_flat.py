import os
import h5py
import numpy as np
import random
import warnings
from argparse import ArgumentParser

###############################################################################


if __name__ == "__main__":

    np.random.seed(42)
    random.seed(42)
    warnings.filterwarnings('ignore')

    # We create the parser
    arg_parser = ArgumentParser(
        description="generate the breast-cancer dataset")
    arg_parser.add_argument(
        "old_path", metavar="old_path", type=str,
        help="path of the h5 dataset file")
    arg_parser.add_argument(
        "new_path", metavar="new_path", type=str,
        help="path of the h5 dataset file")

    arg_list = arg_parser.parse_args()
    old_path = arg_list.old_path
    new_path = arg_list.new_path

    dataset_file = h5py.File(old_path, "r")

    example_train = np.array(dataset_file["x_train"])
    label_train = np.array(dataset_file["y_train"])
    example_test = np.array(dataset_file["x_test"])
    label_test = np.array(dataset_file["y_test"])

    example_train = np.reshape(example_train, (example_train.shape[0], -1))
    example_test = np.reshape(example_test, (example_test.shape[0], -1))

    if(old_path == new_path):
        dataset_file.close()
    dataset_file = h5py.File(new_path, "w")

    dataset_file["x_train"] = example_train
    dataset_file["y_train"] = label_train
    dataset_file["x_test"] = example_test
    dataset_file["y_test"] = label_test
