from abc import ABCMeta
from util.list import find


class IModel(metaclass=ABCMeta):
    """
    """

    def __init__(self, config):
        self.whole_data = None
        self.part_data = None
        self.plotters = []
        self.savers = []
        self.reporters = []
        self.benchmarkers = []

        self.target_functions = []
        self.current_iteration = 0

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
        """
        :param data: dataset to train on, need to be set before calling IModel.train()
        :return: None
        """
        self.whole_data = data

    def stop_training(self):
        """
        :return: return True when master student should stop training the model
        """
        return True

    def part_data(self):
        """
        function to split whole_data into parts thus changing data to train on
        :return: None
        """
        self.part_data = []

    def train(self, session):
        for target in self.target_functions:
            session.run(target)

        for plotter in self.plotters:
            if plotter.is_plot():
                plotter.plot()

        for reporter in self.reporters:
            if reporter.is_report():
                reporter.report()

        for saver in self.savers:
            if saver.is_save():
                saver.save()

        for benchmarker in self.benchmarkers:
            if benchmarker.is_compare():
                benchmarker.compare()

        self.current_iteration += 1

    def test(self):
        pass

    def add_plotter(self, plotter):
        """
        :param plotter:
        :return:
        """
        if find((lambda plot_in_list: plotter.get_name() == plot_in_list.get_name()), self.plotters) is not None:
            self.plotters.append(plotter)

    def add_saver(self, saver):
        """
        :param saver:
        :return:
        """
        if find((lambda saver_in_list: saver.get_name() == saver_in_list.get_name()), self.savers) is not None:
            self.savers.append(saver)

    def add_reporter(self, reporter):
        """

        :param reporter:
        :return:
        """
        if find((lambda reporter_in_list: reporter.get_name() == reporter_in_list.get_name()), self.reporters) is not None:
            self.reporters.append(reporter)

    def add_benchmarket(self, benchmarker):
        """

        :param benchmarker:
        :return:
        """
        if find((lambda benchmarker_in_list: benchmarker.get_name() == benchmarker_in_list.get_name()), self.benchmarkers) is not None:
            self.benchmarkers.append(benchmarker)

    def remove_plotter(self, plotter_name):
        """

        :param plotter_name:
        :return:
        """
        self.plotters = filter(lambda plotter_in_list: plotter_name == plotter_in_list.get_name(), self.plotters)

    def remove_saver(self, saver_name):
        """

        :param saver_name:
        :return:
        """
        self.savers = filter(lambda saver_in_list: saver_name == saver_in_list.get_name(), self.savers)

    def remove_reporter(self, reporter_name):
        """

        :param reporter_name:
        :return:
        """
        self.reporters = filter(lambda reporter_in_list: reporter_name == reporter_in_list.get_name(), self.reporters)

    def remove_benchmarket(self, benchmarker_name):
        """

        :param benchmarker_name:
        :return:
        """
        self.benchmarkers = filter(lambda benchmarker_in_list: benchmarker_name == benchmarker_in_list.get_name(), self.benchmarkers)

    def get_name(self):
        return self.name

    def init_network(self):
        """
        Update self.target_functions accordingly in this function
        :return:
        """
        pass
