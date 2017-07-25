from preprocessor.base import IPreprocessor
import numpy as np


class MNISTGeneration(IPreprocessor):
    """
    """

    def __init__(self, config, dataset):
        import util.constant as const
        super().__init__(config, dataset)

        self.dataset = dataset

        self._whole_data = None
        self._part_data = None

    def _check_config(self, config):
        super()._check_config(config)

    def process(self):
        super().process()

        pass

    def part_data(self):
        """
        function to split whole_data into parts thus changing data to train on
        :return: None
        """
        self._part_data = []
