from abc import ABCMeta


class ISaver(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        import util.constant as const

        try:
            self.saver_config = config[const.CFG_RESULT][const.CFG_SAVER]
        except KeyError:
            raise KeyError('Saver configuration is not found')
        try:
            self.name = self.saver_config[const.CFG_NAME]
        except:
            raise

    def is_save(self):
        pass

    def save(self):
        pass

    def on_training_end(self):
        pass

    def get_name(self):
        return self.name
