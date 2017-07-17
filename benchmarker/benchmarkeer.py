from abc import ABCMeta


class IBenchmarker(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        import util.constant as const

        try:
            self.benchmarker_config = config[const.CFG_RESULT][const.CFG_BENCHMARKER]
        except KeyError:
            raise KeyError('Benchmarker configuration is not found')
        try:
            self.name = self.benchmarker_config[const.CFG_NAME]
        except:
            raise

    def compute_score(self):
        pass

    def compare(self):
        pass

    def on_training_end(self):
        pass

    def get_name(self):
        return self.name
