from abc import ABCMeta


class IDataset(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        """
        :param config: root dictionary of configuration for dataset interface, "data-dir" field must be present
        """
        import util.constant as const
        try:
            self.dataset_config = config[const.CFG_PROBLEM][const.CFG_DATASET]
        except KeyError:
            raise KeyError('Dataset configuration is not found')
        try:
            self.name = self.dataset_config[const.CFG_NAME]
            self.data_dir = self.dataset_config[const.CFG_DATA_DIR]
        except:
            raise

    def get_data(self):
        pass

    def get_dimension(self):
        pass

    def get_name(self):
        return self.name
