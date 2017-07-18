from model.base import IModel


class Autoencoder(IModel):
    """
    """

    def __init__(self, config):
        super().__init__(self, config)
        import util.constant as const

        try:
            self._hyperparameter_config = config[const.CFG_HYPERPARAMETER]
        except KeyError:
            raise KeyError('Hyperparameter configuration is not found')
        try:
            self._stop_iteration = self._hyperparameter_config[const.CFG_MAX_ITERATION]
            self._batch_size = self._hyperparameter_config[const.CFG_BATCH_SIZE]
        except:
            raise

    def _check_config(self, config):
        super()._check_config(config)

    def stop_training(self):
        """
        :return: return True when master student should stop training the model
        """
        return self._current_iteration > self.stop_iteration

    def part_data(self):
        """
        function to split whole_data into parts thus changing data to train on
        :return: None
        """
        self._part_data = []

    def test(self):
        pass

    def init_network(self):
        pass
