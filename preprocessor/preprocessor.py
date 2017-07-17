from abc import ABCMeta


class IPreprocessor(metaclass=ABCMeta):
    """
    """

    def __init__(self, config, dataset):
        import util.constant as const

        self.dataset = dataset

        try:
            self.preprocessor_config = config[const.CFG_PROBLEM][const.CFG_PREPROCESSOR]
        except KeyError:
            raise KeyError('Preprocessor configuration is not found')
        try:
            self.name = self.preprocessor_config[const.CFG_NAME]
        except:
            raise

    def process(self):
        pass

    def get_name(self):
        return self.name