from collections import namedtuple
from dataset.dataset import IDataset


class MNIST(IDataset):
    def __init__(self, config):
        super().__init__(config)

    def get_data(self):
        """
        :return: MNIST Dataset
        """
        "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
        "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz"
        "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz"
        "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"

        return []

    def get_dimension(self):
        return namedtuple('Dimension', 'first', 'second')