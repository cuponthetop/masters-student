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
        self.__benchmark_dir = self._benchmarker_config[const.CFG_BENCHMARK_DIR]

    def _check_config(self, config):
        import util.constant as const

        if const.CFG_RESULT not in config:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_RESULT, 'root')

        if const.CFG_BENCHMARKER not in config[const.CFG_RESULT]:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_BENCHMARKER, const.CFG_PROBLEM)

        if const.CFG_NAME not in config[const.CFG_RESULT][const.CFG_BENCHMARKER]:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_NAME, const.CFG_BENCHMARKER)

        if const.CFG_BENCHMARK_DIR not in config[const.CFG_RESULT][const.CFG_BENCHMARKER]:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_BENCHMARK_DIR, const.CFG_BENCHMARKER)

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

    @property
    def benchmark_dir(self):
        return self.__benchmark_dir

