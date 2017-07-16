from abc import ABCMeta


class IDataset(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        pass

    def get_data(self):
        pass

    def get_dimension(self):
        pass
