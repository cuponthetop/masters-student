import unittest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from util.package import import_name_from_package


class PackageTest(unittest.TestCase):

    def test_module_not_found(self):
        self.assertRaises(ImportError, import_name_from_package,
                          'not-found', 'noname', 'noname')

    def test_name_not_found(self):
        self.assertRaises(ImportError, import_name_from_package,
                          'saver.saver', 'noname', 'noname')

    def test_target_name_collision(self):
        self.assertRaises(ImportError, import_name_from_package,
                          'saver.saver', 'ISaver', 'unittest')

    def test_module_load_success(self):
        import sys
        import_name_from_package('saver.saver', 'ISaver', 'saver')
        self.assertTrue('saver' in sys.modules)


if __name__ == "__main__":
    test = PackageTest()
    test.test_name_not_found()
