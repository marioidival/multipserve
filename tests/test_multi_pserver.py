import multipserve.core_mps as mps
import unittest
import os

class MultiPserverTest(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.dirname(os.path.realpath(__file__))
        self.mockapp_dir = os.path.join(self.test_dir, 'mockapp')
        self.mockapp_dev_file = os.path.join(self.mockapp_dir,
                                             'development.ini')
        self.mpobj = mps.MultiPserve([self.mockapp_dir])

    def test_search_for_pastfile(self):
        self.assertTrue(os.path.isfile(self.mockapp_dev_file))
        self.assertTrue(os.path.isfile(self.mockapp_dev_file))
        self.assertEqual(None, mps.return_pastfile(self.test_dir))
        self.assertEqual(self.mockapp_dev_file,
                         mps.return_pastfile(self.mockapp_dir))

    def test_count_projects(self):
        self.assertTrue(len(self.mpobj.projects))

    def test_mockdir_in_project(self):
        assert self.mockapp_dir in self.mpobj.projects  # python 2.6

    def test_mock_pastfile_is_returned_by_mps(self):
        self.assertEqual(self.mockapp_dev_file,
                         self.mpobj.projects[self.mockapp_dir])
