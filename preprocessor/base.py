from abc import ABCMeta, abstractmethod


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
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_RESULT, 'root')

        if const.CFG_PREPROCESSOR not in config[const.CFG_RESULT]:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_PREPROCESSOR, const.CFG_PROBLEM)

        if const.CFG_NAME not in config[const.CFG_RESULT][const.CFG_PREPROCESSOR]:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_NAME, const.CFG_PREPROCESSOR)

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
