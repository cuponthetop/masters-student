from abc import ABCMeta, abstractmethod


class IDataset(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        """
        :param config: root dictionary of configuration for dataset interface, "data-dir" field must be present
        """
        import util.constant as const
        try:
            self._check_config(config)
        except KeyError:
            raise
        except:
            raise

        self._dataset_config = config[const.CFG_PROBLEM][const.CFG_DATASET]
        self.__name = self._dataset_config[const.CFG_NAME]
        self.__data_dir = self._dataset_config[const.CFG_DATA_DIR]

    def _check_config(self, config):
        import util.constant as const

        if const.CFG_PROBLEM not in config:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_PROBLEM, 'root')

        if const.CFG_DATASET not in config[const.CFG_PROBLEM]:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_DATASET, const.CFG_PROBLEM)

        if const.CFG_NAME not in config[const.CFG_PROBLEM][const.CFG_DATASET]:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_NAME, const.CFG_DATASET)

        if const.CFG_DATA_DIR not in config[const.CFG_PROBLEM][const.CFG_DATASET]:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_DATA_DIR, const.CFG_DATASET)

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_dimension(self):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def data_dir(self):
        return self.__data_dir
