from abc import ABCMeta, abstractmethod
from util.list import find


class IModel(metaclass=ABCMeta):
    """
    """

    def __init__(self, config, preprocessor):
        import util.constant as const

        try:
            self._check_config(config)
        except KeyError:
            raise
        except:
            raise

        self.__preprocessor = preprocessor
        self.__plotters = []
        self.__savers = []
        self.__reporters = []
        self.__benchmarkers = []

        self._target_functions = []
        self._current_iteration = 0

        self._model_config = config[const.CFG_MODEL]
        self.__name = self._model_config[const.CFG_NAME]

    def _check_config(self, config):
        import util.constant as const

        if const.CFG_MODEL not in config:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_MODEL, 'root')

        if const.CFG_NAME not in config[const.CFG_MODEL]:
            raise KeyError(const.MSG_KEY_ERROR % const.CFG_NAME, const.CFG_MODEL)

    @abstractmethod
    def stop_training(self):
        """
        :return: return True when master student should stop training the model
        """
        return True

    def train(self, session):
        """
        probably need to change session related part depending on backend type
        :param session:
        :return:
        """
        train_data = self.__preprocessor.part_data()

        train_results = (session.run(target) for target in self._target_functions)

        (plotter.plot() for plotter in self.__plotters if plotter.is_plot())

        (reporter.report() for reporter in self.__reporters if reporter.is_report())

        (saver.save() for saver in self.__savers if saver.is_save())

        (benchmarker.compare() for benchmarker in self.__benchmarkers if benchmarker.is_compare())

        self._current_iteration += 1

    @abstractmethod
    def test(self):
        pass

    def add_plotter(self, plotter):
        """
        :param plotter:
        :return:
        """
        if find((lambda plot_in_list: plotter.get_name() == plot_in_list.get_name()), self.__plotters) is not None:
            self.__plotters.append(plotter)

    def add_saver(self, saver):
        """
        :param saver:
        :return:
        """
        if find((lambda saver_in_list: saver.get_name() == saver_in_list.get_name()), self.__savers) is not None:
            self.__savers.append(saver)

    def add_reporter(self, reporter):
        """

        :param reporter:
        :return:
        """
        if find((lambda reporter_in_list: reporter.get_name() == reporter_in_list.get_name()), self.__reporters) is not None:
            self.__reporters.append(reporter)

    def add_benchmarket(self, benchmarker):
        """

        :param benchmarker:
        :return:
        """
        if find((lambda benchmarker_in_list: benchmarker.get_name() == benchmarker_in_list.get_name()), self.__benchmarkers) is not None:
            self.__benchmarkers.append(benchmarker)

    def remove_plotter(self, plotter_name):
        """

        :param plotter_name:
        :return:
        """
        self.__plotters = filter(lambda plotter_in_list: plotter_name == plotter_in_list.get_name(), self.__plotters)

    def remove_saver(self, saver_name):
        """

        :param saver_name:
        :return:
        """
        self.__savers = filter(lambda saver_in_list: saver_name == saver_in_list.get_name(), self.__savers)

    def remove_reporter(self, reporter_name):
        """

        :param reporter_name:
        :return:
        """
        self.__reporters = filter(lambda reporter_in_list: reporter_name == reporter_in_list.get_name(), self.__reporters)

    def remove_benchmarket(self, benchmarker_name):
        """

        :param benchmarker_name:
        :return:
        """
        self.__benchmarkers = filter(lambda benchmarker_in_list: benchmarker_name == benchmarker_in_list.get_name(), self.__benchmarkers)

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def init_network(self):
        """
        Update self.target_functions accordingly in this function
        :return:
        """
        pass
