import numpy as np
import struct
from dataset.base import IDataset

from util.file import clean_dir, file_exists
from util.download import download_files, concatenate_urls


MNIST_IMAGE_MAGIC = 2051
MNIST_LABEL_MAGIC = 2049

COMMON_URL = "http://yann.lecun.com/exdb/mnist/"

FILE_NAMES = [
    "train-images-idx3-ubyte",
    "train-labels-idx1-ubyte",
    "t10k-images-idx3-ubyte",
    "t10k-labels-idx1-ubyte"
]


class MNIST(IDataset):
    def __init__(self, config):
        super().__init__(config)

    def _check_config(self, config):
        super()._check_config(config)

    def _is_downloaded(self):
        download_path = self.temp_dir

        filepaths = concatenate_urls(download_path, FILE_NAMES, 'gz')

        return all(file_exists(path) for path in filepaths)

    def _is_saved(self):
        save_path = self.data_dir

        filepaths = concatenate_urls(save_path, FILE_NAMES, 'npy')

        return all(file_exists(path) for path in filepaths)

    def _load_data(self):
        from os.path import join
        save_path = self.data_dir

        self._set_data = ("train_image", np.load(join(save_path, "mnist-train-image.npy")))
        self._set_data = ("train_label", np.load(join(save_path, "mnist-train-label.npy")))
        self._set_data = ("test_image", np.load(join(save_path, "mnist-test-image.npy")))
        self._set_data = ("test_label", np.load(join(save_path, "mnist-test-label.npy")))

    def _download_data(self):
        """
        :return: MNIST Dataset
        """

        save_path = self.temp_dir

        clean_dir(save_path)

        file_urls = concatenate_urls(COMMON_URL, FILE_NAMES, 'gz')
        file_paths = concatenate_urls(save_path, FILE_NAMES, 'gz')

        # download files
        return download_files(file_urls, file_paths)
    
    def _process_data(self):
        from os.path import join
        save_path = self.temp_dir
        # extract
        self._set_data = ("train_image", extract_image(join(save_path, "train-images-idx3-ubyte.gz")))
        self._set_data = ("train_label", extract_label(join(save_path, "train-labels-idx1-ubyte.gz")))
        self._set_data = ("test_image", extract_image(join(save_path, "t10k-images-idx3-ubyte.gz")))
        self._set_data = ("test_label", extract_label(join(save_path, "t10k-labels-idx1-ubyte.gz")))

    def _save_data(self):
        from os.path import join
        clean_dir(self.data_dir)
        # save data
        np.save(join(self.data_dir, "mnist-train-image.npy"), self.data["train_image"])
        np.save(join(self.data_dir, "mnist-train-label.npy"), self.data["train_label"])
        np.save(join(self.data_dir, "mnist-test-image.npy"), self.data["test_image"])
        np.save(join(self.data_dir, "mnist-test-label.npy"), self.data["test_label"])


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
