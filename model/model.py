from abc import ABCMeta


class IModel(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        self.data = None
        self.plotters = []
        self.savers = []
        self.reporters = []
        self.benchmarkers = []

        import util.constant as const

        try:
            self.model_config = config[const.CFG_MODEL]
        except KeyError:
            raise KeyError('Model configuration is not found')
        try:
            self.name = self.model_config[const.CFG_NAME]
        except:
            raise

    def set_data(self, data):
        self.data = data

    def stop_training(self):
        """
        :return: return True when master student should stop training the model
        """
        return True

    def train(self):
        pass

    def test(self):
        pass

    def add_plotter(self, plotter):
        pass

    def add_saver(self, saver):
        pass

    def add_reporter(self, reporter):
        pass

    def add_benchmarket(self, benchmarker):
        pass

    def remove_plotter(self, plotter_name):
        pass

    def remove_saver(self, saver_name):
        pass

    def remove_reporter(self, reporter_name):
        pass

    def remove_benchmarket(self, benchmarker_name):
        pass

    def get_name(self):
        return self.name

