from abc import ABCMeta, abstractmethod


class IReporter(metaclass=ABCMeta):
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

        self._reporter_config = config[const.CFG_RESULT][const.CFG_REPORTER]
        self.__name = self._reporter_config[const.CFG_NAME]

    def _check_config(self, config):
        import util.constant as const

        if const.CFG_RESULT not in config:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_RESULT, 'root')

        if const.CFG_REPORTER not in config[const.CFG_RESULT]:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_REPORTER, const.CFG_PROBLEM)

        if const.CFG_NAME not in config[const.CFG_RESULT][const.CFG_REPORTER]:
            raise KeyError(const.CFG_KEY_ERROR_MSG % const.CFG_NAME, const.CFG_REPORTER)

    @abstractmethod
    def is_report(self):
        pass

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def on_training_end(self):
        pass

    @property
    def name(self):
        return self.__name
