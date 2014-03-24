import multi_pserve.multi_pserver as mps
import unittest
import os

class MultiPserverTest(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.dirname(os.path.realpath(__file__))
        self.mockapp_dir = os.path.join(self.test_dir,'mockapp')
        self.mockapp_dev_file = os.path.join(self.mockapp_dir,'development.ini')

    def test_search_for_pastfile(self):
        self.assertTrue(os.path.isfile(self.mockapp_dev_file))
        self.assertTrue(os.path.isfile(self.mockapp_dev_file))
        self.assertEqual(None, mps.return_pastfile(self.test_dir))
        self.assertEqual(self.mockapp_dev_file, mps.return_pastfile(self.mockapp_dir))

    def test_MultiPserve(self):
        print self.test_dir
        mpobj = mps.MultiPserve([self.mockapp_dir])
        self.assertTrue(len(mpobj.projects))
        self.assertIn(self.mockapp_dir,mpobj.projects)
        self.assertEqual(self.mockapp_dev_file,mpobj.projects[self.mockapp_dir])
        mpobj.load_server(self.mockapp_dir)
        
