from abc import ABCMeta


class IPlotter(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        import util.constant as const

        try:
            self.plotter_config = config[const.CFG_RESULT][const.CFG_PLOTTER]
        except KeyError:
            raise KeyError('Plotter configuration is not found')
        try:
            self.name = self.plotter_config[const.CFG_NAME]
        except:
            raise

    def is_plot(self):
        pass

    def plot(self):
        pass

    def on_training_end(self):
        pass

    def get_name(self):
        return self.name
