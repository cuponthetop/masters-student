

class TensorFlowStudent:
    def __init__(self, config):
        """
        :param config: dictionary of configuration
        """
        from util.package import import_package_from_config
        import util.constant as const

        self.dataset = None
        self.preprocessor = None
        self.model = None
        self.plotter = None
        self.reporter = None
        self.saver = None
        self.benchmarker = None

        try:
            # import specified problem package
            dataset_module = import_package_from_config(config=config[const.CFG_PROBLEM][const.CFG_DATASET])
        except:
            raise
        # create problem
        self.dataset = dataset_module(config)

        try:
            # import specified problem package
            preprocessor_module = import_package_from_config(config=config[const.CFG_PROBLEM][const.CFG_PREPROCESSOR])
        except:
            raise
        self.preprocessor = preprocessor_module(config, self.dataset)

        # create model

        # create result

    def start(self):
        """
        :return: True if successfully trained model, False otherwise
        """
        import tensorflow as tf

        # if necessary part is missing, just return False
        if self.dataset is None:
            return False
        if self.preprocessor is None:
            return False
        if self.model is None:
            return False

        # run problem setting
        self.dataset.get_data()

        processed_data = self.preprocessor.process()

        self.model.set_data(processed_data)

        # init session
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())

        # run model
        while not self.model.stop_training():
            self.model.train()

        # generate results - should be done while training


