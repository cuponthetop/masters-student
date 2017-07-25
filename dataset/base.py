from abc import ABCMeta, abstractmethod
import util.constant as const
from os.path import join


class IDataset(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        """
        :param config: root dictionary of configuration for dataset interface, "data-dir" field must be present
        """
        try:
            self._check_config(config)
        except KeyError:
            raise
        except:
            raise

        self._dataset_config = config[const.CFG_PROBLEM][const.CFG_DATASET]
        self.__is_loaded = False
        self.__name = self._dataset_config[const.CFG_NAME]
        self.__data_dir = self._dataset_config[const.CFG_DATA_DIR]
        self.__data = {}

    def _check_config(self, config):
        if const.CFG_PROBLEM not in config:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_PROBLEM, 'root')

        if const.CFG_DATASET not in config[const.CFG_PROBLEM]:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_DATASET, const.CFG_PROBLEM)

        if const.CFG_NAME not in config[const.CFG_PROBLEM][const.CFG_DATASET]:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_NAME, const.CFG_DATASET)

        if const.CFG_DATA_DIR not in config[const.CFG_PROBLEM][const.CFG_DATASET]:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_DATA_DIR, const.CFG_DATASET)

    def load_data(self):
        if not self.__is_loaded:
            if self._is_saved():
                self._load_data()
            else:
                if not self._is_downloaded():
                    self._download_data()
                self._process_data()
                self._save_data()
            self.__is_loaded = True

    @property
    def data(self):
        return self.__data

    @data.setter
    def _set_data(self, name_data):
        name, data = name_data
        if name not in self.__data:
            self.__data[name] = data
        else:
            raise KeyError

    @property
    def get_dimension(self):
        if not self.__is_loaded:
            raise Exception('Load dataset first')
        return {data.shape for data in self._data}

    @property
    def name(self):
        return self.__name

    @property
    def data_dir(self):
        return join(const.CFG_PROBLEM, const.CFG_DATASET, self.__data_dir)

    @property
    def temp_dir(self):
        return join(const.CFG_PROBLEM, const.CFG_DATASET, const.TEMP_DIR)

    @abstractmethod
    def _is_downloaded(self):
        pass

    @abstractmethod
    def _is_saved(self):
        pass

    @abstractmethod
    def _load_data(self):
        pass

    @abstractmethod
    def _download_data(self):
        pass

    @abstractmethod
    def _process_data(self):
        pass

    @abstractmethod
    def _save_data(self):
        pass
