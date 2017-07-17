from abc import ABCMeta


class IReporter(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        import util.constant as const

        try:
            self.reporter_config = config[const.CFG_RESULT][const.CFG_REPORTER]
        except KeyError:
            raise KeyError('Reporter configuration is not found')
        try:
            self.name = self.reporter_config[const.CFG_NAME]
        except:
            raise

    def is_report(self):
        pass

    def report(self):
        pass

    def on_training_end(self):
        pass

    def get_name(self):
        return self.name
