import pytest

class TestClass(object):
    def test_one(self):
        x = "this"
        pytest.set_trace() # this will stop the test and invoke python debugger(pdb), press 'c' to continue
        assert 'h' in x

    def test_two(self):
        assert 2 == 1+1
