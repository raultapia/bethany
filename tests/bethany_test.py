import os
from bethany import bethany

TEST_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/'


def test_file1():
    r = bethany.analyze(TEST_FOLDER + 'file1')
    assert r['BUG'] == 1
    assert r['FIXME'] == 1
    assert r['HACK'] == 1
    assert r['NOTE'] == 1
    assert r['TODO'] == 1


def test_file2():
    r = bethany.analyze(TEST_FOLDER + 'file2')
    assert r['BUG'] == 0
    assert r['FIXME'] == 0
    assert r['HACK'] == 1
    assert r['NOTE'] == 2
    assert r['TODO'] == 1


if __name__ == "__main__":
    test_file1()
    test_file2()
