import unittest2
import sys
import os

TEST_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/'
SRC_FOLDER = TEST_FOLDER + '../src/'
sys.path.append(SRC_FOLDER)
import bethany

class TestBethany(unittest2.TestCase):
    def test1(self):
        r = bethany.analyze(TEST_FOLDER+'test1')
        self.assertEqual(r['BUG'], 1)
        self.assertEqual(r['FIXME'], 1)
        self.assertEqual(r['HACK'], 1)
        self.assertEqual(r['NOTE'], 1)
        self.assertEqual(r['TODO'], 1)

    def test2(self):
        r = bethany.analyze(TEST_FOLDER+'test2')
        self.assertEqual(r['BUG'], 0)
        self.assertEqual(r['FIXME'], 0)
        self.assertEqual(r['HACK'], 1)
        self.assertEqual(r['NOTE'], 2)
        self.assertEqual(r['TODO'], 1)

if __name__ == '__main__':
    unittest.main()
