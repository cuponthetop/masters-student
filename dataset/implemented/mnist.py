import numpy as np
import struct
from dataset.base import IDataset

from util.file import clean_dir
from util.download import download_files, concatenate_urls


MNIST_IMAGE_MAGIC = 2051
MNIST_LABEL_MAGIC = 2049


class MNIST(IDataset):
    def __init__(self, config):
        super().__init__(config)
        self.__data = {}

    def _check_config(self, config):
        super()._check_config(config)

    def get_data(self):
        """
        :return: MNIST Dataset
        """

        common_url = "http://yann.lecun.com/exdb/mnist/"

        file_distinct_urls = [
            "train-images-idx3-ubyte.gz",
            "train-labels-idx1-ubyte.gz",
            "t10k-images-idx3-ubyte.gz",
            "t10k-labels-idx1-ubyte.gz"
        ]

        # look for data

        # if there, load
        # d = np.load('test3.npy')...

        # if not there, download
        # set directory
        save_path = self.temp_dir

        clean_dir(save_path)

        file_urls = concatenate_urls(common_url, file_distinct_urls)
        filepaths = concatenate_urls(save_path, file_distinct_urls)

        # download files
        result = download_files(file_urls=file_urls, filepaths=filepaths)

        # extract
        self.__data["train_image"] = extract_image(save_path + "train-images-idx3-ubyte.gz")
        self.__data["train_label"] = extract_label(save_path + "train-labels-idx1-ubyte.gz")
        self.__data["test_image"] = extract_image(save_path + "t10k-images-idx3-ubyte.gz")
        self.__data["test_label"] = extract_label(save_path + "t10k-labels-idx1-ubyte.gz")

        # save data
        np.save(self.data_dir + "mnist-train-image.npy", self.__data["train_image"])
        np.save(self.data_dir + "mnist-train-label.npy", self.__data["train_label"])
        np.save(self.data_dir + "mnist-test-image.npy", self.__data["test_image"])
        np.save(self.data_dir + "mnist-test-label.npy", self.__data["test_label"])

        return self.__data

    def get_dimension(self):
        return {data.shape for data in self.__data}


def extract_image(filename):
    import gzip
    with gzip.open(filename) as file:
        magic, num_image, height, width = struct.unpack('>iiii', file.read(16))
        if magic != MNIST_IMAGE_MAGIC:
            raise ValueError("Wrong magic number reading MNIST image file")
        array = np.frombuffer(file.read(), dtype='uint8')
        array = array.reshape([num_image, height, width, 1])
    return array


def extract_label(filename):
    import gzip
    with gzip.open(filename) as file:
        magic, num_label = struct.unpack('>ii', file.read(8))
        if magic != MNIST_LABEL_MAGIC:
            raise ValueError("Wrong magic number reading MNIST label file")
        array = np.frombuffer(file.read(), dtype='uint8')
        array = array.reshape(num_label, 1)
    return array
