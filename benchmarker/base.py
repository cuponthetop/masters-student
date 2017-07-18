from abc import ABCMeta, abstractmethod


class IBenchmarker(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        import util.constant as const
        try:
            self._check_config(config)
        except KeyError:
            raise
        except:
            raise

        self._benchmarker_config = config[const.CFG_RESULT][const.CFG_BENCHMARKER]
        self.__name = self._benchmarker_config[const.CFG_NAME]

    def _check_config(self, config):
        import util.constant as const

        if const.CFG_RESULT not in config:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_RESULT, 'root')

        if const.CFG_BENCHMARKER not in config[const.CFG_RESULT]:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_BENCHMARKER, const.CFG_PROBLEM)

        if const.CFG_NAME not in config[const.CFG_RESULT][const.CFG_BENCHMARKER]:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_NAME, const.CFG_BENCHMARKER)

    @abstractmethod
    def compute_score(self):
        pass

    @abstractmethod
    def compare(self):
        pass

    @abstractmethod
    def on_training_end(self):
        pass

    @property
    def name(self):
        return self.__name
