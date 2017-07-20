from abc import ABCMeta, abstractmethod
import numpy as np


class IPreprocessor(metaclass=ABCMeta):
    """
    """

    def __init__(self, config, dataset):
        import util.constant as const

        self.dataset = dataset

        self._whole_data = None
        self._part_data = None

        try:
            self._check_config(config)
        except KeyError:
            raise
        except:
            raise

        self._preprocessor_config = config[const.CFG_RESULT][const.CFG_PREPROCESSOR]
        self.__name = self._preprocessor_config[const.CFG_NAME]

    def _check_config(self, config):
        import util.constant as const

        if const.CFG_RESULT not in config:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_RESULT, 'root')

        if const.CFG_PREPROCESSOR not in config[const.CFG_RESULT]:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_PREPROCESSOR, const.CFG_PROBLEM)

        if const.CFG_NAME not in config[const.CFG_RESULT][const.CFG_PREPROCESSOR]:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_NAME, const.CFG_PREPROCESSOR)

    @abstractmethod
    def process(self):
        pass

    def set_data(self, data):
        """
        :param data: dataset to train on, need to be set before calling IModel.train()
        :return: None
        """
        self._whole_data = data

    @abstractmethod
    def part_data(self):
        """
        function to split whole_data into parts thus changing data to train on
        :return: None
        """
        self._part_data = []

    @property
    def name(self):
        return self.__name

    @property
    def temp_dir(self):
        import util.constant as const
        return const.TEMP_DIR


def dense_to_one_hot(dense_label, num_class):
    """Convert class labels from scalars to one-hot vectors."""
    num_label = dense_label.shape[0]
    index_offset = np.arange(num_label) * num_class
    labels_one_hot = np.zeros((num_label, num_class))
    labels_one_hot.flat[index_offset + dense_label.ravel()] = 1
    return labels_one_hot


def int_to_float(np_array, max_value):
    np_array = np_array.astype(np.float32)
    np_array = np.multiply(np_array, 1.0 / max_value)
    return np_array
